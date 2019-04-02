import tkinter as tk
import time
from detection import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL

LARGE_FONT= ("Verdana", 12)
engine = pyclamd.ClamdAgnostic()

def viewdir():
    global folder_path
    raw_folder_path = filedialog.askdirectory()
    folder_path = raw_folder_path.replace('/','\\\\')
    print(folder_path)
    sys.stdout.flush()

def scandir():
    result = engine.contscan_file(folder_path)
    if (result is None):
        print('No Virus Found In This Directory')
        sys.stdout.flush()
    else:
        print(result)
        sys.stdout.flush()

class AntiVirus(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("300x140")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Load_Page, Scan_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Load_Page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Load_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to AntiVirus Scanner", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Load Virus Library",
                            command = self.load_module)

        button2 = tk.Button(self, text="System Scan",
                            command = lambda: controller.show_frame(Scan_Page))
        button.pack()
        button2.pack()

    def load_module(self):
        init()
        time.sleep(2)
        print ("end sleep")
        sys.stdout.flush()

class Scan_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        if (engine.ping()):
            label = tk.Label(self, text="AntiVirus Library Loaded", font=LARGE_FONT)
        else:
            label = tk.Label(self, text="Please Load AntiVirus Library First", font=LARGE_FONT)

        label.pack(pady=10,padx=10)

        viewbutton = tk.Button(self, text="Browse", command=viewdir)
        viewbutton.pack()
        scanbutton = tk.Button(self, text="Scan Selected Directory", command=scandir)
        scanbutton.pack()
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Load_Page))
        button1.pack()

def main():
    app = AntiVirus()
    app.mainloop()
    return 0

if __name__ == '__main__':
    main()
