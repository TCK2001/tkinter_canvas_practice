from tkinter import*
import random
from turtle import bgcolor, fillcolor, filling

quotes=["Everything counts.","Make it count","Be yourself"]
meaning=["경험하는 모든 순간들이 축적됩니다.","가치 있는 순간을 만들어라.","진정한 자신의 모습으로 살아가세요."]

def click():
    random_quote=random.randint(0,2)
    Canvas.itemconfig(eng,text=quotes[random_quote])
    Canvas.itemconfig(kor,text=meaning[random_quote])


win=Tk()
win.title("TCK 명언")
win.option_add("*Font","궁서 20")
win.resizable(False,False)

Canvas=Canvas(win,width=700,height=500,bg="pink")
img=PhotoImage(file="C:\Temp/night.png")
Canvas.create_image(350,250,image=img)
eng=Canvas.create_text(350,150,text="오늘의 명언",fill="white",font="궁서 30")
kor=Canvas.create_text(350,200,text="",fill="white",font="궁서 20")
Canvas.pack()

btn=Button(win)
btn.config(text="보기",bg="black",fg="pink",font="궁서 20",command=click)
btn.place(x=310,y=400)


win.mainloop()