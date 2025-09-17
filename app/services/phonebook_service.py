import requests

def fetch_phonebook_info(username: str) -> dict:
    try:
        phonebook_url = f"http://172.19.107.54:8080/api_phonebook/phonebook/employee_info/{username}"
        print(f"📡 Requesting: {phonebook_url}")  # log URL ที่เรียก

        response = requests.get(phonebook_url, timeout=5)
        print(f"📥 Status Code: {response.status_code}")  # log status code
        print(f"📦 Raw Response: {response.text}")  # log raw response

        response.raise_for_status()
        data = response.json()
        print(f"✅ Parsed JSON: ดึงข้อมูลได้แล้วววววววววววววววววว")  # log JSON ที่แปลงแล้ว

        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ Phonebook API error for user {username}:", e)
        return {}
