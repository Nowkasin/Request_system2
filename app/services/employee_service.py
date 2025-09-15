# ส่วนที่บันทึกข้อมูลลง database
from app.models.employee import EmployeeInfo
from app.app import db
from app.services.phonebook_service import fetch_phonebook_info
from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.split(" ")[0], "%Y-%m-%d").date()
    except Exception:
        return None

def save_employee_info(employee_no: str):
    data = fetch_phonebook_info(employee_no).get("result", {})

    if not data:
        print(f"⚠️ No data returned for {employee_no}")
        return False

    now = datetime.now()
    default_date = now.date()
    default_time = now.replace(microsecond=0).time()

    existing = EmployeeInfo.query.filter_by(employee_no=employee_no).first()

    if existing:
        print(f"🔁 Updating existing record for {employee_no}")
        emp = existing
    else:
        print(f"🆕 Creating new record for {employee_no}")
        emp = EmployeeInfo(employee_no=employee_no)
        db.session.add(emp)

    # Map fields
    emp.card_id = data.get('card_id', '')
    emp.title_name_thai = data.get('title_name_thai', '')
    emp.first_name = data.get('first_name', '')
    emp.last_name = data.get('last_name', '')
    emp.full_name = data.get('full_name', '')
    emp.title_name_en = data.get('title_name_en', '')
    emp.english_first_name = data.get('english_first_name', '')
    emp.english_last_name = data.get('english_last_name', '')
    emp.birth_date = parse_date(data.get('birth_date'))
    emp.gender = data.get('gender', '')
    emp.hn = data.get('hn', '')
    emp.position = data.get('position', '')
    emp.email = data.get('email', '')
    emp.affiliation = data.get('affiliation', '')
    emp.employee_type_code = data.get('employee_type_code', '')
    emp.employee_type_name = data.get('employee_type_name', '')
    emp.institution_name = data.get('institution_name', '')
    emp.work = data.get('work', '')
    emp.unit = data.get('unit', '')
    emp.mobile = data.get('mobile', '')
    emp.mobile_2 = data.get('mobile_2', '')
    emp.telephone = data.get('telephone', '')
    emp.telephone_1 = data.get('telephone_1', '')
    emp.telephone_2 = data.get('telephone_2', '')
    emp.telephone_3 = data.get('telephone_3', '')
    emp.line_id = data.get('line_id', '')
    emp.start_date_code = data.get('start_date_code', '')
    emp.start_date = parse_date(data.get('start_date'))
    emp.start_date_name = data.get('start_date_name', '')
    emp.packing_date_code = data.get('packing_date_code', '')
    emp.packing_date = parse_date(data.get('packing_date'))
    emp.packing_date_name = data.get('packing_date_name', '')
    emp.probation_date_code = data.get('probation_date_code', '')
    emp.probation_date = parse_date(data.get('probation_date'))
    emp.probation_date_name = data.get('probation_date_name', '')
    emp.termination_date_code = data.get('termination_date_code', '')
    emp.termination_date = parse_date(data.get('termination_date'))
    emp.termination_name = data.get('termination_name', '')

    # Required audit/log fallbacks
    emp.data_sts00id = emp.data_sts00id or 1
    emp.data_data00date0 = emp.data_data00date0 or default_date
    emp.data_date00time0 = emp.data_date00time0 or default_time
    emp.dbtf_aud00date00date0 = emp.dbtf_aud00date00date0 or default_date
    emp.dbtf_aud00date00time0 = emp.dbtf_aud00date00time0 or default_time

    try:
        db.session.commit()
        print(f"✅ Saved employee info for {employee_no}")
        return True
    except Exception as e:
        db.session.rollback()
        print(f"❌ DB commit failed for {employee_no}:", e)
        return False
