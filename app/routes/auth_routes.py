from flask import Blueprint, request, render_template, redirect, session, flash
import base64
from app.services.sso_service import validate_credentials
from app.services.phonebook_service import fetch_phonebook_info
from app.services.employee_service import save_employee_info

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return redirect('/login')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/home')

    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    encoded_pass = base64.b64encode(password.encode()).decode()

    if not validate_credentials(username, password):
        flash("ไม่พบผู้ใช้ในระบบ SSO", "danger")  # ✅ ใช้ flash แทน
        return redirect('/login')

    user_info = fetch_phonebook_info(username).get("result")
    if not user_info or not user_info.get("full_name"):
        flash("ไม่พบข้อมูลผู้ใช้ในระบบ Phonebook", "danger")  # ✅ ใช้ flash แทน
        return redirect('/login')

    save_employee_info(user_info['employee_no'])

    session['username'] = username
    session['full_name'] = user_info['full_name']
    session['department'] = user_info['position']
    session['role'] = 'admin'
    session['email'] = user_info['email']
    session['employee_no'] = user_info['employee_no']

    return redirect('/home')

@auth_bp.route('/home')
def home():
    # ✅ ป้องกันการเข้าถึงโดยไม่ได้ login
    if 'username' not in session:
        return redirect('/login')
    return render_template('home.html')
