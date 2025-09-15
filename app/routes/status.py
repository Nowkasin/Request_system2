from flask import Blueprint, render_template, session

status_bp = Blueprint('status', __name__)

@status_bp.route('/status')
def status_page():
    requests = session.get('requests', [])
    return render_template('status.html', request_list=requests)

@status_bp.route('/record/<task_code>')
def view_details(task_code):
    requests = session.get('requests', [])
    selected = next((r for r in requests if r.get('taskCode') == task_code), None)
    if not selected:
        return f"ไม่พบข้อมูลสำหรับรหัสงาน {task_code}", 404
    return render_template('record_detail.html', request=selected)
