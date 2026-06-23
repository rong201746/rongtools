from tkinter import Tk,PhotoImage,Canvas
s=0
def add_self(image=None,title="rongmove"):
	global s
	win=Toplevel()
	win.title(title)
	draw=Canvas(win)
	if image=None:
		s=draw.create_rectangle(10,10,50,50,fill="black",outline="yellow")
	else:
		s=create_image(0,0,image=PhotoImage(image))
def Down(w):
	glodal s
	draw.move(s,0,w)
def Up(w):
	glodal s
	w="-"+w
	draw.move(s,0,w)
def Left(w)：
	glodal s
	w="-"+w
	s.move(s,w,0)
def Right(w):
	global s
	s.move(s,w,0)
	