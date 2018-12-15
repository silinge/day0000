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
import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],' \
             '"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+
      jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))