
from turtle import Turtle,Screen
import random
t=False

screen=Screen()
colors=["red","yellow","purple","orange","green","blue"]
screen.setup(width=500,height=400)
a=screen.textinput(title="Make your bet",prompt="Choose the colour: 'red','yellow','purple','orange','green','blue'")
ypos=[-100,-67,-34,34,67,100]
tur=[]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=ypos[i])
    tur.append(tim)

if a:
    t=True


while t:

    for i in tur:
        if i.xcor()>230:
            t=False
            win=i.pencolor()
            if a==win:
                print(f"you have won, the colour won is {win}")
            else:
                print(f"you lost, the colour won is {win}")
        move = random.randint(0, 10)
        i.forward(move)








screen.exitonclick()