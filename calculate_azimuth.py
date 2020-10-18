#find azimuth 

import tkinter as tk
import math 


class azimuthAngle(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x200')

        self.label = tk.Label(text = 'Azimuth Calculation Program',
                font = ('calibre',10,'bold')).grid(row=0,column = 2)

        self.angles()

    def angles(self):
        self.label1 = tk.Label(text = 'x coord. of point 1 = ').grid(row=1,column=1)
        self.label2 = tk.Label(text = 'y coord. of point 1 = ').grid(row=2,column=1)
        self.label3 = tk.Label(text = 'x coord. of point 2 = ').grid(row=3,column=1)
        self.label4 = tk.Label(text = 'y coord. of point 2 = ').grid(row=4,column=1)


        self.x_of_point1 = tk.Entry()
        self.x_of_point1.grid(row=1,column=2)
        self.y_of_point1 = tk.Entry()
        self.y_of_point1.grid(row=2,column=2)

        self.x_of_point2 = tk.Entry()
        self.x_of_point2.grid(row=3,column=2)
        self.y_of_point2 = tk.Entry()
        self.y_of_point2.grid(row=4,column=2)

        self.answer = tk.Button(text = 'Answer',
                font = ('calibre',10,'bold'),
                command = self.islem)
        self.answer.grid(row=5,column = 2)

    def islem(self):
        self.x1 = self.x_of_point1.get()
        self.y1 = self.y_of_point1.get()
        self.x2 = self.x_of_point2.get()
        self.y2 = self.y_of_point2.get()

        try:
            self.dif_y = float(self.y2) - float(self.y1)
            self.dif_x = float(self.x2) - float(self.x1)
        
            self.length = ((self.dif_y)**2 + (self.dif_x)**2)**0.5

            self.az_ang = 0

            value = lambda y,x : math.atan(abs(y)/abs(x)) 

            if (self.dif_y > 0 and self.dif_x > 0):
                self.az_ang = value(self.dif_y, self.dif_x)
                self.az_ang =  ((self.az_ang * 200) / math.pi)

            elif (self.dif_y > 0 and self.dif_x < 0):
                self.az_ang = value(self.dif_y, self.dif_x)
                self.az_ang = 200 - ((self.az_ang * 200) / math.pi)

            elif (self.dif_y < 0 and self.dif_x < 0):
                self.az_ang = value(self.dif_y, self.dif_x)
                self.az_ang = 200 + ((self.az_ang * 200) / math.pi)

            else:
                self.az_ang = value(self.dif_y, self.dif_x)
                self.az_ang = 400 - ((self.az_ang * 200) / math.pi)
                
            self.result1 = tk.Label(text='azimuth is: ')
            self.result1.grid(row=6,column=1)
            self.result2 = tk.Label(text=f'{self.az_ang:.4f} grad ')
            self.result2.grid(row=6,column=2)

            self.length1 = tk.Label(text='length is: ')
            self.length1.grid(row=7,column=1)
            self.length2 = tk.Label(text=f'{self.length:.4f}')
            self.length2.grid(row=7,column=2)
        
        except ValueError:
            self.error1 = tk.Label(text=' Enter numbers only ')
            self.error1.grid(row=6,column=2)

        except ZeroDivisionError:
            self.error2 = tk.Label(text='Cannot divide by zero')
            self.error2.grid(row=6,column=2)
        


if __name__ == '__main__':
    a = azimuthAngle()
    a.mainloop()

