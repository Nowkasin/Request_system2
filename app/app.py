from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime
import os
from dotenv import load_dotenv

db = SQLAlchemy()
login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'dev-secret'

    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_server = os.getenv('DB_SERVER')
    db_name = os.getenv('DB_NAME')
    db_table = os.getenv('DB_TB', 'DBTF_1001PISHRBook00')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mssql+pyodbc://{db_user}:{db_pass}@{db_server}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server"
    )
    app.config['DB_TABLE_NAME'] = db_table

    db.init_app(app)
    login_manager.init_app(app)

    # 🔗 Register Blueprints
    from .routes.request_routes import request_bp
    from .routes.auth_routes import auth_bp
    from .routes.status import status_bp
    app.register_blueprint(status_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(auth_bp)

    # 🧠 Jinja Filter for Date Formatting
    @app.template_filter('format_date')
    def format_date(value):
        try:
            dt = datetime.fromisoformat(value)
            return dt.strftime('%d/%m/%Y')
        except Exception:
            return value

    # 🎨 Status Class Mapping
    @app.context_processor
    def utility_processor():
        def get_status_class(status):
            return {
                'รอการดำเนินการ': 'waiting',
                'กำลังดำเนินการ': 'in-progress',
                'เสร็จสิ้น': 'done'
            }.get(status, '')
        return dict(get_status_class=get_status_class)

    # 📋 Status Page Route
    @app.route('/status')
    def status_page():
        requests = session.get('requests', [])
        return render_template('status.html', request_list=requests)

    return app
