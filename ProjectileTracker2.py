import time as tm
from graphics import *
from math import *

win=GraphWin('test',1280,500)
win.setCoords(0,0,1279,499)
win.setBackground('black')

class arrow():
    def __init__(self,angle,length,windowName):
        self.windowName=windowName
        self.theta=radians(angle)
        self.length=length
        self.height=self.length*sin(self.theta)
        self.base=(self.length**2-self.height**2)**(1/2)
        self.angle=angle

        height=length*sin(self.theta)
        base=(length**2-height**2)**(1/2)
        self.arrowline=Line(Point(0,0),Point(base,height))
        self.arrowline.setFill('white')
        

    def redraw(self,angle,length):
        self.arrowline.undraw()
        newline=arrow(self.angle+angle,self.length+length,self.windowName)
        p2=newline.arrowline.getP2()
        self.arrowline=Line(Point(0,0),p2)
        self.angle=newline.angle
        self.length=newline.length
        del newline
        del p2
        self.arrowline.setFill('white')
        self.arrowline.draw(self.windowName)

    def moveArrow(self):
        start=False
        message=Text(Point(639.5,470),'Select the Trajectory of the CannonBall')
        message.setFill('white')
        message.draw(self.windowName)
        while not start :
            key=self.windowName.getKey()
            if key=='Up':
                self.redraw(5,0)

            elif key=='Down':
                self.redraw(-5,0)
                
            elif key=='Right':
                self.redraw(0,5)
                
            elif key=='Left':
                self.redraw(0,-5)
                
            elif key=='Return':
                self.velocity=self.length
                start=True
                return True
            else:
                pass
    
def animateShot(angle,velocity):
    win=GraphWin('CannonShot',1260,600)
    win.setCoords(0,0,1259,599)
    win.setBackground('black')

    message=Text(Point(639.5,570),'Trajectory of CannonBall')
    message.setFill('white')
    message.draw(win)
    yspeed=Text(Point(639.5,550),(''))
    yspeed.setFill('white')
    yspeed.draw(win)
    distance=Text(Point(639.5,530),'')
    distance.setFill('white')
    distance.draw(win)

    theta = radians(angle)
    time=0.01
    xpos = 0
    ypos = 0
    xvel = velocity*cos(theta)
    yvel = velocity*sin(theta)
    
    while ypos >=0.0:
        yspeed.undraw()
        distance.undraw()

        xpos2=xpos
        ypos2=ypos
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/2.0

        yspeed.setText(('y velocity: %s'%(str(yvel1)[0:5])))
        yspeed.draw(win)
        distance.setText('Distance: {0: 0.1f}m'.format (xpos))
        distance.draw(win)

        #tm.sleep(0.05)
        l=Line(Point(xpos2,ypos2),Point(xpos,ypos))
        l.setFill('white')
        l.draw(win)
        yvel = yvel1   
        
    print ("\nDistance traveled: {0: 0.1f} meters.".format (xpos))
    win.getKey()
    win.close()



def main():
    x=arrow(45,100,win)
    x.arrowline.draw(win)
    x.moveArrow()
    
    if x.moveArrow():
        win.close()
        print(x.angle,x.velocity)
        animateShot(x.angle,x.velocity)
main()