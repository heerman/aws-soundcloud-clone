import json
import request_utils
import endpoints_users

def lambda_handler(event, context):
    """Main entry point for the web service"""

    path = event.get('path', '')
    mthd = event.get('httpMethod', '')
    resp = {'statusCode': 500}  # default response, to be overwritten

    # Each endpoint calls a function
    if mthd == 'GET' and path == '/services/users/getlicenses':
        resp = endpoints_users.get_licenses()

    elif mthd == 'POST' and path == '/services/users/getuserinfo':
        username = request_utils.post_mfd_parameter(event, 'username')
        password = request_utils.post_mfd_parameter(event, 'password')
        resp = endpoints_users.get_user_info(username, password)

    # Add headers to http response
    if 'headers' not in resp:
        resp['headers'] = {}

    resp['headers']['Access-Control-Allow-Origin'] = '*'  # CORS

    # Return http response
    return resp
