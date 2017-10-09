from tkinter import *
from PIL import ImageTk,Image
from PIL import ImageFilter
from PIL import Image,ImageEnhance
pic1=input()
v=Image.open(pic1)
v=v.resize((600,600))
count=0
count1=1.0
count2=0
def printing(x):
	img1=ImageTk.PhotoImage(Image.open(x))
	label.configure(image=img1)
	label.image=img1
def printing1(x):
	img1=ImageTk.PhotoImage(x)
	label.configure(image=img1)
	label.image=img1

def crop():
	global count2
	root1=Tk()
	ID=StringVar()
	labe1=Label(root1,text="l1",font=30)
	labe1.grid(row=0,column=0)
	box1=Entry(root1,bd=4,textvariable=ID)
	box1.grid(row=0,column=1)
	ID=StringVar()
	labe2=Label(root1,text="b1",font=30)
	labe2.grid(row=1,column=0)
	box2=Entry(root1,bd=4,textvariable=ID)
	box2.grid(row=1,column=1)
	ID=StringVar()
	labe3=Label(root1,text="l2",font=30)
	labe3.grid(row=2,column=0)
	box3=Entry(root1,bd=4,textvariable=ID)
	box3.grid(row=2,column=1)
	ID=StringVar()
	labe4=Label(root1,text="b2",font=30)
	labe4.grid(row=3,column=0)
	box4=Entry(root1,bd=4,textvariable=ID)
	box4.grid(row=3,column=1)
	botonA= Button(root1, text = "accept",command=lambda: get_data(box1,box2,box3,box4), width=5)
	botonA.grid(row=4,column=1)
	root1.mainloop()
def get_data(box1,box2,box3,box4):
	global v
	global count2
	a=int( box1.get())
	b=int(box2.get())
	c=int(box3.get())
	d=int(box4.get())
	area=(a,b,c,d)
	v=v.crop(area)
	v.save("y.jpg")
	printing("y.jpg")
def get_merge(photo1,photo2,temp):
	global v
	global count2
	a=photo1.get()
	b=photo2.get()
	x=Image.open(a)
	y=Image.open(b)
	x=x.resize((500,500))
	y=y.resize((500,500))
	if(temp=="A"):
		r1,g1,b1=x.split()
		r2,g2,b2=y.split()
		v=Image.merge("RGB",(r1,g2,b1))
		v.save("z.jpg")
		printing("z.jpg")
	if(temp=="B"):
		v=Image.blend(x,y,0.5)
		v.save("z.jpg")
		printing("z.jpg")
	if(temp=="C"):
		im=Image.new("RGB",(1000,500))
		im.save("v.jpg")
		im.paste(y,(0,0,500,500))
		im.save("new.jpg")
		v=Image.open("new.jpg")
		v.paste(x,(500,0,1000,500))
		v.save("c.jpg")
		printing("c.jpg")
	if(temp=="D"):
		r1,g1,b1=x.split()
		r2,g2,b2=y.split()
		v=Image.merge("RGB",(r2,g1,b1))
		v.save("z.jpg")
		printing("z.jpg")
	if(temp=="E"):
		r1,g1,b1=x.split()
		r2,g2,b2=y.split()
		v=Image.merge("RGB",(r1,g1,b2))
		v.save("z.jpg")
		printing("z.jpg")
def get_merge1(x,y):
	root7=Tk()
	buttonA=Button(root7,text="Layer Merge",command=lambda : get_merge(x,y,"A"),width=8,fg="blue",bg="black")
	buttonA.pack()
	buttonA=Button(root7,text="Layer Merge1",command=lambda : get_merge(x,y,"D"),width=8,fg="blue",bg="black")
	buttonA.pack()
	buttonA=Button(root7,text="Layer Merge2",command=lambda : get_merge(x,y,"E"),width=8,fg="blue",bg="black")
	buttonA.pack()
	buttonB=Button(root7,text="Blend",command=lambda : get_merge(x,y,"B"),width=8,fg="blue",bg="black")
	buttonB.pack()
	buttonC=Button(root7,text="Combine",command=lambda : get_merge(x,y,"C"),width=8,fg="blue",bg="black")
	buttonC.pack()
	root7.mainloop()
def merge():
	root2=Tk()
	labe1=Label(root2,text="Image1",font=30)
	labe1.grid(row=0,column=0)
	photo1=Entry(root2,bd=4)
	photo1.grid(row=0,column=1)
	labe2=Label(root2,text="Image2",font=30)
	labe2.grid(row=1,column=0)
	photo2=Entry(root2,bd=4)
	photo2.grid(row=1,column=1)
	buttonB=Button(root2,text="accept",command=lambda : get_merge1(photo1,photo2),width=5)
	buttonB.grid(row=2,column=1)
	root2.mainloop()
def get_resize(size1,size2):
	global v
	global count2
	a=int(size1.get())
	b=int(size2.get())
	v=v.resize((a,b))
	v.save("z.jpg")
	printing("z.jpg")
def resize():
	root3=Tk()
	labe2=Label(root3,text="size1",font=30)
	labe2.grid(row=1,column=0)
	size1=Entry(root3)
	size1.grid(row=1,column=1)
	labe3=Label(root3,text="size2",font=30)
	labe3.grid(row=2,column=0)
	size2=Entry(root3)
	size2.grid(row=2,column=1)
	buttoC=Button(root3,text="accept",command=lambda : get_resize(size1,size2),width=5)
	buttoC.grid(row=3,column=1)
def get_trans(deg):
	global v
	global count2
	z=float(deg.get())
	v=v.rotate(z)
	v.save("y.jpg")
	printing("y.jpg")
def get_trans1(x):
	global count
	global v
	global count2
	count=count+1
	if(count==1):
		x=float(x)
		v=v.rotate(x)
		v.save("z.jpg")
		printing("z.jpg")
	else:
		x=float(x)
		v=v.rotate(x)
		v.save("z.jpg")
		printing("z.jpg")
def transform():
	root4=Tk()
	labe=Label(root4,text="How many degrees you want rotate")
	labe.grid(row=0,column=0)
	lab=Label(root4,text="Degrees")
	lab.grid(row=1,column=0)
	Degrees=Entry(root4,bd=4)
	Degrees.grid(row=1,column=1)
	butto1=Button(root4,text="accept",fg="blue",bg="black",command=lambda : get_trans(Degrees))
	butto1.grid(row=2,column=0)
	butto2=Button(root4,text="Rotate_Left",fg="blue",bg="black",command=lambda:get_trans1(90))
	butto2.grid(row=3,column=0)
	butto3=Button(root4,text="Rotate_Right",fg="blue",bg="black",command=lambda:get_trans1(-90))
	butto3.grid(row=4,column=0)
	root4.mainloop()
def get_effects(x):
	#y=Image.open(pic1)
	global v
	global count1
	global count2
	if(x=="B"):
		v=v.convert("L")
		v.save("mtst.jpg")
		printing("mtst.jpg")
	if(x=='Bl'):
		v=v.filter(ImageFilter.BLUR)
		v.save("mtst.jpg")
		printing("mtst.jpg")
	if(x=='D'):
		v=v.filter(ImageFilter.FIND_EDGES)
		v.save("mtst.jpg")
		printing("mtst.jpg")
	#if(x=='Br'):
	if(x=='S'):
		v=ImageEnhance.Sharpness(v)
		v=v.enhance(1.0)
		v.save("mtst.jpg")
		printing("mtst.jpg")
	if(x=="Bri"):
		count1=count1+0.1
		v=ImageEnhance.Brightness(v)
		v=v.enhance(count1)
		v.save("mtst.jpg")
		printing("mtst.jpg")
	if(x=="Brd"):
		count1=count1-0.1
		v=ImageEnhance.Brightness(v)
		v=v.enhance(count1)
		v.save("mtst.jpg")
		printing("mtst.jpg")
	v=Image.open("mtst.jpg")

def effects():
	root5=Tk()
	butto1=Button(root5,text="Black_White",command= lambda : get_effects("B"),fg="blue",bg="black",width=8)
	butto1.pack()
	butto2=Button(root5,text="Blur",command= lambda : get_effects("Bl"),fg="blue",bg="black",width=8)
	butto2.pack()
	butto3=Button(root5,text="Edge",command= lambda : get_effects("D"),fg="blue",bg="black",width=8)
	butto3.pack()
	butto4=Button(root5,text="Brightness incr",command= lambda : get_effects("Bri"),fg="blue",bg="black",width=8)
	butto4.pack()
	butto5=Button(root5,text="Brightness decr",command= lambda : get_effects("Brd"),fg="blue",bg="black",width=8)
	butto5.pack()
	butto6=Button(root5,text="Sharpen",command= lambda : get_effects("S"),fg="blue",bg="black",width=8)
	butto6.pack()
def original():
	global v
	global count2
	v=Image.open(pic1)
	v=v.resize((600,600))
	printing1(v)
	count1=0.4
def New_image(photo1):
	global v
	photo1=photo1.get()
	v=Image.open(photo1)
	v=v.resize((600,600))
	printing1(v)
if(len(pic1)>0):
	root= Tk()
	root.configure(background="blue")
	root.title("Photo Editor")
	img=ImageTk.PhotoImage(v)
	label=Label(root,image=img)
	label.image=img
	label.pack(side=LEFT,fill="both",expand=YES)
	labe23=Entry(width=15)
	labe23.pack()
	label22=Button(root,text="New_image",command=lambda : New_image(labe23))
	label22.pack()
	butto1=Button(root,text="crop",fg="blue",bg="black",command=crop,width=12,height=3,font=40)
	butto1.pack(side=TOP)
	butto2=Button(root,text="Edit Two Images",fg="blue",bg="black",command=merge,width=12,height=4,font=40)
	butto2.pack()
	butto3=Button(root,text="resize",fg="blue",bg="black",command=resize,width=12,height=3,font=40)
	butto3.pack()
	butto4=Button(root,text="transform",fg="blue",bg="black",command=transform,width=12,height=3,font=40)
	butto4.pack()
	butto5=Button(root,text="effects",fg="blue",bg="black",command=effects,width=12,height=3,font=40)
	butto5.pack()
	butto6=Button(root,text="Orginal",fg="blue",bg="black",command=original,width=12,height=3,font=40)
	butto6.pack()
	root.mainloop()
else:
	root=Tk()
	label=Label(root,text="you did not enter any file name pls run the program again")
	label.pack()
	root.mainloop()
