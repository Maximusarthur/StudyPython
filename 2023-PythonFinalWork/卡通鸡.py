from turtle import *
from math import *

# 高级椭圆参数方程（颜色），sita为逆时针旋转角度
def ty_c(x, y, sita, a, b, p, q, c):
    fillcolor(c)
    si = 2 * pi / 100
    penup()
    goto(x + a * cos(sita), y + a * sin(sita))
    pendown()
    t = 0
    for i in range(201):
        if i * si + sita <= p:
            penup()
            goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita), y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
            pendown()
        elif p <= i * si + sita <= q + 2 * pi / 100:
            if t == 0:
                begin_fill()
                t = 1
            goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita), y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
    end_fill()

# 高级椭圆方程
def ty(x, y, sita, a, b, p, q):
    si = 2 * pi / 100
    penup()
    goto(x + a * cos(sita), y + a * sin(sita))
    pendown()
    for i in range(201):
        if i * si + sita < p:
            penup()
            goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita), y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
            pendown()
        elif p <= i * si + sita <= q + 2 * pi / 100:
            goto(x + a * cos(i * si) * cos(sita) - b * sin(i * si) * sin(sita), y + a * cos(i * si) * sin(sita) + b * sin(i * si) * cos(sita))
speed(2)
hideturtle()
# 篮球
speed(50)
pensize(10)
pencolor('black')
ty_c(350, -267, 0, 161, 161, 0, 2 * pi, '#ff9900')
ty(350, -267 + 161 + 50, 0, 161, 161, 7 * pi / 6 + pi / 12, 11 * pi / 6 - pi / 12)
ty(350, -267 - 161 - 50, 0, 161, 161, pi / 6 + pi / 12, 5 * pi / 6 - pi / 12)
ty(350, -267 + 161 + 330, 0, 500, 500, 8.5 * pi / 6, 9.5 * pi / 6)
# 脸
pensize(20)
ty_c(0, 0, 0, 657 / 2, 576 / 2, 0, 2 * pi, '#ffcc00')
# 眼睛
pensize(22)
ty_c(55, 52, 0, 106, 104, 0, 2 * pi, 'white')
ty_c(-165, 60, 0, 101, 99, 0, 2 * pi, 'white')
pensize(20)
ty_c(4, 79, 0, 14, 14, 0, 2 * pi, 'black')
ty_c(-201, 80, 0, 14, 14, 0, 2 * pi, 'black')
# 嘴巴
pensize(12)
speed(50)
ty_c(-66, -76, 0, 102, 62, 0, 2 * pi, '#ff6600')
penup()
goto(-155, -50)
pendown()
goto(-134, -64)
goto(-115, -74)
goto(-90, -82)
goto(-67, -86)
goto(-47, -85)
goto(-25, -82)
goto(0, -77)
goto(15, -66)
goto(25, -55)
# 腮红
pensize(1)
speed(50)
pencolor('red')
ty_c(-256, -90, 15 * pi / 180, 49, 66, 0, 2 * pi + 15 * pi / 180, 'red')
ty_c(201, -105, 0, 73, 75, 0, 2 * pi, 'red')
# 领口
color('black', 'black')
pensize(10)
penup()
goto(-275, -227)
pendown()
begin_fill()
goto(-241, -209)
goto(-189, -233)
goto(-166, -260)
goto(-127, -272)
goto(-88, -252)
goto(-49, -233)
goto(-19, -227)
goto(51, -237)
goto(108, -242)
goto(168, -242)
goto(210, -233)
goto(250, -206)
goto(252, -254)
goto(216, -269)
goto(-13, -353)
goto(-65, -362)
goto(-109, -356)
goto(-178, -317)
goto(-214, -296)
goto(-246, -266)
goto(-272, -245)
goto(-275, -227)
end_fill()
# 衣服
penup()
goto(-244, -287)
pendown()
begin_fill()
goto(-269, -314)
goto(-310, -405)
goto(-304, -410)
goto(-21, -416)
goto(317, -410)
goto(331, -398)
goto(323, -381)
goto(319, -356)
goto(315, -320)
goto(275, -266)
goto(263, -257)
pensize(15)
pencolor('#c0c0c0')

goto(252, -254)
goto(216, -269)
goto(-13, -353)
pensize(13)
goto(-65, -362)
goto(-109, -356)
pensize(10)
goto(-178, -317)
goto(-214, -296)
goto(-246, -284)
end_fill()
# 肩带
penup()
goto(-206, -310)
pendown()
pensize(30)
goto(-183, -363)
goto(-180, -384)
goto(-184, -414)

penup()
goto(229, -285)
pendown()
goto(203, -360)
pensize(34)
goto(190, -415)

penup()
goto(-115, -360)
pendown()
pensize(8)
goto(-96, -411)
goto(-75, -413)
goto(18, -371)
goto(69, -341)
goto(105, -325)
pensize(12)
goto(177, -297)
# 中分
pencolor('#808080')
pensize(1)
penup()
goto(67, 393)
pendown()
fillcolor('#808080')
begin_fill()
goto(43, +419)
goto(13, +431)
goto(-96, +426)
goto(-156, +402)
goto(-239, +336)
goto(-277, +300)
goto(-307, +263)
goto(-372, +153)
goto(-383, +101)
goto(-373, +57)
goto(-339, +38)
goto(-298, +40)
goto(-278, +61)
goto(-236, +74)
goto(-176, +103)
goto(-163, +128)
goto(-135, +224)
goto(-95, +265)
goto(-64, +271)
goto(-30, +253)
goto(22, +269)
goto(61, 268)
goto(75, 202)
goto(93, 132)
goto(108, 71)
goto(136, 31)
goto(171, 4)
goto(236, -10)
goto(277, -10)
goto(323, -25)
goto(363, -61)
goto(404, -35)
goto(423, 14)
goto(453, 71)
goto(457, 120)
goto(441, 170)
goto(398, 227)
goto(331, 285)
goto(283, 323)
goto(232, 360)
goto(168, 396)
goto(122, 416)
goto(87, 406)
goto(67, 393)
end_fill()
pencolor('black')
pensize(4)
goto(-30, +253)

done()