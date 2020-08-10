import json
import rds_helper

def get_licenses():
    qry = 'select id, license, license_desc from licenses'
    res = rds_helper.query(qry)
    payload = {'licenses': res}
    return {'statusCode': 200, 'body': json.dumps(payload)}
