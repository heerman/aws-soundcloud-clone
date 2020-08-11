import base64
import hashlib

def base64_decode_password(b64_pw):
    return base64.b64decode(b64_pw).decode('utf-8')

def validate_password(pw_from_user, enc_pw_from_db):
    salt = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    salted_str = (salt + pw_from_user)
    salted_bytes = salted_str.encode()
    enc_pw_from_user = hashlib.sha1(salted_bytes).hexdigest()

    return enc_pw_from_user == enc_pw_from_db
