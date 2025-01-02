import turtle

def draw_stool():
    # 创建一个海龟对象，用于绘制
    t = turtle.Turtle()

    # 设置绘制速度和粗细
    t.speed(10)
    t.pensize(3)

    t.fillcolor("yellow")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.setheading(15)
    t.forward(150)
    t.setheading(165)
    t.forward(150)
    t.setheading(-165)
    t.forward(150)
    t.setheading(-15)
    t.forward(150)
    t.setheading(15)
    t.forward(150)
    t.setheading(-90)
    t.forward(20)
    t.setheading(-165)
    t.forward(150)
    t.setheading(165)
    t.forward(150)
    t.setheading(90)
    t.forward(20)
    t.end_fill()
    t.setheading(15)
    t.forward(150)

    # 绘制靠背
    t.begin_fill()
    t.setheading(90)
    t.forward(180)
    t.setheading(-15)
    t.forward(150)
    t.setheading(-90)
    t.forward(180)
    t.end_fill()
    t.fillcolor("white")
    t.setheading(165)
    t.forward(30)
    t.setheading(90)
    t.penup()
    t.forward(35)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.setheading(165)
    t.forward(30)
    t.setheading(-90)
    t.forward(100)
    t.setheading(-15)
    t.forward(30)
    t.end_fill()
    t.setheading(-90)
    t.penup()
    t.forward(35)
    t.pendown()
    t.setheading(165)
    t.forward(60)
    t.penup()
    t.setheading(90)
    t.forward(35)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.setheading(165)
    t.forward(30)
    t.setheading(-90)
    t.forward(100)
    t.setheading(-15)
    t.forward(30)
    t.end_fill()

    # 绘制桌腿
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(-90)
    t.forward(170)
    t.setheading(15)
    t.forward(20)
    t.setheading(90)
    t.forward(168)
    t.end_fill()
    t.begin_fill()
    t.backward(168)
    t.setheading(-165)
    t.forward(20)
    t.setheading(165)
    t.forward(20)
    t.setheading(90)
    t.forward(168)
    t.end_fill()

    t.penup()
    t.goto(120, 10)
    t.pendown()
    t.begin_fill()
    t.setheading(-90)
    t.forward(170)
    t.setheading(15)
    t.forward(20)
    t.setheading(90)
    t.forward(168)
    t.end_fill()
    t.begin_fill()
    t.backward(168)
    t.setheading(-165)
    t.forward(20)
    t.setheading(165)
    t.forward(20)
    t.setheading(90)
    t.forward(166)
    t.end_fill()

    t.penup()
    t.goto(-120, 10)
    t.pendown()
    t.begin_fill()
    t.setheading(-90)
    t.forward(170)
    t.setheading(15)
    t.forward(20)
    t.setheading(90)
    t.forward(168)
    t.end_fill()
    t.begin_fill()
    t.backward(168)
    t.setheading(-165)
    t.forward(20)
    t.setheading(165)
    t.forward(20)
    t.setheading(90)
    t.forward(170)
    t.end_fill()



    # 隐藏海龟并显示绘画结果
    turtle.done()

draw_stool()