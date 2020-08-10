import sys
import pymysql

rds_host = 'aaa.bbb.us-east-1.rds.amazonaws.com'
rds_port = 3306
name = 'db_user'
password = 'db_password'
db_name = 'db_name'

def connect():
    """Return connection object to AWS RDS"""
    cxn = pymysql.connect(
        host=rds_host, port=rds_port, connect_timeout=1,
        user=name, passwd=password, db=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    return cxn

def query(query, placeholders=[]):
    """Execute a SQL query against AWS RDS"""
    cxn = connect()
    if cxn is None:
        return
    with cxn.cursor() as cur:
        if len(placeholders) < 1:
            cur.execute(query)
        else:
            cur.execute(query, placeholders)
        return cur.fetchall()
