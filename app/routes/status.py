from flask import Blueprint, render_template, session, request, jsonify

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

@status_bp.route('/update/<task_code>', methods=['POST'])
def update_request(task_code):
    requests = session.get('requests', [])
    selected = next((r for r in requests if r.get('taskCode') == task_code), None)
    if not selected:
        return jsonify({'message': f'ไม่พบรหัสงาน {task_code}'}), 404

    data = request.get_json()
    for key, value in data.items():
        if key in selected:
            selected[key] = value

    session['requests'] = requests
    return jsonify({'message': '✅ บันทึกข้อมูลเรียบร้อยแล้ว'})
