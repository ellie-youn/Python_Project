# 터틀 그래픽을 활용하여 별 모양 그리기

import turtle

t = turtle.Pen()

for i in range(5):
    t.forward(50)
    t.right(144)

turtle.exitonclick()