import json
import rds_helper

def get_default_audio_tags():
    qry = "select * from audio_tags "
    res = rds_helper.query(qry)
    return {'statusCode': 200, 'body': json.dumps(res)}

def get_default_audio_folders():
    qry = (
        "select TAGS " + 
        "as folder from audio_tags " + 
        "group by TAGS"
    )
    res = rds_helper.query(qry)
    return {'statusCode': 200, 'body': json.dumps(res)}

def get_user_audio_folders():
    qry = (
        "select upper(TAGS) as folder from audio_files " + 
        "group by TAGS"
    )
    res = rds_helper.query(qry)
    return {'statusCode': 200, 'body': json.dumps(res)}

def get_audio_sample(key, tempo=-1):
    # query db
    # get s3 url
    # return redirect to url
    qry = "select * from audio_files where file_key = '" + key + "'"
    res = {'message': 'Not implemented'}
    return {'statusCode': 501, 'body': json.dumps(res)}

def verify_clip(key):
    print('verifyclip endpoint')
    qry = "select * from audio_files where file_key = %s"
    res = rds_helper.query(qry, [key])
    if len(res) < 1:
        return {'statusCode': 500}
    return {'statusCode': 200, 'body': json.dumps(res[0])}
