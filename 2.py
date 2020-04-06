import os, sys, string
import poplib
from email import parser
from email.header import decode_header

server= poplib.POP3_SSL("pop.163.com","995")
#server= poplib.POP3("pop3.163.com")
server.user("julianforthehorde@163.com")
server.pass_("ISVGGMSZTFLWSRYG")

resp, mails, octets = server.list()
print("total number of emails: %d" % len(mails))

for index in range(len(mails)):
    resp, lines, octets = server.retr(index+1)
    msg_content = b"\r\n".join(lines).decode('utf-8')
    msg = parser.Parser().parsestr(msg_content)
    emailbase = {}

    for line in msg.items():
        header = line[0]
        if header in ['From', 'Subject','Date']:
            item= decode_header(line[1])[-1]
            code = item[1] if item[1]!= None else 'ascii'
            if isinstance(item[0], bytes): value = str(item[0],code)
            else: value = item[0]
            emailbase[header] = value
    print("-------------%d/%d----------------"%(index+1,len(mails)))
    print("发信信箱："+emailbase["From"])
    print("信件主题："+emailbase ['Subject'])
    print("发信时间："+emailbase['Date'])
server.quit()
