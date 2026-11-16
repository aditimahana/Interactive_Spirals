# CircleSpiral4.py
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.speed(0)
colors = ["crimson", "navajowhite", "cornflowerblue", "olivedrab"]
for x in range(150):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(95)
