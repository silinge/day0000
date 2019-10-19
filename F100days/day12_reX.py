# 正则表达式
# 6位数的QQ号
# import re
#
# def mainly():
#     username = input("Enter your name:")
#     qq = input("Enter your QQ ID: ")
#     # match 函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r"^[0-9a-zA-Z_]{6,20}$", username)
#     """ {6,20} 6和20中间不要写空格!!!!!"""
#     if not m1:
#         print("Enter the right username.")
#     m2 = re.match(r"^[1-9]\d{4,11}$", qq)
#     if not m2:
#         print('Enter a right qq id.')
#     if m1 and m2:
#         print("Great, the info is valid!")
#
# if __name__ == '__main__':
#     mainly()

# 提取手机号
# import re
#
# def mainly():
#     '''创建正则表达式,使用了预测和回顾来保证手机号前后不应该出现数字'''
#     pattern = re.compile(r'(?<=\D)1[345789]\d{9}(?=\D)')
#     sentence = '''重要的事情说113078432930遍, 我的手机号是13718695521, 不是15926243315, 不是120或者999
#     , 大长今的电话号码是13088889999, 今英的手机号是15010101011. 最后一个电话号码后面还要写内容不能是空,
#     不然匹配不到,为空对象或者没有位置都不行.比如这个手机号你就看不到13077778888'''
#     # 查找所有匹配并保存在一个列表中
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('-'*10+'分割线'+'-'*10)
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('-'*10+'分割线'+'-'*10)
#     # 通过search函数来搜索指定位置并找出所有匹配
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
#
# if __name__ == '__main__':
#     mainly()
# 屏蔽不良词语
# import re
# def mainly():
#     sentence = "Damn it, are you crazy? you sucker, stupid ugly ass, perv, sick bastard, screw it, go to hell"
#     purified = re.sub('damn|crazy|stupid|suck|bastard|screw|hell|ass', '**', sentence, flags=re.IGNORECASE)
#     print(print(purified))
#     # flags= 是正则表达式的匹配标记 指定忽略大小写, 进行多行匹配,显示调试信息等 可以多参数 例如 flags=re.a | re.b | re.c
# if __name__ == '__main__':
#     mainly()

# 拆分字符串
# import re
# def whatever():
#     poems = '人生若只如初见,何事秋风悲画扇,等闲变却故人心。却道故人,心易变.'
#     sentence_list = re.split(r'[,.。,]', poems)
#     while ' ' in sentence_list:
#         sentence_list.remove(' ')
#     print(sentence_list)
#
# if __name__ == '__main__':
#     whatever()
#
# import pyperclip
# # 转义字符
# print('my bro\'s name is \'008\'')
# # 原始字符
# print(r'my sister\'s name is \'Robbin\'')
# str = 'helloohMaria'
# print('he'in str)
# print('llol' in str)
# print(str.isalpha())
# print(str.isalnum()) #判断字符串是否含有字母和数字
# print(str.isdecimal()) #判断字符串是否只含数字
# print(str[0:5].isalpha())
# print(str[3:6].isdecimal())
# list = ['你是不能不漂荡的风', '东风夜放花千树','众里寻他千百度','独上高楼望断天涯路', '衣带渐宽终不悔']
# print('**'.join(list))
# sentence = 'I will be right here waiting for you.'
# words_list = sentence.split()
# print(words_list)
# email = '    jackfrueding@126.com    '
# print(email)
# print(email.strip())
# print(email.lstrip())
# # 将文本放入剪切板中
# # pyperclip.copy('为伊消得人憔悴')
# # 从系统剪切板获得文本 greattttt
# print(pyperclip.paste())

# from io import StringIO
#
# def reverse_str1(str):
#     return str[::-1]
#
# def reverse_str2(str):
#     if len(str) <= 1:
#         return str
#     return reverse_str2(str[1:]) + str[0:1]
#
# def reverse_str3(str):
#     #StringIO对象是python中可变字符串
#     #不应该使用不变字符串做字符串连接操作 因为会产生很多无用字符串对象
#     rstr = StringIO()
#     str_len = len(str)
#     for index in range(str_len - 1, -1, -1):
#         rstr.write(str[index])
#     return rstr.getvalue()
#
# def reverse_str4(str):
#     return ''.join(str[index] for index in range(len(str) - 1, -1, -1))
#
# def reverse_str5(str):
#     # 将字符串处理成列表
#     str_list = list(str)
#     str_len = len(str)
#     # 使用zip函数将两个序列合并成一个产生元组的迭代器
#     # 每次正好可以取到一前一后两个下标来实现元素的交换
#     for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
#         str_list[i], str_list[j] = str_list[j], str_list[i]
#     # 将列表元素连接成字符串
#     return ''.join(str_list)
#
# if __name__ == '__main__':
#     str = 'life is short, I use Python.'
#     print(reverse_str1(str))
#     print(str)
#     print(reverse_str2(str))
#     print(str)
#     print(reverse_str3(str))
#     print(str)
#     print(reverse_str4(str))
#     print(str)
#     print(reverse_str5(str))
#     print(str)
#
# import re
#
# def mainly():
#     username = input('Enter a username: ')
#     qq = input('Enter the qq ID:')
#     M1 = re.match(r'^[0-9a-zA-Z]{6,20}$', username)
#     if not M1:
#         print('Enter a valid username: ')
#     M2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not M2:
#         print('Enter a valid ID.')
#     if M1 and M2:
#         print('It is correct!')
#
# if __name__ == '__main__':
#     mainly()

# 手机号的检测
# import re
#
# def mainly():
#     pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
#     sentence = '''重要的申请就要多说1213176764321次, 我的手机号那就是14512344321, 不是15500008181, 也不是120, 999, 911,
#     长今的手机号13322223333, 今英的手机号是15025025025, 嗯.'''
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('分....隔....线....')
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('分....隔....线....')
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
#
# if __name__ == '__main__':
#     mainly()

# 净化
# import re
#
# def mainly():
#     sentence = 'damn it, holy crap, what a crazy ugly ass, stupid nerd, go to hell sucker'
#     purified = re.sub('damn|ass|stupid|nerd|hell|suck|crap|crazy|ugly', '666', sentence, flags=re.IGNORECASE)
#     print(purified)
#
# if __name__ == '__main__':
#     mainly()