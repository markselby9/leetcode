__author__ = 'fengchaoyi'
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders

import os, socket, urllib2

#server['name'], server['user'], server['passwd']
def send_mail(server, fro, to, subject, text, timeval, files=[]):
    assert type(server) == dict
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['Subject'] = subject
    msg['To'] = COMMASPACE.join(to) #COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True)
    # msg['Date'] = formatdate(timeval)
    msg.attach(MIMEText(text))

    for file in files:
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
        part.set_payload(open(file, 'rb'.read()))
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    import smtplib
    smtp = smtplib.SMTP()
    smtp.connect(server['name'],"25")
    smtp.login(server['user'], server['passwd'])
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()

server={}
server['name']="mail.fudan.edu.cn"
sender = '10300200021@fudan.edu.cn' #enter sender here
server['user']=sender
server['passwd']='enter password here' #enter password here
to=["14212010002"] #enter receiver list here ( in a list)
subject="hello"
text="hello i'm from the past"

send_mail(server,sender,to,subject,text)