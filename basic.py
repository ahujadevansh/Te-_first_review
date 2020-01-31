import tkinter as tk
from PIL import Image,ImageTk

class Basic:
    def __init__(self,root):
        self.root=root

        self.f=tk.Frame(self.root,height=950,width=1688)
        self.f.pack()

        self.bgimg=ImageTk.PhotoImage(Image.open("images/os_bg.jpg"))
        self.panel=tk.Label(self.f,image=self.bgimg)
        self.panel.pack()

        self.header=tk.Message(self.f,width=1688,font="Times 25 bold",
                                text="\t\t\t\t\tQ n A System\t\t\t  ",bg="BLACK",fg="WHITE",relief=tk.SOLID,
                                borderwidth=2)
        self.header.place(x=2,y=2)
        self.panel.pack_propagate(0)
        self.f.pack_propagate(0)
        self.f.grid_propagate(0)
        