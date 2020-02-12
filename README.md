# autosubmit
<img src='https://img.shields.io/badge/author-%E5%B0%8F%E5%B7%9D-ff69b4.svg'><img src='https://img.shields.io/badge/python-3.7-blue.svg'><img src='https://img.shields.io/badge/vue-2-blueviolet.svg'><a href="https://github.com/2239559319/autosubmit/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/2239559319/autosubmit"></a>
--------


> 四川大学健康报告每日自动打卡

- 仓库文件结构
```
|-font       前端文件(Vue源码)
|-main.py    运行文件(在这里进行登录提交发|送邮件)
|-api.py     后端文件(主要是接收来自前端的信息并存储到数据库)

```
- 使用方法
 
  用手机浏览器进入前端页面填报信息[主页][1],在进行填报前会确认定位，请使用正确的定位，邮箱是为了提交报告成功后发送成功消息到邮箱，每天晚上0点后开始自动从后端数据库里面进行提交(PS太懒了不想写密码加密，不过保证不会使用数据库里面的信息，只用做这个程序登录提交报告)
- 默认的提交信息如下，请看好再使用
    - 今日是否在校： 否
    - 所在地点：国内
    - 今日体温范围： 36.6℃-36.9℃
    - 今日是否到过或者经停武汉？：否
    - 今日是否到过或者经停湖北其他地区（除武汉）？： 否
    - 今日是否出现发热、乏力、干咳、呼吸困难等症状？：否
    - 今日是否与武汉市或武汉周边的人员有过较为密集的接触？：否
    - 今日是否与湖北其他地区（除武汉外）的人员有过较为密集的接触？：否
    - 今日是否接触疑似/确诊人群？：否
    - 是否处于观察期？：否
    - 是否有任何与疫情相关的， 值得注意的情况？：否


[1]:https://2239559319.github.io/school/autosubmit/