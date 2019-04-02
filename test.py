from tkinter import filedialog
from tkinter import *
from detection import *
import sys
from time import sleep
import tkinter as tk

def viewdir():
    global folder_path
    folder_path = filedialog.askdirectory()
    print(folder_path)
    sys.stdout.flush()

def load():
    init()
    print("Loading finished")

m = tk.Tk()
m.title('Anti Virus Scanner')
label = tk.Label(m, text="Waiting for the software to load.")
label.pack()

m.after(200, load)
m.mainloop()

print("TEST point")
sys.stdout.flush()
#viewbutton = Button(text="Browse", command=viewdir).grid(row=2, column=3)
#scanb = Button(m, text="Scan", command=callback)


def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.frame = tk.Frame(self)
    self.geometry("200x200")
    self.frame.pack(side="top", fill = "both", expand=True)
    self.label = tk.Label(self, text = "Welcome to Anti Virus Scanner")
    button1 = tk.Button(self, text = "Load Module",
                              command = self.load_module)
    self.label.pack(in_=self.frame)
    button1.pack(in_=self.frame)

def load_module(self):
    self.label.config(text = "Loading Virus Module")
    init()
    self.label.update_idletasks()
    time.sleep(2)
    print ("end sleep")
    self.label.config(text = "Done Loading")
