#part 1
#json
# import json
# from urllib.request import  urlopen
#
# def getCountry(ipAddress):
#     # response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
#     response = urlopen("https://ipstack.com/json/" + ipAddress).read().decode("utf-8")
#     responseJson = json.loads(response)
#     return responseJson.get("country_cod")
# print(getCountry("50.78.253.58"))
#这个网站无用了 跳转的链接需要注册获得api 所以就跳过吧。
#——————————————————————————
# part2
# import json
# jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
#              '"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
# jsonObj = json.loads(jsonString)
# print(jsonObj.get("arrayOfNums"))
# print(jsonObj.get("arrayOfNums")[1])
# print(jsonObj.get("arrayOfNums")[1].get("number")+
#       jsonObj.get("arrayOfNums")[2].get("number"))
# print(jsonObj.get("arrayOfFruits")[2].get("fruit"))
#范例 处理json的字段吧
#——————————————————————————
#part 2
#获取维基百科页面编辑历史的IP记录
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import re
# import random
#
# random.seed(datetime.datetime.now())
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org" + articleUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                                                            href=re.compile("^(/wiki/)((?!:).)*$"))
#
# def getHistoryIPs(pageUrl):
#     #编辑历史页面URL链接格式
#     #http://en.wikipedia.org/w/index.php?title=Tittle_in_URL&action=history
#     pageUrl = pageUrl.replace("/wiki/", "")
#     historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
#     print("history url is : " + historyUrl)
#     html = urlopen(historyUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     #找出class属性是“mw-anouserlink"链接
#     #他们用IP地址代替用户名
#     ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
#     addressList = set()
#     for ipAddress in ipAddresses:
#         addressList.add(ipAddress.get_text())
#     return addressList
#
# links =getLinks("/wiki/Python_(programming_language)")
#
# while(len(links)>0):
#     for link in links:
#         print("________________")
#         historyIPs = getHistoryIPs(link.attrs["href"])
#         for historyIP in historyIPs:
#             print(historyIP)
#
#     newLink = links[random.randint(0, len(links)-1)].attrs["href"]
#     links = getLinks(newLink)
#这一部分是能正常运行运行的了，以后命名变量尽量不要用近似的名称 放错了地方很难发现

#——————————————————————————
# part3
# from urllib.request import urlretrieve
# from urllib.request import  urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, features='lxml')
# imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
# urlretrieve(imageLocation, "logo.jpg")
#保存这个网页上面的一张图片

#——————————————————————————
# part 4
# import os
# # from urllib.request import urlretrieve
# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# #
# # downloadDirectory = "download"
# # baseUrl = "http://pythonscraping.com"
# #
# # def getAbsoluteURL(baseUrl, source):
# #     if source.startswith("http://www."):
# #         url = "http://"+source[11:]
# #     elif source.startswith("http://"):
# #         url = source
# #     elif source.startswith("www."):
# #         url = source[4:]
# #         url = "http://" + source
# #     else:
# #         url = baseUrl+"/"+source
# #     if baseUrl not in url:
# #         return None
# #     return url
# #
# # def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
# #     path = absoluteUrl.replace("www.", "")
# #     path = path.replace(baseUrl, "")
# #     path = downloadDirectory + path
# #     directory = os.path.dirname(path)
# #
# #     if not os.path.exists(directory):
# #         os.makedirs(directory)
# #
# #     return path
# #
# # html = urlopen("http://www.pythonscraping.com")
# # bsObj = BeautifulSoup(html, features='lxml')
# # downloadList = bsObj.findAll(src = True)
# #
# # for download in downloadList:
# #     fileUrl = getAbsoluteURL(baseUrl, download["src"])
# #     if fileUrl is not None:
# #         print(fileUrl)
# # urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
#下载网页上所以带有src属性的文件 注意建立了分支之后 在gitbash 切换不同分支 文件的显示是不同的 wired
#——————————————————————————
# part 5

#创建和修改csv文件
# import csv
#
# csvFile = open(r"E:\day0000\gitignorefolder\Newcsv.csv", 'w+')#这里要使用具体的文件名 而不是文件夹路径 不然不知道打开和写入的目标是什么
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(("i", "i plus 2" , "i*2"))
#     for i in range(10):
#         writer.writerow((i, i+2, i*2))
# finally:
#     csvFile.close()

#——————————————————————————
# part 6
#采集wiki 百科的网页里面的表格存储到csv文件
# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html, features='lxml')
# table = bsObj.findAll("table", {"class":"wikitable"})[0]
# rows = table.findAll("tr")
#
# csvFile = open(r"E:\day0000\gitignorefolder\editors.csv", "w+", newline='', encoding='utf-8')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#             writer.writerow(csvRow)
# finally:
#     csvFile.close()

#——————————————————————————
# 插入一部分mysql的用法
# 1 CREATE DATABASE put a name; 结尾要使用； 非常重要
# 2 USE put a name; 使用这个数据库 put a name
# 3 CREATE TABLE put 2nd name; 在put a name 库之中建立一张表 叫做put 2nd name 这是不行的，还要跟上定义表头项目
# 4CREATE TABLE put 2nd name (id BIGINT(7) NOT NULL AUTO_INCREMENT, title VARCHAR(200),
# content VARCHAR(10000), created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id));
# 这样才能建立一张表 不报错
# 5 INSERT INTO pages (title, content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long."); 结尾的分号 很重要啊
# 6 SELECT * FROM pages WHERE id = 2; 在pages 中找到并显示id 2的内容 *表示全部内容
# 7 SELECT * FROM pages WHERE title LIKE "%test%"; 找到title中包含了test的所有条目
# 8 SELECT id, title FROM pages WHERE content LIKE "%page content%"; 找到内容content中包含page content的 id title 这次不用显示所有。
# 9 DELETE FROM pages WHERE id = 1; 删除一个set 可以先使用SELECT查看一下 避免删除错误 不能忘了WHERE 你可能删除了所有内容
# 10 UPDATE pages SET title="A new title", content="Some new content" WHERE id =2; 更改id = 2 的内容吧。
#——————————————————————————
# part7
#建立一个链接mysql
# import pymysql

# conn = pymysql.connect(host = '127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='123456', db='mysql') 用的windows的话，删除 unix_socket='/tmp/mysql.sock'
# conn = pymysql.connect(host = '127.0.0.1', user='root', passwd='123456', db='mysql')
# cur = conn.cursor()
# cur.execute("USE scraping")
#
# cur.execute("SELECT * FROM pages WHERE id=2")
# print(cur.fetchone())
# cur.close()
# conn.close()
#真的可以连上
#——————————————————————————
# ALTER
# DATABASE
# scraping
# CHARACTER
# SET = utf8mb4
# COLLATE = utf8mb4_unicode_ci;
#
# USE scraping;
#
# ALTER
# TABLE
# pages
# CONVERT
# TO
# CHARACTER
# SET
# utf8mb4
# COLLATE
# utf8mb4_unicode_ci;
#
# ALTER
# TABLE
# pages
# CHANGE
# title
# title
# VARCHAR(200)
# CHARACTER
# SET
# utf8mb4
# COLLATE
# utf8mb4_unicode_ci;
#
# ALTER TABLE pages CHANGE content content VARCHAR(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 用于转换mysql格式为Unicode 以避免使用某些文字出现乱码
#——————————————————————————
# part8
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
# import pymysql
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8')
# #windows 系统下不用写 unix_socket的内容 linux 需要写 passwd 改成你的密码
# cur = conn.cursor()
# cur.execute("USE scraping")
# random.seed(datetime.datetime.now())
#
# def store(title, content):
#     cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content))
#     cur.connection.commit()
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     title = bsObj.find("h1").get_text()
#     content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
#     store(title,content)
#     return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
# links = getLinks("/wiki/Kevin_Bacon")
# try:
#     while len(links) >0:
#         newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#         print(newArticle)
#         links = getLinks(newArticle)
# finally:
#     cur.close()
#     conn.close()

#——————————————————————————
# part9
# CREATE TABLE wikipedia.pages (id INT NOT NULL AUTO_INCREMENT, url VARCHAR(255) NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
# 数据库命令 创建新的数据库 wikipedia 并在其下创建表pages 这些名称都不用加引号 否则要报错
# CREATE TABLE wikipedia.links (id INT NOT NULL AUTO_INCREMENT, fromPagedId INT NULL, toPageId INT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
# 创建一张新表links
# from bs4 import BeautifulSoup
# import re
# from urllib.request import urlopen
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute("USE wikipedia")
#
# def insertPageIfNotExists(url):
#     cur.execute("SELECT * FROM pages WHERE url=%s", (url))
#     if cur.rowcount ==0:
#         cur.execute("INSERT INTO PAGES (url) VALUES(%s)", (url))
#         conn.commit()
#         return cur.lastrowid
#     else:
#         return cur.fetchone()[0]
#
# def insertLink(fromPageId, toPageId):
#     cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
#     if cur.rowcount == 0:
#         cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES(%s, %s)", (int(fromPageId), int(toPageId)))
#         conn.commit()
#
# pages = set()
#
# def getLinks(pageUrl, recursionLevel):
#     global pages
#     if recursionLevel > 4:
#         return;
#     pageId = insertPageIfNotExists(pageUrl)
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     for link in bsObj.findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
#         insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
#         if link.attrs['href'] not in pages:
#             newPage = link.attrs['href']
#             pages.add(newPage)
#             getLinks(newPage, recursionLevel+1)
# getLinks("/wiki/Kevin_Bacon", 0)
# cur.close()
# conn.close()
# 这段程序可能需要运行几天 wiki的服务器最终会拒绝访问，测试了几分钟已经存了近3000个链接
# import smtplib
# from email.mime.text import MIMEText
# msg = MIMEText("The body of the email is here")
# msg["Subject"] = "An Email Alert"
# msg["From"] = "address@emailwhosend.com"
# msg["To"] = "address@emailwhoreceive.com"
#
# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()
# 当你的电脑有一个正常运行的SMTP客户端 再把localhost改成远程服务器地址就可以发信了

# import smtplib
# from email.mime.text import MIMEText
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import time
# def sendMail(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "fromemailaddress"
#     msg['To'] = "toemailaddress"
#
#     s = smtplib.SMTP('localhost')
#     s.send_message(msg)
#     s.quit()
#
# bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"), features='lxml')
# while(bsObj.find("a", {"id":"answer"}).attrs['tittle'] == "NO"):
#     print("It is not Christmas yet.")
#     time.sleep(3600)
# bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
# sendMail("It is Christmas!", "According to http://itischristmas.com, it is Christmas!")
# 每隔一个小时检查一个网站是不是圣诞节到了，如果到了 给你发一封邮件告诉你
#——————————————————————————
# part10
# from urllib.request import urlopen
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# print(textPage.read())
# 直接读取文本
# from urllib.request import  urlopen
#
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textPage.read(), 'utf-8'))
# 俄文版本要指定编码 才能更好的显示出文本
#——————————————————————————
# part11
# from urllib.request import urlopen
# from io import StringIO
# import csv
#
# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
#
# # for row in csvReader:
# #     print(row)
#
# # 将对象嵌入的思路
# for row in csvReader:
#     print("The album \""+row[0]+"\"was released in " + str(row[1]))
# csvReader 和 csvDictReader是不同的 读取第一行的表头
# from urllib.request import urlopen
# from io import StringIO
# import csv
#
# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# dictReader = csv.DictReader(dataFile)
# # print(dictReader.fieldnames)
# for row in dictReader:
#     print(row)

# 读取pdf文件
# from urllib.request import urlopen
# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from io import open
#
# def readPDF(pdfFile):
#     rsrcmgr = PDFResourceManager()
#     restr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, restr, laparams=laparams)
#
#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()
#
#     content = restr.getvalue()
#     restr.close()
#     return content
#
# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)
# pdfFile.close()

# 处理doc 文件

# from zipfile import ZipFile
# from urllib.request import urlopen
# from io import BytesIO
#
# wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# wordFile = BytesIO(wordFile)
# document = ZipFile(wordFile)
# xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))
# 直接读取xml 不够理想，没法阅读 再试试处理xml 标签的内容抽出正文
# from zipfile import ZipFile
# from urllib.request import urlopen
# from io import BytesIO
# from bs4 import BeautifulSoup
#
# wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# wordFile = BytesIO(wordFile)
# document = ZipFile(wordFile)
# xml_content = document.read('word/document.xml')
#
# wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')
# textString = wordObj.findAll("w:t")
# for textElem in textString:
#     print(textElem.text)

# 处理不同文本样式的标签
# from zipfile import ZipFile
# from urllib.request import urlopen
# from io import BytesIO
# from bs4 import BeautifulSoup
#
# wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# wordFile = BytesIO(wordFile)
# document = ZipFile(wordFile)
# xml_content = document.read("word/document.xml")
#
# wordObj = BeautifulSoup(xml_content.decode("utf-8"), 'lxml')
# textStrings = wordObj.findAll('w:t')
# for textElem in textStrings:
#     closeTag = ""
#     try:
#         style = textElem.parent.previousSibling.find("w:pstyle")
#         if style is not None and style["w:val"] == "Title":
#             print("<h1>")
#             closeTag = "</h1>"
#     except AttributeError:
#         pass
#     print(textElem.text)
#     print(closeTag)

#——————————————————————————
# part12 new chapter  dirty data to clean
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# def ngrams(inputs, n):
#     inputs = inputs.split(" ")
#     output = []
#     for i in range(len(inputs)-n+1):
#         output.append(inputs[i:i+n])
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, 'lxml')
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content, 2)
# print(ngrams)
# print("2-grams count is :"+str(len(ngrams)))

# 第二版 去掉一些转义符 还有Unicode

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# def ngrams(content, n):
#     content = re.sub('\n+', " ", content)
#     content = re.sub(' +', " ", content)
#     content = bytes(content, "UTF-8")
#     content = content.decode("ascii", "ignore")
#     print(content)
#     content = content.split(' ')
#     output = []
#     for i in range(len(content)-n+1):
#         output.append(content[i:i+n])
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, 'lxml')
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content, 2)
# print(ngrams)
# print("2-grams count is :"+str(len(ngrams)))

# 第三版 单独建立一个清洗用的函数
# from collections import OrderedDict
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import string
#
# def cleanInput(inputs):
#     inputs = re.sub("\n+", " ", inputs)
#     inputs = re.sub("\[[0-9]*\]", "", inputs)
#     inputs = re.sub(" +", " ", inputs)
#     inputs = bytes(inputs, "utf-8")
#     inputs = inputs.decode("ascii", "ignore")
#     cleanInput = []
#     inputs = inputs.split(" ")
#     for item in inputs:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == "a" or item.lower() == "i"):
#             cleanInput.append(item)
#     return cleanInput
#
# def ngrams(inputs, n):
#     inputs = cleanInput(inputs)
#     output = []
#     for i in range(len(inputs) - n+1):
#         output.append(inputs[i:i+n])
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, "lxml")
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content, 2)
# ngrams = OrderedDict(sorted(ngrams, key=lambda t:t[1], reverse=True))
# print(ngrams)

# import string
# print(string.punctuation) 获取了python中所有的标点符号 英文格式 处理中文的 还得手动试试 strip(string.punctuation) 就是扔掉了单词前后端的标点了。
# 第四版 对数据去重
# from collections import OrderedDict
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import string
#
# def cleanInput(inputs):
#     inputs = re.sub('\n+', " ", inputs)
#     inputs = re.sub('\[[0-9]*\]', "", inputs)
#     inputs = re.sub(' +', " ", inputs)
#     inputs = bytes(inputs, "UTF-8")
#     inputs = inputs.decode("ascii", "ignore")
#     cleanInput = []
#     inputs = inputs.split(' ')
#     for item in inputs:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
#             cleanInput.append(item)
#     return cleanInput
#
# def ngrams(inputs, n):
#     inputs = cleanInput(inputs)
#     output = []
#     for i in range(len(inputs)- n+1):
#         output.append(inputs[i:i+n])
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, "lxml")
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content, 2)
# ngrams = dict(ngrams)
# print(type(ngrams))
# ngrams = OrderedDict(sorted(ngrams, key=lambda t:t[1], reverse=True))
# ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t:t[1], reverse=True))
#
# print(ngrams)
# #——————————————————————————
# # part 13
# from urllib.request import urlopen
# from random import randint
#
# def wordListSum(wordList):
#     sum = 0
#     for word, value in wordList.items():
#         sum += value
#     return sum
# def retrieveRandomWord(wordList):
#
#     randIndex = randint(1, wordListSum(wordList))
#     for word, value in wordList.items():
#         randIndex -= value
#         if randIndex <=0:
#             return word
#
# def buildDict(text):
#     text = text.replace("\n", " ");
#     text = text.replace("\"", " ");
#     punctuation = [',', ',', ';', ':']
#     for symbol in punctuation:
#         text = text.replace(symbol, " "+symbol+" ");
#     words = text.split(" ")
#     words = [word for word in words if word != ""]
#     wordDict = {}
#     for i in range(1, len(words)):
#         if words[i-1] not in wordDict:
#             wordDict[words[i-1]] = {}
#         if words[i] not in wordDict[words[i-1]]:
#             wordDict[words[i-1]][words[i]] = 0
#         wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] +1
#
#     return wordDict
#
# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8")
# wordDict = buildDict(text)
#
# length = 100
# chain = ""
# currentWord = "I"
# for i in range(0, length):
#     chain += currentWord+" "
#     currentWord = retrieveRandomWord(wordDict[currentWord])
#
# print(chain)
# #——————————————————————————
# # part 14
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pymysql
#
# conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd='123456', db = 'mysql', charset = 'utf8')
#
# cur = conn.cursor()
# cur.execute("USE wikipedia")
#
# class SolutionFound(RuntimeError):
#     def __init__(self, message):
#         self.message = message
#
# def getLinks(fromPageId):
#     cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
#     if cur.rowcount == 0:
#         return None
#     else:
#         return [x[0] for x in cur.fetchall()]
#
# def constructDict(currentPageId):
#     links = getLinks(currentPageId)
#     if links:
#         return dict(zip(links, [{}]*len(links)))
#     return {}
#
# def searchDepth(targetPageId, currentPageId, linkTree, depth):
#     if depth == 0:
#         return linkTree
#     if not linkTree:
#         linkTree = constructDict(currentPageId)
#         if not linkTree:
#             return {}
#     if targetPageId in linkTree.keys():
#         print("TARGET"+str(targetPageId)+"FOUND!")
#         raise SolutionFound("PAGE:"+str(currentPageId))
#
#     for branchKey, branchValue in linkTree.items():
#         try:
#             linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
#         except SolutionFound as e:
#             print(e.message)
#             raise SolutionFound("PAGE:"+str(currentPageId))
#         return linkTree
#
# try:
#     searchDepth(134951, 1, {}, 4)
#     print("No solution found")
# except SolutionFound as e:
#     print(e.message)

# pick up again
#day 0007
# from nltk import word_tokenize
# from nltk import Text
# tokens = word_tokenize("Here is some not very interesting text")
# text = Text(tokens)
# print(text)

# from nltk.book import *
# print(len(text3)/len(words))
# from nltk import FreqDist
# fdist = FreqDist(text6)
# print(fdist.most_common(10))
# print(fdist["Grail"])


# from nltk.book import *
# from nltk import bigrams
# bigrams = bigrams(text6)
# bigramsDist = FreqDist(bigrams)
# print(bigramsDist[("Sir", "Robin")])

# from nltk.book import *
# # from nltk import ngrams
# # fourgrams = ngrams(text6, 4)
# # for fourgram in fourgrams:
# #     if fourgram[0] == "coconut":
# #         print(fourgram)
# make them link again

# from nltk.book import *
# from nltk import word_tokenize
# text = word_tokenize("Strange women lying in ponds distributing swords is no basis for a system of government. "
                     # "Supreme executive derives from a mandate from the masses, net from some farcical aquatic ceremony.")
# textone = word_tokenize("the dust was thick so he had to dust")
# from nltk import pos_tag
# print(pos_tag(textone))

# from nltk import word_tokenize, sent_tokenize, pos_tag
# sentences = sent_tokenize("Google is one of the best companies in the world. I constantly google myself to see what I'm up to.")
# nouns = ['NN', 'NNS', 'NNP', 'NNPS']
#
# for sentence in sentences:
#     if "google" in sentence.lower():
#         taggedWords = pos_tag(word_tokenize(sentence))
#         for word in taggedWords:
#                 if word[0].lower() == "google" and word[1] in nouns:
#                     print(sentence)

#选出Google作为名词使用的那个句子 打印出来
# part 15 -------------------------------------------
# import requests
# params = {'firstname': 'Williams', 'lastname': 'Xu'}
# r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params) #书中给的链接错误 缺少pages
# print(r.text)
#向网页提交两个参数

# import requests
# params = {'email_addr':'DonotRunThis@gmail.com'}
# r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)
# print(r.text)
# 这是加入oreilly的邮箱列表 如果没有确认使用正常的邮箱 不用运行提交。

# import requests
#
# files = {'uploadFile':open("/e/f/g/milab.bmp", 'rb')}
# r = requests.post("http://pythonscraping.com/pages/processing2.php", files = files)
#
# print(r.text)
# 上传一个文件

# import requests
#
# params = {'username': "July", 'password':"password"}
# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print("Cookie is set to: ")
# print(r.cookies.get_dict())
# print("---------------")
# print("Going to profile page...")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)
# print(r.text)
# 获取到cookie

# import requests
#
# session = requests.Session()
# params = {'username':'username', 'password':'password'}
# s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print("Cookie is set to: ")
# print(s.cookies.get_dict())
# print("---------------")
# print("Going to profile page...")
# s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
# print(s.text)

#http 认证方式
# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth("Ben", 'password')
# r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
# print(r.text)

#part16_______________
# day8
# 采集javascript
# from selenium import webdriver
# # import time
# # driver = webdriver.PhantomJS(executable_path=r"D:\phantomjs-2.1.1-windows\bin")
# # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# # time.sleep(4)
# # print(driver.find_element_by_id('content').text)
# # driver.close()
#很不幸 selenium 不再支持phantomjs了 所以教材要更新了，只能去使用无头版的chrome或者Firefox 那又是另外的代码了。
# import requests
#
# files = {'uploadFile': open('../files/Python-logo.png', 'rb')}
# r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
#
# print(r.text)

# import requests
#
# params = {'username':'Ryan', 'password':'password'}
#
# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print("Cookie is set to: ")
# print(r.cookies.get_dict())
# print("__________________")
# print("Going to profile page...")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)
# print(r.text)

# import requests
#
# session = requests.Session()
#
# params = {'username':'whatname', 'password':'guesswhat'}
#
# s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
# print("Cookie is set to:")
# print(s.cookies.get_dict())
# print("-------------------")
# print("Going to profile page...")
# s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
# print(s.text)
# part17 -----------------------------------
# image operate

# from PIL import Image, ImageFilter
#
# fly = Image.open("55.jpg")
# blurryfly = fly.filter(ImageFilter.GaussianBlur)
# blurryfly.save("55_bulrred.jpg")
# blurryfly.show()

# from PIL import Image, ImageFilter
# flynew = Image.open("‪E:/backup0219/SavedPictures/0601.jpg") 复制的路径报错的 改了
# flynew = Image.open("E:/backup0219/SavedPictures/0601.jpg") 手动输入左斜杠正确
# flynew = Image.open(r"E:\backup0219\SavedPictures\0601.jpg") 手动输入原来的路径加r 正确
# blurrflynew = flynew.filter(ImageFilter.GaussianBlur)
# blurrflynew.save("E:/backup0219/SavedPictures/0601_blurred.jpg")
# blurrflynew.show()
# 关于路径的问题 不能直接使用Windows 文件属性复制的路径来，这样会报错，手动输入一遍看起来一模一样就是没问题 也是有病
#coding:utf-8
from PIL import Image
import subprocess

# def cleanFile(filePath, newFilePath):
#     image = Image.open(filePath)
#
#     image = image.point(lambda  x: 0 if x < 125 else 255) #'''通过对x< 数值的调整 来去掉灰影 增加识别的准确率 测试的图片 120 -130之间效果较好。'''
#     image.save(newFilePath)
#
#     subprocess.call(["tesseract", newFilePath, 'output'])
#
#     outputFile = open("output.txt", 'r')
#     print(outputFile.read())
#     outputFile.close()
#
# cleanFile("C:/Users/XuWilliam/Pictures/Gradiant.jpg", "C:/Users/XuWilliam/Pictures/Gradiant_clean2.png")
# cleanFile("C:/Users/XuWilliam/Pictures/Gradiant.tif", "C:/Users/XuWilliam/Pictures/Gradiant_clean2.png")
# cleanFile(r"‪C:\Users\XuWilliam\Pictures\Gradiant.tif", r"C:\Users\XuWilliam\Pictures\Gradiant_clean2.png")
# 对tif格式图片不友好 还要注意处理路径问题
# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth("William", 'password')
#
# r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
#
# print(r.text)
#破解验证码
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import subprocess
# import requests
# from PIL import Image
# from PIL import ImageOps
#
# def cleanImage(imagePath):
#     image = Image.open(imagePath)
#     image = image.point(lambda  x: 0 if x < 135 else 255)
#     borderImage = ImageOps.expand(image, border=20, fill = 'white')
#     borderImage.save(imagePath)
#
# html = urlopen("http://www.pythonscraping.com/humans-only")
# bsObj = BeautifulSoup(html, features="lxml")
# imageLocatin = bsObj.find("img", {"title":"Image CAPTCHA"})["src"]
# formBuildId = bsObj.find("input", {"name":"form_build_id"})["value"]
# captchaSid = bsObj.find("input", {"name":"captcha_sid"})["value"]
# captchaToken = bsObj.find("input", {"name":"captcha_token"})["value"]
#
# captchaUrl = "http://pythonscraping.com"+imageLocatin
# urlretrieve(captchaUrl, "captcha.jpg")
# cleanImage("captcha.jpg")
# p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p.wait()
# f = open("captcha.txt", "r")
#
# captchaResponse = f.read().replace(" ", "").replace("\n", "")
# print("Captcha solution attempt: "+captchaResponse)
#
# if len(captchaResponse) == 5:
#     params = {"captcha_token":captchaToken, "captcha_sid":captchaSid, "form_id":"comment_node_page_form",
#               "form_build_id":formBuildId, "captcha_response":captchaResponse, "name":"Ryan Mitchell",
#               "subject":"I come to seek the Grail", "comment_body[und][0][value]":"...and I am definitely not a bot"}
#     r = requests.post("http://www.pythonscraping.com/comment/reply/10", data=params)
#     responseObj = BeautifulSoup(r.text)
#     if responseObj.find("div", {"class":"messages"}) is not None:
#         print(responseObj.find("div", {"class":"messages"}).get_text())
# else:
#     print("There was a problem reading the CAPTCHA correctly!")
# #反正运行了几次都失败了

#单元测试
# import unittest
#
# class TestAddition(unittest.TestCase):
#     def setUp(self):
#         print("Setting up the test")
#
#     def tearDown(self):
#         print("Tearing down the test")
#
#     def test_twoPlusTwo(self):
#         total = 9+2
#         self.assertEqual(11, total)
#
# if __name__ == "__main__":
#     unittest.main()

#测试维基百科
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import unittest
#
# class TestWikipedia(unittest.TestCase):
#     bsObj = None
#     # @classmethod
#     def setUpClass():
#         global bsObj
#         url = "http://en.wikipedia.org/wiki/Monty_Python"
#         bsObj = BeautifulSoup(urlopen(url))
#
#     def test_titleText(self):
#         global bsObj
#         pageTitle = bsObj.find("h1").get_text()
#         self.assertEqual("Monty Python", pageTitle)
#
#     def test_contentExists(self):
#         global bsObj
#         content = bsObj.find("div", {"id":"mw-content-text"})
#         self.assertIsNotNone(content)
#
# if __name__ == '__main__':
#     unittest.main()

#2
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import  unittest
# import re
# import datetime
# import random
#
# random.seed(datetime.datetime.now())
#
# class TestWikipedia(unittest.TestCase):
#     bsObj = None
#     url = None
#
#     def test_PageProperties(self):
#         global bsObj
#         global url
#
#         url = "http://en.wikipedia.org/wiki/Monty_Python"
#
#         for i in range(1, 100):
#             bsObj = BeautifulSoup(urlopen(url), "lxml")
#             titles = self.titleMatchesURL()
#             self.assertEquals(titles[0], titles[1])
#             self.assertTrue(self.contentExists())
#             url = self.getNextLink()
#         print("Done")
#
#     def titleMatchesURL(self):
#         global bsObj
#         global url
#
#         pageTitle = bsObj.find("h1").get_text()
#         urlTitle = urlopen[(url.index("/wiki")+6):]
#         urlTitle = urlTitle.replace("_", " ")
#         urlTitle = unquote(urlTitle)
#         return [pageTitle.lower(), urlTitle.lower()]
#
#     def contenExists(self):
#         global bsObj
#         content = bsObj.find("div", {"id":"mw-content-text"})
#         if content is not None:
#             return True
#         return False
#
#     def getNextLink(articleUrl):
#         html = urlopen("http://en.wikipedia.org" + articleUrl)
#         bsObj1 = BeautifulSoup(html, "lxml")
#         return bsObj1.find("div", {"id":"badyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
    # 获取随机链接有点混乱 第二遍再补上。

# import socks
# import socket
# from urllib.request import urlopen
#
# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket
# print(urlopen("http://icanhazip.com").read())
''' multiple line
ha ha ha 
hahaha
haaaaa
hhhaaaaa
'''