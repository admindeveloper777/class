# from tkinter import*
# root=Tk()
# root.title("dasturcham")

# i=Label(root,text="Hammaga salom dostlar")
# # i.pack()
# # i.pack(side=TOP)
# i.grid(row=10,column=10)
# l=Label(root,text="salom barcha barchaga")
# l.grid(row=1,column=1)

# def ism():
# 	soz="hello"+e.get()
# 	# i=Label(root,text=soz)
# 	# i.pack()
# tugma=Button(root,text="Enter your name",bg="white",fg=("blue"),padx=10,pady=10,command=ism)
# tugma.pack()

# tug=Button(root,text="salom",bg="yellow",fg=("blue"),padx=30,pady=30)
# tug.pack()

# tugm=Button(root,text="hay",bg="red",fg=("blue"),padx=30,pady=30)
# tugm.pack()
# tugma.pack()

# e=Entry(root,width=10,bg="red",fg="yellow",borderwidth=5)
# e.pack()
# e.insert(0,"ism kiriting")


# root.mainloop()




from tkinter import*
root=Tk()
root.title("dastur")

e=Entry(root,width=50,borderwidth=3,bg="yellow",fg="red")
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def tugma_add():
	return
tugma1=Button(root,text="1",fg="red",bg="yellow",padx=40,pady=20,comman=tugma_add)
tugma2=Button(root,text="2",fg="red",padx=40,bg="yellow",pady=20,comman=tugma_add)
tugma3=Button(root,text="3",fg="red",padx=40,bg="yellow",pady=20,comman=tugma_add)
tugma4=Button(root,text="4",fg="red",padx=40,bg="yellow",pady=20,comman=tugma_add)
tugma5=Button(root,text="5",fg="red",padx=40,bg="yellow",pady=20,comman=tugma_add)
tugma6=Button(root,text="6",fg="red",padx=40,bg="yellow",pady=20,comman=tugma_add)
tugma7=Button(root,text="7",fg="red",padx=40,pady=20,bg="yellow",comman=tugma_add)
tugma8=Button(root,text="8",fg="red",padx=40,pady=20,bg="yellow",comman=tugma_add)
tugma9=Button(root,text="9",fg="red",padx=40,pady=20,bg="yellow",comman=tugma_add)
tugma0=Button(root,text="0",fg="red",padx=40,pady=20,bg="yellow",comman=tugma_add)
tugma11=Button(root,text="+",fg="red",padx=40,pady=20,bg="yellow",common=tugma_add)
tugma12=Button(root,text="=",fg="red",padx=40,pady=20,bg="yellow",common=tugma_add)

tugma1.grid(row=3 ,column=0)
tugma2.grid(row=3 ,column=1)
tugma3.grid(row=3 ,column=2)

tugma4.grid(row=2,column=0)
tugma5.grid(row=2,column=1)
tugma6.grid(row=2,column=2)

tugma7.grid(row=1,column=0)
tugma8.grid(row=1,column=1)
tugma9.grid(row=1,column=2)

tugma0.grid(row=4,column=0)
tugma11.grid(row=4,column=1)
tugma12.grid(row=4,column=2)
root.mainloop()