import endpoints_scripts

def lambda_handler(event, context):
    """Main entry point for the web service"""

    path = event.get('path', '')
    mthd = event.get('httpMethod', '')
    resp = {'statusCode': 500}  # default response, to be overwritten

    # Each endpoint calls a function
    if mthd == 'GET' and path == '/services/scripts/getlicenses':
        resp = endpoints_scripts.get_licenses()

    # Add headers to http response
    if 'headers' not in resp:
        resp['headers'] = {}

    resp['headers']['Access-Control-Allow-Origin'] = '*'  # CORS

    # Return http response
    return resp
