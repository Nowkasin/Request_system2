from flask import Blueprint, request, render_template, redirect, session
from werkzeug.utils import secure_filename
import os
from datetime import datetime

request_bp = Blueprint('request', __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx', 'png', 'jpg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_fallback_code():
    prefix = 'IQ'
    last = int(session.get('last_task_code', 0)) + 1
    session['last_task_code'] = last
    padded = str(last).zfill(6)
    return f"{prefix}-{padded}"

@request_bp.route('/request', methods=['GET', 'POST'])
def request_form():
    if request.method == 'GET':
        task_code = session.get('task_code_fallback') or generate_fallback_code()
        session['task_code_fallback'] = task_code

        time_options = [f"{h:02d}:{m:02d}" for h in range(8, 19) for m in (0, 30)]
        return render_template('request_form.html', task_code=task_code, time_options=time_options, filtered_end_times=time_options)

    # รับข้อมูลจากฟอร์ม
    form_data = request.form.to_dict()
    files = request.files.getlist('attachments')

    # ตรวจสอบเวลา
    start_time = form_data.get('startTime')
    end_time = form_data.get('endTime')
    if end_time <= start_time:
        return "⚠️ เวลาสิ้นสุดต้องมากกว่าเวลาเริ่ม", 400

    # บันทึกไฟล์
    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            saved_files.append(filename)

    # สร้าง request object
    request_data = {
        "taskCode": form_data.get("taskCode"),
        "selectedCategory": form_data.get("selectedCategory"),
        "type": form_data.get("type"),
        "title": form_data.get("title"),
        "priority": form_data.get("priority"),
        "reporterEmail": form_data.get("reporterEmail"),
        "reporterPhone": form_data.get("reporterPhone"),
        "coordinatoragency": form_data.get("coordinatoragency"),
        "coordinatorEmail": form_data.get("coordinatorEmail"),
        "coordinatorMobile": form_data.get("coordinatorMobile"),
        "assigneeagency": form_data.get("assigneeagency"),
        "assigneeEmail": form_data.get("assigneeEmail"),
        "assigneeMobile": form_data.get("assigneeMobile"),
        "packageCode": form_data.get("packageCode"),
        "sendDate": form_data.get("sendDate"),
        "startTime": start_time,
        "endTime": end_time,
        "details": form_data.get("details"),
        "note": form_data.get("note"),
        "attachments": saved_files,
        "status": "รอการดำเนินการ",
        "createdAt": datetime.now().isoformat()
    }

    # ✅ บันทึกลง database หรือ session
    all_requests = session.get('requests', [])
    all_requests.append(request_data)
    session['requests'] = all_requests

    # สร้าง taskCode ใหม่
    new_code = generate_fallback_code()
    session['task_code_fallback'] = new_code

    return redirect('/status')
