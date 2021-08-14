import turtle
import math

r = int(input("Nhập bán kính hình tròn: "))

n = turtle.Turtle()
n.pensize(3)
n.circle(r)
turtle.done()

c = 2 * math.pi * r
s = math.pi * (r**2)

print("Chu vi diện tích hình tròn có bán kính {r} là: {c}".format(r=r,c=c))
print("Diện tích hình tròn có bán kính {r} là: {s}".format(r=r,s=s))

