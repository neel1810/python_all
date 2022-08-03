## GUI -- Graphical User Interface -- Frontend
## Login System


## Positioning elements -- 3 methods, pack, grid, place
## pack() -- positions elements to center of the screen
## grid (row=, column=)
## -- pack and grid can not be used together
## Place(x=,y=) and pack() works together

from  tkinter import *

admin={'anoop':'1234',
       'anu':'1234'}

message= ' '

def disp():
    if ur.get() not in admin.keys():
        message ='Access Blocked' 
    elif admin[ur.get().lower()] == pw.get():
        message = 'Login Successfull'
        
    else:
        message = 'Wrong Credintial'
    Label (a, text = message,bg='yellow',fg='black').place(x = 60, y= 140)

a= Tk()
a.title('MyPage')
a.geometry('500x400')
Label(a,text='WELCOME TO THE PYTHON STUDIO ').pack()

Label(a,text='UserName: ').place(x = 20, y= 20)
ur=Entry(a)
ur.place(x = 100, y= 20)

Label(a,text='Password: ').place(x = 20, y= 60)
pw=Entry(a,show='*')
pw.place(x = 100, y= 60)

Button(a, text='LOGIN', command=disp).place(x = 70, y= 100)

