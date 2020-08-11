import json
import rds_helper
import user_utils
import request_utils

def get_licenses():
    qry = 'select id, license, license_desc from licenses'
    res = rds_helper.query(qry)
    payload = {'licenses': res}
    return {'statusCode': 200, 'body': json.dumps(payload)}

def get_user_info(username, password):
    qry = "select * from users where username = %s"
    res = rds_helper.query(qry, [username])

    pw_from_user = user_utils.base64_decode_password(password)
    enc_pw_from_db = res[0]['password']
    
    if not user_utils.validate_password(pw_from_user, enc_pw_from_db):
        return {'statusCode': 401}  # incorrect password

    user = {
        'comment_count': res[0]['comment_count'],
        'created': res[0]['created'].strftime('%Y-%m-%d %H:%M:%S') + '.0',
        'email': res[0]['email'],
        'first_name': res[0]['first_name'],
        'id': res[0]['id'],
        'last_name': res[0]['last_name'],
        'status': res[0]['status'],
        'username': res[0]['username'] 
    }

    xml_out = str(request_utils.xml_serialize(user, 'user'))

    return {
        'statusCode': 200,
        'body': str(xml_out)
    }
