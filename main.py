import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk

app = tk.Tk()
app.title('Login System')
app.geometry('500x350')
app.configure(bg="orange")
app.resizable(False,False)
app.iconbitmap('mainico.ico')

login_user = StringVar()
login_pass = StringVar()
register_user = StringVar()
register_pass = StringVar()
register_auth = StringVar()
#------------------------------------------------

def sign_in():
  login_win = Toplevel()
  login_win.title('Sign In')
  login_win.geometry('600x450')
  login_win.configure(bg="gold")
  login_win.resizable(False,False)
  login_win.iconbitmap("sign_in_ico.ico")

  global login_user
  global login_pass

  msg1 = tk.Label(login_win, text='User Name',font=(10),relief=GROOVE)
  msg1.place(relx=0.1, rely=0.3, anchor=CENTER)

  msg2 = tk.Label(login_win, text=' Password ', font=(10), relief=GROOVE)
  msg2.place(relx=0.1, rely=0.5, anchor=S)

  user_name = Entry(login_win, textvariable=login_user,font=(10), relief=GROOVE)
  user_name.place(relx=0.6, rely=0.3, anchor=CENTER, width=300)

  user_pass = Entry(login_win, show="*",
                    textvariable=login_pass, font=(10), relief=GROOVE)
  user_pass.place(relx=0.6, rely=0.5, anchor=S, width=300,)

  button = tk.Button(login_win, text='Sign In', width=20, height=2, command=check,
                     activebackground="dark grey", activeforeground="red",  relief=GROOVE)
  button.place(relx=0.5, rely=0.7, anchor=CENTER)

  stop = tk.Button(login_win, text='EXIT', width=20, height=2, command=login_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
  stop.place(x=375,y=400, anchor=SE)
#------------------------------------------------


def sign_up():

  register_win = Toplevel()
  register_win.title('Sign Up')
  register_win.geometry('650x500')
  register_win.configure(bg="gold")
  register_win.resizable(False,False)
  register_win.iconbitmap("sign_up_ico.ico")
  global register_user
  global register_pass
  global register_auth

  msg1 = tk.Label(register_win, text='User Name',font=(10), relief=GROOVE)
  msg1.place(relx=0.2, rely=0.2, anchor=CENTER)

  msg2 = tk.Label(register_win, text=' Password ', font=(10), relief=GROOVE)
  msg2.place(relx=0.2, rely=0.4, anchor=CENTER)

  msg3 = tk.Label(register_win, text='Authorization', font=(10), relief=GROOVE)
  msg3.place(relx=0.2, rely=0.6, anchor=CENTER)

  user_name = Entry(register_win, relief=GROOVE,font=(10), textvariable=register_user)
  user_name.place(relx=0.6, rely=0.2, anchor=CENTER, width=300)

  user_pass = Entry(register_win, relief=GROOVE,font=(10), textvariable=register_pass)
  user_pass.place(relx=0.6, rely=0.4, anchor=CENTER, width=300,)

  auth = Entry(register_win, textvariable=register_auth, font=(10), relief=GROOVE)
  auth.place(relx=0.6, rely=0.6, anchor=CENTER, width=300)

  button = tk.Button(register_win, text='Sign Up', width=20, height=2, command=add_user,
                     activebackground="dark grey", activeforeground="red", relief=GROOVE)
  button.place(x=300,y=375, anchor=CENTER)

  stop = tk.Button(register_win, text='EXIT', width=20,height=2, command=register_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
  stop.place(x=375, y=465, anchor=SE)
#------------------------------------------------


def check():
  global login_user
  global login_pass
  a = login_user.get()
  b = login_pass.get()

  files_in_osdir = os.listdir()
  if a in files_in_osdir:
    userfile = open(a, "r")
    checking = userfile.read().splitlines()
    if b in checking:
      success = Toplevel()
      success.geometry("350x250")
      success.resizable(False,False)
      success.iconbitmap("green_ico.ico")
      success.configure(bg="peach puff")
      success.title("Successfull Sign In")
      stop = tk.Button(success, text='Success', width=25, height=2, command=success.destroy,
                        font=('times',15,'bold'),relief=GROOVE)
      stop.place(relx=0.5, rely=0.5, anchor=CENTER)

    else:
      wrong_pass = Toplevel()
      wrong_pass.geometry("350x250")
      wrong_pass.title("Wrong PassWord")
      wrong_pass.configure(bg="peach puff")
      wrong_pass.resizable(False,False)
      wrong_pass.iconbitmap("red_ico.ico")
      stop = tk.Button(wrong_pass, text='Wrong Password', width=25, height=2,
                       command=wrong_pass.destroy, font=('times',13,'bold'),relief=GROOVE)
      stop.place(relx=0.5, rely=0.5, anchor=CENTER)

  else:
    user_not_found = Toplevel()
    user_not_found.geometry("350x250")
    user_not_found.title("User not Found ")
    user_not_found.configure(bg="peach puff")
    user_not_found.resizable(False,False)
    stop = tk.Button(user_not_found, text='User not Found Kindly register First', width=30,
                     height=2,font=('times',13,'bold'), command=user_not_found.destroy, relief=GROOVE)
    stop.place(relx=0.5, rely=0.5, anchor=CENTER)
#------------------------------------------------


def add_user():
  global register_user
  global register_pass
  global register_auth

  username = register_user.get()
  password = register_pass.get()
  auth = register_auth.get()

  if auth == "12345":

    file = open(username, "w")
    file.write(username + "\n")
    file.write(password)
    file.close()

    success = Toplevel()
    success.geometry("350x250")
    success.configure(bg="peach puff")
    success.title("Successfull Sign up")
    success.resizable(False,False)
    success.iconbitmap("green_ico.ico")
    sop = tk.Button(success, text='Success', width=25, height=2, command=success.destroy,
                    font=('times',15,'bold'), relief=GROOVE)
    sop.place(relx=0.5, rely=0.5, anchor=CENTER)

  else:
    wrong_auth = Toplevel()
    wrong_auth.geometry("350x250")
    wrong_auth.title("Wrong Authorization")
    wrong_auth.configure(bg="peach puff")
    wrong_auth.resizable(False,False)
    wrong_auth.iconbitmap("red_ico.ico")
    stop = tk.Button(wrong_auth, text='Wrong Auth', width=25, height=2,
                     command=wrong_auth.destroy, font=('times',13,'bold'), relief=GROOVE)
    stop.place(relx=0.5, rely=0.5, anchor=CENTER)
#----------------------------------------------

pic = Image.open("images.jpg")#(for image in main(app) page)
picture = ImageTk.PhotoImage(pic)

image =tk.Button(app, width=200, height=200, image=picture)
image.place(relx=0.5, rely=0.35, anchor=CENTER)

login = tk.Button(app, text='Sign In', width=20, height=3, command=sign_in,
                  activebackground="dark grey", activeforeground="red", relief=GROOVE)
login.place(relx=0.3, rely=0.75, anchor=CENTER)

register = tk.Button(app, text='Sign Up', width=20, height=3, command=sign_up,
                     activebackground="dark grey", activeforeground="red", relief=GROOVE)
register.place(relx=0.7, rely=0.75, anchor=CENTER)

stop = tk.Button(app, text='stop', width=20, height=1, command=app.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(x=325,y=330, anchor=SE)

app.mainloop()

