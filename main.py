from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("Main")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("Topwin")
    l2=Label(top,text="This is top level window")
    l2.pack()
    top.mainloop()

l1=Label(root,text="This is root window")
b=Button(root,text="Click here to open a new window", command=topwin)
l1.pack()
b.pack()
root.mainloop()