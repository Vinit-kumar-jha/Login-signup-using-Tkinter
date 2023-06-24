from tkinter import *
from PIL import ImageTk

#functionality part
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def signup_page():
    login_window.destroy()
    import signup

 #===============gui-part======
login_window=Tk()
login_window.geometry('790x512+50+50')
login_window.resizable(0,0) #would not be able to maximize the window
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='background.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',20,'bold')
              ,bg='white',fg='firebrick1')
heading.place(x=520,y=50)



usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold')
                    ,bd=0,fg='firebrick1')
usernameEntry.place(x=480,y=120)
usernameEntry.insert(0,'Username')


usernameEntry.bind('<FocusIn>',user_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=480,y=142)


passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',10,'bold')
                    ,bd=0,fg='firebrick1')
passwordEntry.place(x=480,y=180)
passwordEntry.insert(0,'Password')


passwordEntry.bind('<FocusIn>',password_enter)
Frame(login_window,width=250,height=2,bg='firebrick1').place(x=480,y=202)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=700,y=175)




forgotButton=Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',font=('Microsoft Yahei UI Light',11,'bold'),
                    fg='firebrick1',activeforeground='firebrick1')
forgotButton.place(x=600,y=210)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),
                   fg='white',bg='firebrick1',activeforeground='white'
                   ,activebackground='firebrick1',cursor='hand2',bd=0,width=19)
loginButton.place(x=480,y=250)

orLabel=Label(login_window,text= "----------------OR—---------------",font=('Open Sans',16),
              fg='firebrick1',bg='white')
orLabel.place(x=470,y=300)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=530,y=350)


google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=580,y=350)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=630,y=350)

signupLabel=Label(login_window,text= "Don’t have an account ?",font=('OpenSans','9','bold'),
                  fg='firebrick1',bg='white')
signupLabel.place(x=480,y=420)

newaccountButton=Button(login_window,text='Create new one',
                        font=('Open Sans','9','bold underline'),fg='blue',bg='white',
                        activeforeground='blue',activebackground='white',cursor='hand2',
                        bd=0,command=signup_page)
newaccountButton.place(x=630,y=420)

login_window.mainloop()
