import tkinter as tk
import time
import os
from detection import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL
from tkinter import *

LARGE_FONT= ("Verdana", 12)
engine = pyclamd.ClamdAgnostic()

global logname

def call_hinsert():
    return lambda: controller.get_page(history_Page)


def viewdir():
    global folder_path
    raw_folder_path = filedialog.askdirectory()
    folder_path = raw_folder_path.replace('/','\\\\')
    print(folder_path)
    sys.stdout.flush()

def multiquarantine(file_list):
    #Multi-File Quarantine
    quarantine_directory = os.getcwd()+"\\Quarantened_Files\\"
    if not os.path.exists(quarantine_directory):
        os.makedirs(quarantine_directory)

    for each_file in file_list:
      old_location = os.path.dirname(os.path.abspath(each_file))
      new_location = quarantine_directory + each_file
      os.rename(old_location,new_location)

def quarantine(file_path):
    #Multi-File Quarantine
    quarantine_directory = os.getcwd()+"\\Quarantened_Files\\"
    print("----------------------------------------------------------------")
    print(quarantine_directory)
    print("----------------------------------------------------------------")
    sys.stdout.flush()
    if not os.path.exists(quarantine_directory):
        os.makedirs(quarantine_directory)


    old_location = file_path
    file_name = os.path.basename(file_path)
    file_name.replace('/','')
    new_location = quarantine_directory + file_name
    print("New file path location: " + new_location)
    sys.stdout.flush()
    os.rename(old_location,new_location)



def scandir():
    result = engine.contscan_file(folder_path)
    scanHis(result, folder_path)
    if (result is None):
        print('No Virus Found In This Directory')
        sys.stdout.flush()
    else:
        print(result)
        print("----------------------------------")
        sys.stdout.flush()
        result_path = next(iter(result))
        result_path = result_path.replace('\\\\','\\')
        result_path = result_path.replace('\\','/')
        print(result_path)
        print("----------------------------------")
        quarantine(result_path)
        print("File has been Quarantined")
        sys.stdout.flush()

def schedulescan():
    print("Check")
    sys.stdout.flush()
    time = self.variable.get()
    print(time)
    sys.stdout.flush()
    #Implement Scheduled Scanning
    return 0

class AntiVirus(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Load_Page, Scan_Page, quarantine_Page, history_Page, schedule_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Load_Page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

class Load_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(background='#3868a3')
        label = tk.Label(self, text="Welcome to AntiVirus Scanner", font=LARGE_FONT)
        label.configure(background='#3868a3')
        label.pack(pady=10,padx=10)

        loadbi = tk.PhotoImage(file="img/reload.png")
        scanbi = tk.PhotoImage(file="img/scan.png")
        schebi = tk.PhotoImage(file="img/schedule.png")
        quarbi = tk.PhotoImage(file="img/quarantine.png")
        histbi = tk.PhotoImage(file="img/history.png")

        button = tk.Button(self, image=loadbi,
                            command = self.load_module)
        button.image = loadbi
        button["bg"] = "#3868a3"
        button["border"] = "0"

        button2 = tk.Button(self, image=scanbi,
                            command = lambda: controller.show_frame(Scan_Page))
        button2.image = scanbi
        button2["bg"] = "#3868a3"
        button2["border"] = "0"

        button3 = tk.Button(self, image=schebi,
                            command = lambda: controller.show_frame(schedule_Page))
        button3.image = schebi
        button3["bg"] = "#3868a3"
        button3["border"] = "0"

        button4 = tk.Button(self, image=histbi,
                            command = lambda: controller.show_frame(history_Page))
        button4.image = histbi
        button4["bg"] = "#3868a3"
        button4["border"] = "0"

        button5 = tk.Button(self, image=quarbi,
                            command = lambda: controller.show_frame(quarantine_Page))
        button5.image = quarbi
        button5["bg"] = "#3868a3"
        button5["border"] = "0"

        button.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)
        button4.pack(pady=10)
        button5.pack(pady=10)

    def load_module(self):
        init()
        time.sleep(2)
        print ("end sleep")
        sys.stdout.flush()

class Scan_Page(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
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

class schedule_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Scheduled Scanning", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        variable = StringVar(self)
        variable.set("1 Day")
        w = OptionMenu(self, variable, "1 Day", "7 Days", "30 Days")
        w.pack()

        button2 = tk.Button(self, text="Schedule Scanning",
                            command=schedulescan)
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Load_Page))
        button1.pack()

class history_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Scanning History", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        lb = Listbox(self)
        self.lb = lb
        lb.pack()

        v = StringVar()
        Label(self, textvariable=v, bg="grey").pack()
        v.set("New Text!")

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Load_Page))
        button1.pack()

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
        print('TEST')
        sys.stdout.flush()

        logpath = os.getcwd() + '\\scanHistory'
        files = []
        for (dirpath, dirnames, filenames) in os.walk(logpath):
            files.extend(filenames)
            break

        for file in files:
            self.lb.insert(END, file)


class quarantine_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Quarantine System", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        lb = Listbox(self)
        lb.pack()
        lb.insert(END, "a list entry")

        for item in ["one", "two", "three", "four"]:
            lb.insert(END, item)

        deletebutton = tk.Button(self, text="Delete",
                            command=lambda lb=lb: lb.delete(ANCHOR))
        deletebutton.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Load_Page))
        button1.pack()

def main():
    app = AntiVirus()
    app.mainloop()
    return 0

if __name__ == '__main__':
    main()
