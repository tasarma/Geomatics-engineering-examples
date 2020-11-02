# https://en.wikipedia.org/wiki/Delaunay_triangulation


import sys
import math as mt
import numpy as np
import turtle as tt
import tkinter as tk
import matplotlib.pyplot as plt 


#Take screen width and height for turtle screesizes
st = tk.Tk()
width = st.winfo_screenwidth()
height = st.winfo_screenheight()
st.destroy()


ID = [] #Point id
x = []  #X coordinate of point
y = []  #Y coordinate of point
s = 0   #Length of data

def reading_file():
    #=== Read the data form file ===

    print('Please wait...')
    with open('data.txt', 'r') as data:
        reading = data.readlines()
        content = []
        s = len(reading)

        for i in range(s):
            dividing = reading[i].split()
            content.append(dividing)
            IDs = content[i][0]
            xs = float(content[i][1])
            ys = float(content[i][2])
            ID.append(IDs)
            x.append(xs)
            y.append(ys)

        
        #Find turtle interior screen' coordinate sistem dimensions
        #according to X and Y values at project
        n = float(max(x)) - float(min(x))
        m = float(max(y)) - float(min(y))
        tt.delay(0)
        tt.setup(width=height, height=height, startx=None, starty=0)
        dn = n/15
        dm = m/15
        if n>m:
            tt.setworldcoordinates(min(y)-dn, min(x)-dn, min(y)+n+dn, max(x)+dn)
        elif n<m:
            tt.setworldcoordinates(min(y)-dm, min(x)-dm, max(y)+dm, min(x)+m+dm)
        else:
            tt.setworldcoordinates(min(y)-dm, min(x)-dm, max(y)+dm, max(x)+dm)


        tt.penup()
        for i in range(s):
            tt.goto(x[i],y[i]);tt.dot(5,'black')
            tt.write(ID[i],False,'left',('Arial',15,'normal'))
            #tt.write(str(tt.pos()),False,'right')

reading_file()


class Point():
    def __init__ (self,ID,x,y):
        self.ID = ID
        self.x = x
        self.y = y
        
points = []
for i in range(len(x)):
    a = Point(ID[i],float(x[i]),float(y[i]))
    points.append(a)



def circumcircleCenter(a,b,c):
    #=== Compute circumcenter of a triangle ===

    xy = []
    D = 2*(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y))
    x = ((a.y**2 + a.x**2)*(b.y - c.y) + (b.y**2 + b.x**2)*(c.y - a.y) + (c.y**2 + c.x**2)*(a.y - b.y))/D
    xy.append(x)
    y = ((a.y**2 + a.x**2)*(c.x - b.x) + (b.y**2 + b.x**2)*(a.x - c.x) + (c.y**2 + c.x**2)*(b.x - a.x))/D
    xy.append(y)

    return xy



def circumcircleRadious(a,b,c):
    #=== Compute circumradious of a triangle ===

    def side(p,q):
        return mt.sqrt((float(q.x)-float(p.x))**2 + (float(q.y)-float(p.y))**2)
    s1 = side(a,b)
    s2 = side(a,c)
    s3 = side(b,c)

    r = 2*(s1*s2*s3) / (mt.sqrt((s1+s2+s3)*(s2+s3-s1)*(s3+s1-s2)*(s1+s2-s3)))

    return r





def delanuay(points):
    sid = []
    sos = []
    sos.append(sys.maxsize)
    sos.append(sys.maxsize)
    sos.append(sys.maxsize)
    sid.append(sos)
    for i in range(len(points)):
        for j in range(len(points)):
            for k in  range(len(points)):
                if i ==len(points):
                    break
                a1 = points[i]
                a2 = points[j]
                a3 = points[k]
                tt.penup()
                
                if a1.ID != a2.ID and a2.ID != a3.ID and a1.ID != a3.ID:
                    r = circumcircleRadious(a1,a2,a3)
                    center = circumcircleCenter(a1,a2,a3)
                    
                    soo = []
                    for m in range(len(points)):
                        if points[m].ID != a1.ID and points[m].ID != a2.ID and points[m].ID != a3.ID:
                            distance = mt.sqrt((center[0]-points[m].x)**2 + (center[1]-points[m].y)**2)
                            soo.append(distance)
                    
                    def plot(a):
                        noo = 0
                        
                        ins = []
                        for i in range(len(soo)):
                            if float(soo[i]) < r/2:
                                noo +=1
                        if noo == 0:
                            ins.append(a1.ID)
                            ins.append(a2.ID)
                            ins.append(a3.ID)
                            tt.up()
                            tt.goto(center[0],center[1])
                            
                            tt.rt(90)
                            tt.fd(r/2)
                            tt.lt(90)
                            tt.down()
                            tt.delay(0)
                            tt.circle(r/2)
                            tt.undo()
                            tt.up()
                            
                           
                            tt.goto(a1.x,a1.y);tt.dot(10,'red')
                            tt.down()
                            tt.goto(a2.x,a2.y);tt.dot(10,'red')
                            tt.goto(a3.x,a3.y)
                            tt.goto(a1.x,a1.y)
                            tt.up()   
                        
                        else:
                            tt.up()
                            tt.goto(center[0],center[1])
                            tt.rt(90)
                            tt.fd(r/2)
                            tt.lt(90)
                            tt.down()
                            tt.delay(0)
                            tt.circle(r/2)
                            tt.undo()
                            tt.up()

                        if ins!=[]:
                            sid.append(ins)
                            indx = sid.index(ins)
                            for i in range(len(sid)-1):
                                if (ins[0] == sid[i][0]) or (ins[0] == sid[i][1]) or (ins[0] == sid[i][2]):
                                    if (ins[1] == sid[i][0]) or (ins[1] == sid[i][1]) or (ins[1] == sid[i][2]):
                                        if (ins[2] == sid[i][0]) or (ins[2] == sid[i][1]) or (ins[2] == sid[i][2]):
                                            del sid[indx]
                                          
                        return noo
                        
                        
                    plot(soo)
 
    del sid[0]
    return sid


trian = []
commonside = {}

a = delanuay(points)

for i in range(len(a)):
    #=== Draw circle ===
    
    no =[]
    no.append(i+1)
    no.append(a[i])
    trian.append(no)
    
    
    n1 = int(a[i][0])
    n2 = int(a[i][1])
    n3 = int(a[i][2])
    tt.delay(0)
    tt.up()
    tt.goto((points[n1-1].x+points[n2-1].x+points[n3-1].x)/3,(points[n1-1].y+points[n2-1].y+points[n3-1].y)/3)
    tt.write(i+1,False,'center',('Arial',15,'normal'))
    tt.rt(90)
    tt.fd(80)
    tt.lt(90)
    tt.down()
    tt.circle(200)


