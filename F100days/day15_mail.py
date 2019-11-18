# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText
#
# def mainly():
#     # 自行修改邮件发送参数
#     sender = 'example@gmail.com'
#     receivers = ['examples01@gmail.com', 'examples02@gmail.com']
#     message = MIMEText('用Python发送邮件的示例代码。', 'plain', 'utf-8')
#     message['From'] = Header('武则天', 'utf-8')
#     message['To'] = Header('李白', 'utf-8')
#     message['Subject'] = Header('示例代码实验邮件', 'utf-8')
#     smtper = SMTP('smtp.126.com')
#     # 自己修改登录口令
#     smtper.login(sender, 'secretpass')
#     smtper.sendmail(sender, receivers, message, message.as_string())
#     print('Finished.')
#
# if __name__ == '__main__':
#     mainly()

# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
#
# import urllib
#
# def mainly():
#     # 创建一个带附件的邮件消息对象
#     message = MIMEMultipart()
#     # 创建文本内容
#     text_content = MIMEText('附件中有年度影像请查收。', 'plain', 'utf-8')
#     message['Subject'] = Header('Picture', 'utf-8')
#     # 将文本内容添加到邮件消息对象中
#     message.attach(text_content)
#     # 读取文件并将文件作为附件添加到邮件消息对象中
#     with open('good_path/pic.txt', 'rb') as f:
#         txt = MIMEText(f.read(), 'base64', 'utf-8')
#         txt['Content-Type'] = 'text/plain'
#         txt['Content-Disposition'] = 'attachment; filename=pic.txt'
#         message.attach(txt)
#         # 读取文件将文件作为附件添加到邮件消息对象中
#     with open('good_path/pic_anni.zip', 'rb') as f:
#         pic = MIMEText(f.read(), 'base64', 'utf-8')
#         pic['Content-Type'] = 'applicatiom/vnd.go-zip'
#         pic['Content-Disposition'] = 'attachment; filename=anni-pic.zip'
#         message.attach(pic)
#
#     # 创建SMTP对象
#     smtper = SMTP('smtp.126.com')
#     # 开启安全连接
#     # smtper.starttls()
#     sender = 'alphabet@go.com'
#     receivers = ['window@yahoo.haha.com']
#     # 登录到SMTP服务器
#     # 此处不是使用密码而是邮件客户端授权码进行登录
#     # 对此有疑问的读者可以联系自己使用的邮件服务器客服
#     smtper.login(sender, 'secretpass')
#     # 发送邮件
#     smtper.sendmail(sender, receivers, message.as_string())
#     # 与邮件服务器断开连接
#     smtper.quit()
#     print('发送完成。')
#
# if __name__ == '__main__':
#     mainly()

# 短信平台
# import urllib.parse
# import  http.client
# import json
#
# def mainly():
#     host = '250.ihuyi.com'
#     sms_send_uri = '/webservice/sms.php?method=Submit'
#     # 下面的参数需要填入自己注册的账号和对应的密码
#     params = urllib.parse.urlencode({'account':'你自己的账号', 'password':'你的密码（我怎么知道你的密码）','content':
#                                      '你的验证码：232359、（装的真一点）、','mobile':'手机号', 'format':'json'})
#     print(params)
#     headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'text/plain'}
#     conn = http.client.HTTPConnection(host, port=80, timeout=30)
#     response = conn.getresponse()
#     response_str = response.read()
#     jsonstr = response_str.decode('utf-8')
#     print(json.loads(jsonstr))
#     conn.close()
#
# if __name__ == '__main__':
#     mainly()