#encoding:utf-8

import MySQLdb
import requests
import json
import smtplib
import time
from datetime import datetime, timezone, timedelta
from email.message import EmailMessage

class DBsystem(object):
    def __init__(self):
        self.db = MySQLdb.connect(host='2239559319.mysql.pythonanywhere-services.com',
                                  user='2239559319',
                                  password='',      #这里密码私密
                                  db='2239559319$default',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def query(self):
        self.cursor.execute('''select username, password, email, location from autosubmit''')
        print(self.cursor.fetchall())

class AutoSubmit(object):

    def __init__(self, username, password):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }
        self.s = requests.session()
        self.username = username
        self.password = password

    def login(self):
        '''
            :param username: 学号
            :param password: 密码
            :return: 登录结果
            '''
        url = 'https://wfw.scu.edu.cn/a_scu/api/sso/check'
        data = {
            'username': self.username,
            'password': self.password,
            'redirect': 'https://wfw.scu.edu.cn/site/polymerization/polymerizationInfor',
        }
        try:
            r = self.s.post(url=url, data=data, headers=self.headers)
            if r.json()['m'] == '操作成功':
                return '成功登录'
            else:
                return '登录失败请稍后再试'
        except Exception:
            return '登录失败请稍后再试'

    def submit(self, location_str):

        location_dic = json.loads(location_str)

        url = 'https://wfw.scu.edu.cn/ncov/wap/default/save'
        data = {
            'tw': '3',
            'sfcxtz': '0',
            'sfjcbh': '0',
            'sfcxzysx': '0',
            'qksm': '',
            'sfyyjc': '0',
            'jcjgqr': '0',
            'remark': '',
            'address': location_dic['formattedAddress'],
            'geo_api_info': location_str,
            'area': f"{location_dic['addressComponent']['province']} {location_dic['addressComponent']['city']} {location_dic['addressComponent']['district']}",
            'province': location_dic['addressComponent']['province'],
            'city': location_dic['addressComponent']['city'],
            'sfzx': '0',
            'sfjcwhry': '0',
            'sfjchbry': '0',
            'sfcyglq': '0',
            'gllx': '',
            'glksrq': '',
            'jcbhlx': '',
            'jcbhrq': '',
            'ismoved': '0',
            'bztcyy': '',
            'sftjhb': '0',
            'sftjwh': '0',
            'jcjg': '',
        }
        try:
            r = self.s.post(url=url, data=data, headers=self.headers)
            if r.json['m'] == '操作成功':
                return '提交成功'
        except Exception:
            print('提交失败')

def sendMail(content, receiver):
    msg = EmailMessage()
    msg.set_content(content)

    sender = 'w773127754@163.com'
    password = ''       #这里密码私密

    msg['Subject'] = '健康报告发送'
    msg['From'] = sender
    msg['To'] = receiver
    try:
        s = smtplib.SMTP_SSL('smtp.163.com', 465)
        s.login(sender, password)
        s.send_message(msg)
        s.quit()
        print("发送成功")
    except Exception:
        print("发送失败")

def interval(f):
    utc_time = datetime.now()
    cst_time = utc_time.astimezone(timezone(timedelta(hours=8)))
    preday = cst_time.day

    while True:

        nowtime = datetime.now().astimezone(timezone(timedelta(hours=8)))

        if nowtime.day != preday and nowtime.hour == 0:
            preday = nowtime.day
            f()
        time.sleep(600)

def start():
    db = DBsystem()
    for e in db.query():
        cur_user = AutoSubmit(username=e[0], password=e[1])
        cur_user.login()
        result = cur_user.submit(e[3])
        if result == '提交成功':
            sendMail('每日健康报告已上传', e[2])
        else:
            sendMail('健康报告上传失败请手动去公众号填写', e[2])
        time.sleep(10)

if __name__ == '__main__':
    interval(start)