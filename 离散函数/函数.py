import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)



def lisan_sin():
    y1=np.sin(np.pi*x)
    plt.title('sin(n)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def lisan_ex():
    y4=e**x1*0.01
    plt.grid(True)
    plt.title('e^x(n)')
    plt.stem(x1,y4)
    plt.show()

def  lisan_jieyue():
    def dwjy(t):
        r=np.where(t>=0.0,1.0,0.0)
        return r
    n=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('u(n)')
    plt.grid(True)
    plt.stem(n,dwjy(n))
    plt.show()

def lisan_chongji():
    def dwxl(temp):
        r=np.where(temp==0.0,1.0,0.0)
        return r
    m=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('δ(n)')
    plt.grid(True)
    plt.stem(m,dwxl(m))
    plt.show()





import tkinter as tk
class App:
    def __init__(self, root):
        root.title("离散函数图像")
        frame = tk.Frame(root)
        frame.pack()
        self = tk.Button(frame, text="离散sin", fg="blue", command=lisan_sin)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散ex", fg="blue", command=lisan_ex)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散阶跃", fg="blue", command=lisan_jieyue)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散冲击", fg="blue", command=lisan_chongji)
        self.pack(side=tk.LEFT)

root = tk.Tk()
app = App(root)
root.mainloop()
