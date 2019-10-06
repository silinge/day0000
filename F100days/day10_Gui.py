# import tkinter
# import tkinter.messagebox
#
# def mainly():
#     flag = True
#
#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello, world!') if flag else ('blue', 'Goodbye, world!')
#
#         label.config(text=msg, fg=color)
#
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定退出?'):
#             top.quit()
#
#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('600x400')
#     # 标题
#     top.title('little game')
#     # 创建标签对象并添加顶层窗口
#     label = tkinter.Label(top, text="Hello, world!", font='Arial -32', fg = 'red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象， 指定添加到哪个容器中，通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command = change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command = confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     mainly()

# import pygame
#
# def mainly():
#     # 初始化pygame 模块
#     pygame.init()
#     # 初始化并显示窗口尺寸(
#     screen = pygame.display.set_mode((800, 600))
#     # 设置当前窗口标题
#     pygame.display.set_caption("big ball talk to small ball.")
#
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并处理他
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running == False
#
# if __name__ == '__main__':
#     mainly()

# import pygame
#
# def mainly():
#     pygame.init()
#     screen = pygame.display.set_mode((1000, 400))
#     pygame.display.set_caption('小小大大')
#     screen.fill((33, 240, 189))
#     pygame.draw.circle(screen, (255, 80, 80), (120, 120), 60, 0)
#     # 绘制一个圆 参数是屏幕 颜色 圆心位置 半径 0表示填充圆
#
#     # 刷新窗口
#     pygame.display.flip()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
# if __name__ == '__main__':
#     mainly()

# import pygame
# def mainly():
#     pygame.init()
#     screen = pygame.display.set_mode((600, 500))
#     pygame.display.set_caption('消息啊大大大')
#     x, y = 60, 40
#     running = True
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.fill((222, 111, 45))
#         pygame.draw.circle(screen, (255, 20, 20), (x, y), 30, 0)
#         pygame.display.flip()
#         pygame.time.delay(100)
#         x, y = x + 5, y + 5
#
# if __name__ == '__main__':
#     mainly()
#
# from enum import Enum, unique
# from math import sqrt
# from random import randint
#
# import pygame
#
# @unique
# class Color(Enum):
#     '''颜色'''
#
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (220, 220, 220)
#
#     @staticmethod
#     def random_color():
#
#         r = randint(0, 240)
#         g = randint(0, 255)
#         b = randint(0, 199)
#         return (r, g, b)
#
# class Ball(object):
#     '''球'''
#
#     def __init__(self, x, y, radius, sx, sy, color = Color.RED):
#         '''初始化'''
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move(self, screen):
#         '''移动'''
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy
#
#     def eat(self, other):
#         '''吃其他球'''
#         if self.alive and other.alive and self != other:
#             dx, dy = self.x - other.x, self.y - other.y
#             distance = sqrt(dx ** 2 + dy ** 2)
#             if distance < self.radius + other.radius and self.radius > other.radius:
#                 other.alive = False
#                 self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self, screen):
#         '''绘制球'''
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
#
# def mainly():
#     # 定义用来装所有球的容器
#     balls = []
#     pygame.init()
#     # 初始化窗口尺寸
#     screen = pygame.display.set_mode((800, 800))
#     # 设置标题
#     pygame.display.set_caption("吃吧。")
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 # 处理鼠标事件代码
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                     # 获取点击鼠标的位置
#                 x, y = event.pos
#                 radius = randint(10, 100)
#                 sx, sy = randint(-10, 10), randint(-10, 10)
#                 color = Color.random_color()
#                     # 点击鼠标位置创建一个球（大小，速度，颜色随机）
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 balls.append(ball)
#         screen.fill((233, 222, 240))
#         # 取出容器中的球，如果没有被吃掉就绘制，被吃掉就移除
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#
#         pygame.display.flip()
#         # 每隔50毫秒就改变球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             # 检查有没有吃到其他球
#             for other in balls:
#                 ball.eat(other)
#
# if __name__ == '__main__':
#     mainly()

# from enum import Enum, unique
# from math import sqrt
# from random import randint
# import pygame
#
# @unique
# class Color(Enum):
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (222, 233, 244)
#
#     @staticmethod
#     def random_color():
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         return (r, g, b)
#
# class Ball(object):
#
#     def __init__(self, x, y, radius, sx, sy, color = Color.RED):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move(self, screen):
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.sy - self.radius <= 0 or self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy
#
#     def eat(self, other):
#         if self.alive and other.alive and self != other:
#             dx, dy = self.x - other.x, self.y - other.y
#             distance = sqrt(dx ** 2 + dy ** 2)
#             if distance < self.radius + other.radius and self.radius > other.radius:
#                 other.alive = False
#                 self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
#
# def mainly():
#     balls = []
#     pygame.init()
#     screen = pygame.display.set_mode((400, 900))
#     print(screen.get_width())
#     print(screen.get_height())
#     pygame.display.set_caption('以大吃小')
#     x, y = 50, 60
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 x, y = event.pos
#                 radius = randint(10, 100)
#                 sx, sy = randint(-10,10), randint(-10, 10)
#                 color = Color.random_color()
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 balls.append(ball)
#
#         screen.fill((255, 255, 255))
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#
#         pygame.display.flip()
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             for other in balls:
#                 ball.eat(other)
#
#
# if __name__ == '__main__':
#     mainly()

# import tkinter
#
# def mouse_evt_handler(evt=None):
#     row = round((evt.y - 20)/40)
#     col = round((evt.x - 20)/40)
#     pos_x = 40 * col
#     pos_y = 40 * row
#     canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill= 'black')
#
# top = tkinter.Tk()
# # 设置窗口尺寸
# top.geometry('650x650')
# top.title('五子棋')
# # 设置窗口尺寸不可改变
# top.resizable(False, False)
# # 设置窗口置顶
# top.wm_attributes('-topmost', 1)
# canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
# canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
# for index in range(15):
#     canvas.create_line(20, 20+40*index, 580, 20 + 40*index, fill='black')
#     canvas.create_line(20+40*index, 20, 20+40*index, 580, fill='black')
# canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
# canvas.pack()
# tkinter.mainloop()

# import tkinter
# import time
#
# # 播放动画效果的函数
# def play_animation():
#     canvas.move(oval, 2, 2)
#     canvas.update()
#     top.after(50, play_animation)
#
# x = 10
# y = 10
# top = tkinter.Tk()
# top.geometry('700x650')
# top.title('动画效果')
# top.resizable(False, False)
# top.wm_attributes('-topmost', 1)
# canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
# canvas.create_rectangle(0, 0, 600, 600, fill='green')
# oval = canvas.create_oval(10, 10, 60, 60, fill='blue')
# canvas.pack()
# top.update()
# play_animation()
# tkinter.mainloop()

# import turtle as t
# t.pensize(3)
# t.penup()
# t.goto(-180, 150)
# t.pencolor('red')
# t.fillcolor('yellow')
# t.pendown()
# t.begin_fill()
# for _ in range(36):
#     t.forward(200)
#     t.right(170)
# t.end_fill()
# t.mainloop()