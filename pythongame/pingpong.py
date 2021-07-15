import turtle
import os
import winsound
wn = turtle.Screen()
wn.title("copy from tokyoedtech")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#分数
score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #乌龟默认是1，1 这里定义成球拍要边长一些。
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#同样的方式定义第二个球拍 只有位置不同
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #乌龟默认是1，1 这里定义成球拍要边长一些。
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0) #位置不同

#定义球
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 #调整运行速度
ball.dy = -0.2

#弄个笔
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor() #return to the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding to make the func work
wn.listen()
wn.onkeypress(paddle_a_up, "w") #按w键 paddle_a_up 干活了
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    #动这个球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #边缘检查
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("notifi.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A :{} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A :{} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #板和球碰撞
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1