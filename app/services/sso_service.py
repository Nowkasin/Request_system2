import requests
import base64

def validate_credentials(username: str, password: str) -> bool:
    try:
        # 🔐 เข้ารหัสรหัสผ่านเป็น base64 ตามระบบ SSO
        encoded_pass = base64.b64encode(password.encode()).decode()

        # 🔗 URL ของ SSO API ที่คุณให้มา
        sso_url = f"http://172.19.107.54:8080/ldap/RestfulWS/username/{username}/password/{encoded_pass}"

        # ✅ ไม่ต้องใช้ Authorization header ถ้า API ไม่ต้องการ
        response = requests.get(sso_url, timeout=5)
        response.raise_for_status()

        # ✅ API ตอบกลับเป็น true หรือ false โดยตรง
        return response.json() is True

    except requests.exceptions.RequestException as e:
        print(f"❌ SSO connection error for user {username}:", e)
        return False
