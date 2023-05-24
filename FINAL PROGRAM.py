import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
db=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library'
    )
my_cur=db.cursor()
root=tkinter.Tk()
def TEACHER():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    #Canvas.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()



    def RETURN():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='library'
            )
        my_cur=db.cursor()

        def entry():
            root=Tk()
            root.title('Teacher Account')
            root.geometry('250x300')
            Label(root,text="Book return",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Book Name").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Book Number").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="Return Date" ).grid(row=6,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            Label(root,text="" ).grid(row=7,column=0)
            def returnbk():
                bkname=v1.get()
                bkno=v2.get()
                isdt=v3.get()
                my_cur=db.cursor()
                my_cur.execute('insert into BOOKS values(%s,%s)',(bkname,bkno))
                db.commit()
                messagebox.showinfo('successful','Thank you... Keep Reading :)')
                v1.set('')
                v2.set('')
                v3.set('')
            def clear():
                v1.set('')
                v2.set('')
                v3.set('')
            def close():
                root.destroy()
            Button(root,text='RETURN', command=returnbk).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()
        entry()
    def ISSUE():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='library'
            )
        my_cur=db.cursor()
        def entry():
             root=Tk()
             root.title('Teacher Account')
             root.geometry('250x300')
             Label(root,text="Book Issue",font='missy').grid(row=0,columnspan=2)
             Label(root,text="").grid(row=1,column=0)
             Label(root,text="Book Name").grid(row=2,column=0)
             Label(root,text="").grid(row=3,column=0)
             Label(root,text="Book Number").grid(row=4,column=0)

             Label(root,text="" ).grid(row=5,column=0)
             Label(root,text="Issue Date" ).grid(row=6,column=0)
             v1=StringVar()
             v2=StringVar()
             v3=StringVar()
             e1=Entry(root, textvariable=v1).grid(row=2,column=1)
             e2=Entry(root, textvariable=v2).grid(row=4,column=1)
             e3=Entry(root, textvariable=v3).grid(row=6,column=1)
             Label(root,text="" ).grid(row=7,column=0)
             def issue():
                 bkname=v1.get()
                 bkno=v2.get()
                 isdt=v3.get()
                 my_cur=db.cursor()
                 my_cur.execute('delete from BOOKS where book_no=%s',(bkno))
                 db.commit()
                 messagebox.showinfo('successful','you have issued the book :)')
                 v1.set('')
                 v2.set('')
                 v3.set('')
             def clear():
                 v1.set('')
                 v2.set('')
                 v3.set('')

             def close():
                 root.destroy()
             Button(root,text='ISSUE', command=issue).grid(row=10,column=0)
             Button(root,text='RESET', command=clear).grid(row=10,column=1)
             Button(root,text='EXIT', command=close).grid(row=10,column=2)
             root.mainloop()

        entry()
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="WELCOME TEACHER", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
    btn1 = Button(root,text="RETURN BOOK",bg='black', fg='white',command=RETURN)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="ISSUE BOOK",bg='black', fg='white',command=ISSUE)
    btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()


def STUDENT():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    #Canvas.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    def RETURN():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='kvdiat',
            database='library'
            )
        my_cur=db.cursor()
        def entry():
            root=Tk()
            root.title('Student Account')
            root.geometry('250x300')
            Label(root,text="Book return",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Book Name").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Book Number").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="Return Date" ).grid(row=6,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            Label(root,text="" ).grid(row=7,column=0)
            def returnbk():
                bkname=v1.get()
                bkno=v2.get()
                isdt=v3.get()
                my_cur=db.cursor()
                my_cur.execute('insert into BOOKS values(%s,%s)',(bkname,bkno))
                db.commit()
                messagebox.showinfo('successful','Thank you... Keep Reading :)')
                v1.set('')
                v2.set('')
                v3.set('')
            def clear():
                v1.set('')
                v2.set('')
                v3.set('')
            def close():
                root.destroy()
            Button(root,text='RETURN', command=returnbk).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()
        entry()
    def ISSUE():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='library'
            )
        my_cur=db.cursor()
        def entry():
            root=Tk()
            root.title('Student Account')
            root.geometry('250x300')
            Label(root,text="Book Issue",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Book Name").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Book Number").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="Issue Date" ).grid(row=6,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            Label(root,text="" ).grid(row=7,column=0)
            def issue():
                bkname=v1.get()
                bkno=v2.get()
                isdt=v3.get()
                my_cur=db.cursor()
                my_cur.execute('delete from BOOKS where book_no=%s',(bkno))
                db.commit()
                messagebox.showinfo('successful','you have issued the book :)')
                v1.set('')
                v2.set('')
                v3.set('')
            def clear():
                v1.set('')
                v2.set('')
                v3.set('')

            def close():
                root.destroy()
            Button(root,text='ISSUE', command=issue).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()

        entry()
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="WELCOME STUDENT", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
    btn1 = Button(root,text="ISSUE BOOK",bg='black', fg='white',command=ISSUE)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="RETURN BOOK",bg='black', fg='white',command=RETURN)
    btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()

def LIBRARIAN():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    #Canvas.sdestroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    def ADD():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='library'
            )
        my_cur=db.cursor()

        def entry():
            root=Tk()
            root.title('Student Details')
            root.geometry('250x300')
            Label(root,text="Library Details",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Username").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Password").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="class" ).grid(row=6,column=0)
            Label(root,text="" ).grid(row=7,column=0)
            Label(root,text="admssion number" ).grid(row=8,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            v4=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            e4=Entry(root, textvariable=v4).grid(row=8,column=1)
            Label(root,text="" ).grid(row=9,column=0)

            def insert():
                name=v1.get()
                pswd=v2.get()
                cl=v3.get()
                admno=v4.get()
                my_cur=db.cursor()
                my_cur.execute('insert into student values(%s,%s,%s,%s)',(name,pswd,cl,admno))
                db.commit()
                messagebox.showinfo('successful','1 record inserted')
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')

            def clear():
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')
            def close():
                root.destroy()
            Button(root,text='SUBMIT', command=insert).grid(row=10,column=0)
            Button(root,text='RESET', command=clear).grid(row=10,column=1)
            Button(root,text='EXIT', command=close).grid(row=10,column=2)
            root.mainloop()
        entry() 
    def EXIT():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='library'
            )
        my_cur=db.cursor()

        def entry():
            root=Tk()
            root.title('Student Details')
            root.geometry('250x300')
            Label(root,text="Library Details",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Username").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Password").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="class" ).grid(row=6,column=0)
            Label(root,text="" ).grid(row=7,column=0)
            Label(root,text="admssion number" ).grid(row=8,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            v4=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            e4=Entry(root, textvariable=v4).grid(row=8,column=1)
            Label(root,text="" ).grid(row=9,column=0)
            def delete():
                name=v1.get()
                pswd=v2.get()
                cl=v3.get()
                admno=v4.get()
                my_cur=db.cursor()
                my_cur.execute('delete from student where admno=%s',(admno))
                db.commit()
                messagebox.showinfo('successful','1 record deleted')
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')

            def clear():
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')
            def close():
                root.destroy()
            Button(root,text='SUBMIT', command=delete).grid(row=10,column=0)
            Button(root,text='RESET', command=clear).grid(row=10,column=1)
            Button(root,text='EXIT', command=close).grid(row=10,column=2)
            root.mainloop()
        entry() 
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="WELCOME LIBRARIAN", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
    btn1 = Button(root,text="ADD NEW STUDENT/TEACHER",bg='black', fg='white',command=ADD)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="REMOVE STUDENT/TEACHER",bg='black', fg='white',command=EXIT)
    btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()



c=Canvas(root,width=3000,height=3000)
c.pack()
img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\oldlib.gif")
c.create_image(0,0, anchor=NW , image=img)
headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="WELCOME TO OUR LIBRARY", fg='black',font="Times")
headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
headingLabel.config(height=10,width=25)
btn1 = Button(root,text="TEACHER",bg='black', fg='white',command=TEACHER)
btn1.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="STUDENT",bg='black', fg='white',command=STUDENT)
btn2.place(relx=0.35,rely=0.3, relwidth=0.2,relheight=0.1)

btn3 = Button(root,text="LIBRARIAN",bg='black', fg='white', command=LIBRARIAN)
btn3.place(relx=0.60,rely=0.3, relwidth=0.2,relheight=0.1)
mainloop()

