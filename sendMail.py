# !/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import emailAccount

sender = 'presouce@163.com'
receiver = 'presouce@163.com'
smtpserver = 'smtp.163.com'

def sendMail(sub, context):
    msg = MIMEText(context, _subtype='plain',_charset='gb2312')  # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(sub, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(emailAccount.username, emailAccount.password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
