import tkinter
import lib

root = tkinter.Tk()
address = "88:1B:99:09:E8:96"
lib.connect(address)
def w():
   lib.moveForward()

def s():
   lib.moveBackward()
   
def a():
   lib.moveLeftward()
   
def d():
   lib.moveRightward()
   
def c():
   lib.turnLeft2()
   
def v():
   lib.turnRight2()
   
def l():
   lib.shootLeft()
   
def r():
   lib.shootLeft()

w = tkinter.Button(root, text ="Move Forward", command = w)
w.grid(row=0,column=0)

s = tkinter.Button(root, text ="Move Backward", command = s)
s.grid(row=1,column=0)

a = tkinter.Button(root, text ="Move leftward", command = a)
a.grid(row=2,column=0)

d = tkinter.Button(root, text ="Move rightward", command = d)
d.grid(row=3,column=0)

c = tkinter.Button(root, text ="turn left", command = c)
c.grid(row=0,column=1)


v = tkinter.Button(root, text ="turn right", command = v)
v.grid(row=1,column=1)

l = tkinter.Button(root, text ="shoot left", command = l)
l.grid(row=0,column=2)

r = tkinter.Button(root, text ="shoot right", command = r)
r.grid(row=1,column=2)

root.mainloop()
