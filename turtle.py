import turtle
t = turtle.Turtle()
t.shape("turtle")
 
x1 = int(input("큰 원의 중심좌표 x1 : "))
y1 = int(input("큰 원의 중심좌표 y1 : "))
bigC = int(input("큰 원의 반지름 : "))
 
x2 = int(input("작은 원의 중심좌표 x2 : "))
y2 = int(input("작은 원의 중심좌표 y2 : "))
smallC = int(input("작은 원의 반지름 : "))
 
t.up()
t.goto(x1,y1)
t.down()
t.circle(bigC)
 
t.up()
t.goto(x2, y2)
t.down()
t.circle(smallC)
 
dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
 
if dist > bigC+smallC:
    print("두번째 원이 첫번째 원의 내부에 없습니다.")
else:
    print("두번째 원이 첫번째 원의 내부에 있습니다.")
 
