import smtplib
from email.mime.text import MIMEText

mailto_list=["3081959858@qq.com"]
mail_host="smtp.163.com"
mail_user="julianforthehorde@163.com"
mail_pass="ISVGGMSZTFLWSRYG"

msg=MIMEText('这是我用程序发送的一封电子邮件。')
msg['Subject']="用程序发送的电子邮件"
msg['From'] =mail_user
msg['To'] = ";".join(mailto_list)

try:
    s=smtplib.SMTP_SSL(mail_host,465)
    #s.connect(mail-host)
    s.login(mail_user,mail_pass)
    s.sendmail(mail_user,mailto_list,msg.as_string())
    s.close()
    print("发送成功")
except Exception as e:
    print(str(e))
    print("发送失败")
