from turtle import*
import time
def drawGap():           #绘制数码管间隔
    penup()
    fd(5)
def drawLine(draw):      #绘制单段数码管
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)
def drawDigit(digit):    #根据数字绘制单个数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawDate(date):
    pencolor("red")
    for i in date:
        if i=='-':
            write("年",font=("Arial",18,"normal"))
            pencolor("green")
            fd(40)
        elif i=='=':
            write("月",font=("Arial",18,"normal"))
        elif i=='+':
            write("日",font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    setup(800,350,200,200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    hideturtle()
    done()
main()
