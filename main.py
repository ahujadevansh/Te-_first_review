import tkinter as tk
from basic import *
from input_output import *

class Main(Basic):
    def __init__(self,root):
        super().__init__(root)
        self.add_buttons()

    def add_buttons(self):

        self.stimg=ImageTk.PhotoImage(Image.open("images/start.jpg"))
        self.start_button=tk.Button(self.panel,image=self.stimg,command=self.input)
        self.start_button.place(x=40,y=300)
        
        self.eximg=ImageTk.PhotoImage(Image.open("images/exit.jpg"))
        self.exit_button=tk.Button(self.panel,image=self.eximg,command=self.exit)
        self.exit_button.place(x=270,y=300)

    def input(self):
        self.f.destroy()
        self.i=InputPage(root)
    
    def exit(self):
        self.root.destroy()





        
root=tk.Tk()
f=Main(root)
root.mainloop()