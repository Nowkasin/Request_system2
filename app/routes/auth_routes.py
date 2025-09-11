from flask import Blueprint, jsonify, request
import base64
from app.services.sso_service import validate_credentials


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/ldap/RestfulWS/username/<username>/password/<encoded_pass>', methods=['GET'])
def validate_sso(username, encoded_pass):
    try:
        password = base64.b64decode(encoded_pass).decode('utf-8')
    except Exception as e:
        print("❌ Base64 decode error:", e)
        return jsonify({"error": "Invalid password encoding"}), 400

    is_valid = validate_credentials(username, password)
    return jsonify(is_valid)
