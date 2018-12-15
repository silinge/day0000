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
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "download"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, features='lxml')
downloadList = bsObj.findAll(src = True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
#下载网页上所以带有src属性的文件 注意建立了分支之后 在gitbash 切换不同分支 文件的显示是不同的 wired