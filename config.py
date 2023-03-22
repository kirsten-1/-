import os
from datetime import timedelta

DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liu246531zaishi@127.0.0.1:3306/situational?charset=utf8'
SQLALCHEMY_POOL_SIZE = 100

#邮箱设定
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'yoursender@qq.com'
MAIL_PASSWORD = 'yourpassword'

#登录session设置
SECRET_KEY=os.urandom(24)
PERMANENT_SESSION_LIFETIME=timedelta(hours=5)


# Web日志路径
apache_log = '/var/log/apache2/access.log'

#爆破次数设定
burst_num=30

# SQL 注入攻击匹配规则
sqlrule = "'|--|update|extractvalue|union|select|substr|information_schema".split(
    '|')
# XSS 跨站攻击匹配规则
xssrule = "script|iframe|javascript|onerror|onmouseover|/>".split('|')
# 木马后门 匹配规则
backrule = "eval|assert|system|shell_exec|passthru".split('|')


#type设置
attackType = {
    100: '无威胁',
    101: 'XSS跨站',
    102: 'SQL注入',
    103: '目录扫描',
    104: 'DoS攻击',
    105: '暴力破解',
    106: '木马后门',
    107: 'SSH爆破'
}

# 要监视是否正常运行的程序列表
process = ['apache', 'mysqld', 'vsftpd', 'sshd']


local_ip = '101.42.172.145'
local_adapter = 'any'  #网卡名字可不指定
local_coord = [-118.24368, 34.05223]
local_city = 'Tianjin'


# 流量统计单位
stream_unit = 1024               # KB
# stream_unit = 1024 * 1024        # MB
# stream_unit = 1024 * 1024 * 1024 # GB
