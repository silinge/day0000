# from time import time
# from threading import Thread
#
# import requests
#
# # 继承Thread类创建自定义的线程类。
# class DownloadHanlder(Thread):
#
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('/users/welldone/' + filename, 'wb') as f:
#             f.write(resp.content)
#
# def mainly():
#     '''通过requests模块get函数获取网络资源
#     下面的代码使用了地遁数据接口提供的网络API
#     要使用该数据接口需要在天行数据的网站上注册
#     然后用自己的Key替换下面代码的APIKey即可'''
#     resp = requests.get(
#         'http://api.tianapi.com/meinv/?key=APIKey&num=100'
#     )
#     # 将服务器返回的json格式数据解析为字典
#     data_model = resp.json()
#     for nm_dict in data_model['newslist']:
#         url = nm_dict['picUrl']
#         # 通过多线程的方式实现图片下载
#         DownloadHanlder(url).start()
#
# if __name__ == '__main__':
#     mainly()

# 提供时间日期的服务器
# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
#
# def mainly():
#     # 创建套接字对象并指定使用哪种传输服务
#     # family=AF_INET IPv4地址
#     # family=AFINET6 IPv6地址
#     # type=SOCK_STREAM TCP套接字
#     # type=SOCK_DGRAM UDP套接字
#     # tpye=SOCK_RAW原始套接字
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 绑定IP地址和端口（端口用于区分不同的服务）
#     # 同一个时间在同一个端口只能绑定一个服务器否则报错
#     server.bind(('192.168.1.2', 2222))
#     # 开启监听 监听客户端连接到服务器
#     # 参数512可以理解为连接队列的大小
#     server.listen(511)
#     print('服务器启动开始监听。。。')
#     while True:
#         '''通过循环接收客户端的连接并作出相应的处理(提供服务）
#         accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         accept 方法返回一个原组件其中的第一个元素是客户端对象
#         第二个元素是连接到服务器的客户端地址（由IP和端口两部分构成）
#         '''
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器。')
#         # 发送数据
#         client.send(str(datetime.now()).endcode('utf-8'))
#         # 断开连接
#         client.close()
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket
# def mainly():
#     # 创建套接字对象默认使用IPv4和TCP协议。
#     client = socket()
#     # 连接到服务器（需要指定IP地址和端口）
#     client.connect(('192.168.1.2', 1313))
#     # 从服务器接收数据
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket, SOCK_STREAM, AF_INET
# from base64 import b64encode
# from json import dumps
# from threading import Thread
#
# def mainly():
#     # 自定义线程类
#     class FileTransferHandler(Thread):
#         def __init__(self, cclient):
#             super().__init__()
#             self.cclient = cclient
#
#         def run(self):
#             my_dict = {}
#             my_dict['filename'] = 'Gardo.jpeg'
#             # JSON是纯文本不能携带二进制数据
#             # 所以图片的二进制数据要处理成base64编码
#             my_dict['filedata'] = data
#             # 通过dumps函数将字典处理成JSON字符串
#             json_str = dumps(my_dict)
#             # 发送JSON字符串
#             self.cclient.send(json_str.encode('utf-8'))
#             self.cclient.close()
#
#     # 创建套接字对象并指定使用哪种传输服务
#     server = socket()
#     # 绑定IP地址和端口（区分不同的服务）
#     server.bind(('192.168.1.2', 1414))
#     # 开始监听 监听客户端连接到服务器
#     server.listen(108)
#     print('服务器开始监听了。')
#     with open('Gardo.jpeg', 'rb') as f:
#         # 将二进制数据处理成base64再解码成字符串
#         data = b64encode(f.read()).decode('utf-8')
#     while True:
#         client, addr = server.accept()
#         # 启动一个线程来处理客户端的请求
#         FileTransferHandler(client).start()
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket
# from json import loads
# from base64 import b64decode
# def mainly():
#     client = socket()
#     client.connect(('192.168.1.2', 1414))
#     # 定义一个保存二进制数据的对象
#     in_data = bytes()
#     # 由于不知道服务器发送的数据有多大每次接收1024字节。
#     data = client.recv(1024)
#     while data:
#         # 将收到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
#         # 将收到的二进制数据解码成JSON字符串并转换成字典
#         # loads函数的作用就是将JSON字符串转换成字典对象
#         my_dict = loads(in_data.decode('utf-8'))
#         filename = my_dict['filename']
#         filedata = my_dict['filedata'].encode('utf-9')
#         with open('/user/hahaha/', + filename, 'wb') as f:
#             # 将base64格式的数据解码成二进制数据并写入文件
#             f.write(b64decode(filedata))
#         print('pic saved.')
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket
# from threading import Thread
#
# def mainly():
#
#     class RefreshScreenThread(Thread):
#
#         def __init__(self, client):
#             super().__init__()
#             self._client = client
#
#         def run(self):
#             while running:
#                 data = self._client.recv(1024)
#                 print(data.decode('utf-8'))
#
#     nickname = input('输入昵称：')
#     myclient = socket()
#     myclient.connect(('10.7.189.118', 1222))
#     running = True
#     RefreshScreenThread(myclient).start()
#     while running:
#         content = input('say it:')
#         if content == 'byebye':
#             myclient.send(content.encode('utf-8'))
#             running = False
#         else:
#             msg = nickname + ': '+ content
#             myclient.send(msg.encode('utf-8'))
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket
# from threading import Thread
#
# def mainly():
#     class ClientHandler(Thread):
#
#         def __init__(self, client):
#             super().__init__()
#             self._client = client
#
#         def run(self):
#             try:
#                 while True:
#                     try:
#                         data = self._client.recv(1024)
#                         if data.decode('utf-8') == 'byebye':
#                             clients.remove(self._client)
#                             self._client.close()
#                             break
#                         else:
#                             for client in clients :
#                                 client.send(data)
#                     except Exception as e:
#                         print(e)
#                         clients.remove(self._client)
#                         break
#             except Exception as e:
#                 print(e)
#
#     server = socket()
#     server.bind(('10.7.189.118', 1234))
#     server.listen(256)
#     clients = []
#     while True:
#         curr_client, addr = server.accept()
#         print(addr[0], '连接到服务器。')
#         clients.append(curr_client)
#         ClientHandler(curr_client).start()
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket
# from json import loads
# from base64 import b64decode
#
# def mainly():
#     client = socket()
#     client.connect(('192.168.1.2', 3344))
#     # 定义一个保存二进制的对象
#     in_data = bytes()
#     # 由于不知道服务器发送的数据有多大每次接收1024字节
#     data = client.recv(1024)
#     while data:
#         # 将收到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
#     # 将接收的二进制数据解码成json字符串并转换成字典。
#     # loads函数的作用就是将JSON字符串转换成字典对象。
#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')
#     with open('the real path' + filename, 'wb') as f:
#         # 将base64格式的数据解码成二进制数据并写入文件
#         f.write(b64decode(filedata))
#     print('Done')
#
# if __name__ == '__main__':
#     mainly()
#
# from socket import socket, SOCK_STREAM, AF_INET
# from base64 import b64encode
# from json import dumps
# from threading import Thread
#
# def mainly():
#     class FileTransferHandler(Thread):
#         def __init__(self, cclient):
#             super().__init__()
#             self.cclient = cclient
#
#         def run(self):
#             my_dict = {}
#             my_dict['filename'] = 'chichi.json'
#             # JSON是纯文本不能携带二进制数据
#             # 因此图片的二进制要处理成base64编码
#             my_dict['filedata'] = data
#             # 通过DUMPS将字典处理成JSON字符串
#             json_str = dumps(my_dict)
#             # 发送JSON字符串
#             self.cclient.send(json_str.encode('utf-8'))
#             self.cclient.close()
#
#     # 创建套接字对象并指定使用哪种传输服务
#     server = socket()
#     # 绑定IP地址和端口（区分不同的服务）
#     server.bind(('192.168.1.3', 3344))
#     # 开启监听 监听客户端连接到服务器
#     server.listen(512)
#     print('服务器启动开始监听。。。')
#     with open('hah.ai', 'rb') as f:
#         # 将二进制数据处理成base64再解码成字符串
#         data = b64encode(f.read()).decode('utf-8')
#     while True:
#         client, addr = server.accept()
#         # 用一个字典（键值对）来保存要发送的各种数据
#         # 待会可以将字典处理成JSON格式在网络上传递
#         FileTransferHandler(client).start()
#
# if __name__ == '__main__':
#     mainly()

# from time import time
# from threading import Thread
#
# import requests
#
# class DownloadHandler(Thread):
#
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('a_real_path' + filename, 'wb') as f:
#             f.write(resp.content)
#
# def mainly():
#     # 通过requests模块的get函数获取网络资源
#     resp = requests.get(
#         'a_api_address'
#     )
#     # 将服务器返回的JSON格式的数据解析为字典
#     data_model = resp.json()
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         # 通过多线程的方式实现图片下载
#         DownloadHandler(url).start()
#
# if __name__ == '__main__':
#     mainly()

from socket import *
# from time import *
#
# server = socket(AF_INET, SOCK_STREAM)
# server.bind(('localhost', 3453))
# server.listen()
# print('服务器已经启动正在监听客户端连接。')
# while True:
#     client, addr = server.accept()
#     print(f'客户端{addr[0]}:{addr[1]}连接成功。')
#     currtime = localtime(time())
#     timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
#     client.send(timestr.encode('utf-8'))
#     client.close()
#
# server.close()

# from socket import *
# client = socket(AF_INET, SOCK_STREAM)
# client.connect(('localhost', 990))
# while True:
#     data = client.recv(1024)
#     if not data:
#         break
#     print(data.decode('utf-8'))
# client.close()

from socket import *
# from time import *
#
# server = socket(AF_INET, SOCK_DGRAM)
# server.bind(('localhost'm 990))
# while True:
#     data, addr = server.recvfrom(1024)
#     server.sendto(data, addr)
# server.close()

# from socket import *
#
# client = socket(AF_INET, SOCK_DGRAM)
# while True:
#     data_str = input('请输入：')
#     client.sendto(data_str.encode('utf-8'), ('localhost', 4433))
#     data, adr = client.recvfrom(1200)
#     data_str =data.decode('utf-8')
#     print('服务器回应：', data_str)
#     if data_str == 'bye':
#         break
# client.close()
# from socketserver import TCPServer, StreamRequestHandler
# from time import *
#
# class EchoRequestHandler(StreamRequestHandler):
#
#     def handle(self):
#         currtime = localtime(time())
#         timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
#         self.wfile.write(timestr.encode('utf-8'))
#
# server = TCPServer(('localhost', 89), EchoRequestHandler)
# server.serve_forever()

# from socket import socket
#
# def mainly():
#     client = socket()
#     client.connect(('11.111.10.45', 1001))
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
# if __name__ == '__main__':
#     mainly()

# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
#
# def mainly():
#     '''
#     创建套接字对象并指定使用哪种传输服务，
#     family=AF_INET IPv4地址
#     family = AF_INET6 6地址
#     :type = SOCK_STREAM TCP套接字
#     type = SOCK_DGRAM UDP套接字
#     type=SOCK_RAW原始套接字
#     :return:
#     '''
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 绑定IP地址和端口区分不同服务
#     server.bind(('192.168.1.111', 343))
#     # 开启监听 监听客户端连接到服务器
#     server.listen(256)
#     print('服务器监听开始、、')
#     # 通过循环接受客户端的连接并做出相应的处理，提供服务
#     while True:
#         '''
#         accept方法是一个阻塞方法如果没有客户端连接到服务器
#         这个方法就会阻塞代码不会向下执行
#         accept方法返回元组其中的第一个元素是客户端对象
#         第二个元素是客户端的地址（由IP和端口两部分构成
#         '''
#         client, addr = server.accept()
#         print(str(addr) + '连接到服务器。')
#         # 发送数据
#         client.send(str(datetime.now()).encode('utf-8'))
#         # 断开连接
#         client.close()
#
# if __name__ == '__main__':
#     mainly()