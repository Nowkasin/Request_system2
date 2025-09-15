# app/models/employee.py
import os
from app.app import db
from sqlalchemy import Identity, Integer, UniqueConstraint

class EmployeeInfo(db.Model):
    __tablename__ = os.getenv('DB_TB', 'DBTF_1001PISHRBook00')
    __table_args__ = (
        {'schema': 'dbo'},
    )

    # 🔹 Identity primary key (ให้ SQL Server สร้างเอง)
    DBTF_ID = db.Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)

    # 🔹 System fields
    data_sts00id = db.Column(db.Integer)  # ให้เป็นตัวเลขถ้าใน DB เป็น tinyint/int
    data_token00idcode00 = db.Column(db.String(50))
    data_prg00id = db.Column(db.String(50))
    data_login00id = db.Column(db.String(50))
    data_fnc00id = db.Column(db.String(50))
    data_event00log00id = db.Column(db.String(50))
    data_data00date0 = db.Column(db.Date)
    data_date00time0 = db.Column(db.Time)
    data_user00id = db.Column(db.String(50))
    data_dev00id = db.Column(db.String(50))
    data_loc00latitude00 = db.Column(db.String(50))
    data_loc00longitude00 = db.Column(db.String(50))

    # 🔹 Log fields
    data_log00sts00id = db.Column(db.String(50))
    data_log00token00idcode00 = db.Column(db.String(50))
    data_log00prg00id = db.Column(db.String(50))
    data_log00login00id = db.Column(db.String(50))
    data_log00fnc00id = db.Column(db.String(50))
    data_log00event00log00id = db.Column(db.String(50))
    data_log00data00date0 = db.Column(db.Date)
    data_log00date00time0 = db.Column(db.Time)
    data_log00user00id = db.Column(db.String(50))
    data_log00dev00id = db.Column(db.String(50))
    data_log00loc00latitude00 = db.Column(db.String(50))
    data_log00loc00longitude00 = db.Column(db.String(50))

    # 🔹 Status & audit
    data_dt00def00sts00id = db.Column(db.String(50))
    data_dt00order00no00 = db.Column(db.String(50))
    DBTF_STS00ID = db.Column(db.String(50))
    DBTF_STSS00ID = db.Column(db.String(50))
    DBTF_AUD00ID = db.Column(db.String(50))

    dbtf_aud00sts00id = db.Column(db.String(50))
    dbtf_aud00stss00id = db.Column(db.String(50))
    dbtf_aud00date00date0 = db.Column(db.Date)
    dbtf_aud00date00time0 = db.Column(db.Time)
    dbtf_aud00tran00id = db.Column(db.String(50))

    dbtf_aud01sts00id = db.Column(db.String(50))
    dbtf_aud01stss00id = db.Column(db.String(50))
    dbtf_aud01date00date0 = db.Column(db.Date)
    dbtf_aud01date00time0 = db.Column(db.Time)
    dbtf_aud01tran00id = db.Column(db.String(50))

    DBTF_IMP00ID = db.Column(db.String(50))
    dbtf_imp00sts00id = db.Column(db.String(50))
    dbtf_imp00stss00id = db.Column(db.String(50))
    dbtf_imp00date00date0 = db.Column(db.Date)
    dbtf_imp00date00time0 = db.Column(db.Time)
    dbtf_imp00tran00id = db.Column(db.String(50))
    dbtf_imp00tran00idcode00 = db.Column(db.String(50))
    dbtf_imp00tran01id = db.Column(db.String(50))
    dbtf_imp00tran01idcode00 = db.Column(db.String(50))
    dbtf_imp00tran02id = db.Column(db.String(50))
    dbtf_imp00tran02idcode00 = db.Column(db.String(50))

    # 🔹 Employee info
    # เอา primary_key ออกจาก employee_no (ให้ unique ถ้าต้องการบังคับเอกลักษณ์)
    employee_no = db.Column(db.String(50), nullable=False, unique=True)
    card_id = db.Column(db.String(50))
    title_name_thai = db.Column(db.String(100))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(300))
    full_name = db.Column(db.String(300))
    title_name_en = db.Column(db.String(200))
    english_first_name = db.Column(db.String(200))
    english_last_name = db.Column(db.String(200))
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    hn = db.Column(db.String(20))
    position = db.Column(db.String(200))
    email = db.Column(db.String(200))
    affiliation = db.Column('affiliaction', db.String(200))  # map กับชื่อจริงใน DB
    employee_type_code = db.Column(db.String(20))
    employee_type_name = db.Column(db.String(100))
    institution_name = db.Column(db.String(300))
    work = db.Column(db.String(300))
    unit = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    mobile_2 = db.Column(db.String(20))
    telephone = db.Column(db.String(20))
    telephone_1 = db.Column(db.String(20))
    telephone_2 = db.Column(db.String(20))
    telephone_3 = db.Column(db.String(20))
    line_id = db.Column(db.String(100))

    # 🔹 Employment dates
    start_date_code = db.Column(db.String(20))
    start_date = db.Column(db.Date)
    start_date_name = db.Column(db.String(100))
    packing_date_code = db.Column(db.String(20))
    packing_date = db.Column(db.Date)
    packing_date_name = db.Column(db.String(100))
    probation_date_code = db.Column(db.String(20))
    probation_date = db.Column(db.Date)
    probation_date_name = db.Column(db.String(100))
    termination_date_code = db.Column(db.String(20))
    termination_date = db.Column(db.Date)
    termination_name = db.Column(db.String(100))

    def __repr__(self):
        return f"<EmployeeInfo employee_no={self.employee_no} full_name={self.full_name}>"
