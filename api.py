from flask import Flask, request
from flask_restful import Resource, Api
import MySQLdb
import json

class DBsystem(object):
    def __init__(self):
        self.db = MySQLdb.connect(host='2239559319.mysql.pythonanywhere-services.com',
                                  user='2239559319',
                                  password='',          #这里密码私密
                                  db='2239559319$default',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return list(self.cursor.fetchall())

    def insert(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        return list(self.cursor.fetchall())

def create_app():
    app = Flask(__name__)
    api = Api(app)
    mysqldb = DBsystem()

    class AutoSubmit(Resource):
        def options(self):
            return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                         'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                         'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                         }

        def post(self):
            data = json.loads(request.get_data(as_text=True))
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            location = data.get('location')
            isexist = len(mysqldb.query(f"""select * from autosubmit where username='{username}'""")) != 0
            if isexist:
                return {
                           'msg': 'duplicate',
                           'data': '用户已存在'
                       }, {
                           'Access-Control-Allow-Origin': '*',
                           'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                           'Content-Type': 'application/json;charset=utf-8',
                       }
            else:
                a = mysqldb.insert(f"""insert into autosubmit(username, password, email, location)
                values('{username}','{password}','{email}','{location}')""")
                return {
                           'msg': 'success',
                           'data': '已成功提交数据,请等待邮件'
                       }, {
                           'Access-Control-Allow-Origin': '*',
                           'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                           'Content-Type': 'application/json;charset=utf-8',
                       }

    api.add_resource(AutoSubmit, '/autosubmit')

    return app
