formatter = "{} {} {} {}" # the {} must be blank without string

print(formatter.format(1, 2, 3, 4,9800)) #more is ok
# print(formatter.format(345)) not work
print(formatter.format("How", "you", "doing", "?"))
print(formatter.format(True, True, False, 400*2))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("可惜不是你",
                       "等到风景都看透",
                       "然后一起颤抖",
                       "才更明白什么是温柔"))

lines = ("lalala",
         "lalala",
         "看不穿是你",
         "猜不透是你瞳孔的颜色",
         "你是我一生唱不完的歌")
print(formatter.format(*lines)) #使用*将元组中的各个数据传入 数量不能少 多了就忽略后面的
print(repr(lines)) #repr 显示变量原来的样子
a = 1+2+35+2+65+100
print(repr(a))