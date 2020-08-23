from Tkinter import *
import tkFileDialog
from PIL import Image,ImageTk
import numpy as np
import sys
import MySQLdb
import tkMessageBox
from Home import Welcome_To_Sentiment_Analysis

class Authentication:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.db = MySQLdb.connect("localhost", "root", "", "sentiment_analysis")
        self.top=top
        top.geometry("400x260")
        top.title("Authentication")
        top.configure(background="#c0c0c0")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.01, relheight=1.02, relwidth=1.01)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#f4f4ff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=405)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.49, rely=0.26, relheight=0.14, relwidth=0.43)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(width=174)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.49, rely=0.57, relheight=0.14, relwidth=0.43)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(width=174)
        self.Entry2.config(show="*");

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.06, rely=0.24, height=31, width=147)
        self.Label1.configure(background="#f0f0ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter Username:''')
        self.Label1.configure(width=147)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.06, rely=0.51, height=31, width=147)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#f0f0ff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Enter Password:''')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.54, rely=0.75, height=42, width=148)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#8080ff")
        self.Button1.configure(borderwidth="1")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(command=self.login)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

    def login(self):
        cursor=self.db.cursor()
        uname=self.Entry1.get()
        password=self.Entry2.get()
        sql="select * from admin where username='"+uname +"' and password='"+password+"'"
        cursor.execute(sql)
        results=cursor.fetchall()
        count=0
        for row in results:
            count=count+1

        if count>0:
            self.top.destroy()
            global val, w, root1
            root1 = Tk()
            top1 = Welcome_To_Sentiment_Analysis(root1)
            root1.mainloop()
        else:
            tkMessageBox.showinfo("Message", "Wrong userid or password")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Authentication (root)
    root.mainloop()




if __name__ == '__main__':
    vp_start_gui()


