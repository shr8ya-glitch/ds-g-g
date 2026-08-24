from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Events")
window.geometry("100x100")
def key(event):
    print(event.char)
window.bind("<Key>",key)
def handle(event):
    print("Button was clicked")
    messagebox.showinfo("Alert","Virus Detected")
button=Button(text="Click Me")
button.pack()
button.bind("<Button-1>",handle)
window.mainloop()