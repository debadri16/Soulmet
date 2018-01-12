import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

class Soulmet:
    def __init__(self):
        #connect to the db
        self.conn=mysql.connector.connect(user='root',password='',host='localhost',database='soulmet')
        self.mycursor=self.conn.cursor()
        self.program_menu()


    def program_menu(self):

        # create the layout
        self.root = Tk()
        self.root.title('Soulmet')
        self.root.maxsize(250, 200)
        self.root.minsize(250, 200)
        self.emaillabel = Label(self.root, text='Email: ')
        self.emaillabel.grid(row=0, column=0)
        self.emailInput = Entry(self.root)
        self.emailInput.grid(row=0, column=1)

        self.passwordlabel = Label(self.root, text='Password: ')
        self.passwordlabel.grid(row=1, column=0)
        self.passwordinput = Entry(self.root)
        self.passwordinput.grid(row=1, column=1)

        self.submitbutton = Button(self.root, text="Login", command=self.login)
        self.submitbutton.grid(row=2, column=1)

        self.registerbutton = Button(self.root, text="Register", command=self.register)
        self.registerbutton.grid(row=3, column=1)

        self.forgotpass = Button(self.root, text="Forgot password?", command=self.updatepass)
        self.forgotpass.grid(row=4, column=1)

        self.exitbutton = Button(self.root, text="Exit", command=self.exit_db)
        self.exitbutton.grid(row=5, column=1)

        self.root.mainloop()

    def user_menu(self):
        self.root.destroy()
        self.root3 = Tk()
        self.root3.title("Welcome")
        self.root3.maxsize(200, 150)
        self.root3.minsize(200, 150)

        self.viewall=Button(self.root3,text="View all users",command=self.view_all_users).grid(row=0,column=1)

        self.proposals = Button(self.root3, text="View who proposed you", command=self.view_proposal).grid(row=1, column=1)

        self.proposed = Button(self.root3, text="View whom you proposed", command=self.view_propposed).grid(row=2, column=1)

        self.matches = Button(self.root3, text="View matches", command=self.view_matches).grid(row=3, column=1)

        self.logout = Button(self.root3, text="Logout", command=self.logout).grid(row=4, column=1)

    def login(self):
        email=self.emailInput.get()
        password=self.passwordinput.get()
        query='''select * from `users` where `email` like '{}' and `password` like '{}' '''.format(email,password)
        self.mycursor.execute(query)
        lst=self.mycursor.fetchall()
        if len(lst)==1:
            self.current_user_id = lst[0][0]
            self.is_logged_in = 1
            self.user_menu()
        else:
            messagebox.showerror("Incorrect credentials", "Enter correct email or password")

    def register(self):
        self.root1=Tk()
        self.root1.title('Registration')
        self.root1.maxsize(300,200)
        self.root1.minsize(300,200)
        self.namelabel = Label(self.root1, text='Name: ').grid(row=0, column=0)
        self.nameInput = Entry(self.root1)
        self.nameInput.grid(row=0, column=1)

        self.elabel = Label(self.root1, text='Email: ').grid(row=1, column=0)
        self.eInput = Entry(self.root1)
        self.eInput.grid(row=1, column=1)

        self.passlabel = Label(self.root1, text='Password: ').grid(row=2, column=0)
        self.passInput = Entry(self.root1)
        self.passInput.grid(row=2, column=1)

        self.genderlabel = Label(self.root1, text='Gender (Male/Female): ').grid(row=3, column=0)
        self.genderInput=Entry(self.root1)
        self.genderInput.grid(row=3,column=1)
        self.citylabel = Label(self.root1, text='City: ').grid(row=4, column=0)
        self.cityInput = Entry(self.root1)
        self.cityInput.grid(row=4, column=1)

        self.regbutton = Button(self.root1, text="Register",command=self.reg).grid(row=5, column=1)

    def reg(self):
        name =self.nameInput.get()
        email =self.eInput.get()
        password =self.passInput.get()
        gender =self.genderInput.get()
        city =self.cityInput.get()
        query = '''insert into `users` (`user_id`,`name`,`email`,`password`,`gender`,`city`) 
        values (NULL,'{}','{}','{}','{}','{}')'''.format(name, email, password, gender, city)
        self.mycursor.execute(query)
        self.conn.commit()
        messagebox.showinfo("Registered","You are registered")
        self.root1.destroy()

    def updatepass(self):
        self.root1 = Tk()
        self.root1.title('Password update')
        self.root1.maxsize(300, 200)
        self.root1.minsize(300, 200)
        self.namelabel = Label(self.root1, text='Name: ').grid(row=0, column=0)
        self.nameInput = Entry(self.root1)
        self.nameInput.grid(row=0, column=1)

        self.elabel = Label(self.root1, text='Email: ').grid(row=1, column=0)
        self.eInput = Entry(self.root1)
        self.eInput.grid(row=1, column=1)

        nextbutton = Button(self.root1, text="Next", command=lambda: updt()).grid(row=2, column=1)

        def updt():
            name = self.nameInput.get()
            email = self.eInput.get()
            query = '''select * from `users` where `email` like '{}' and `name` like '{}' '''.format(email, name)
            self.mycursor.execute(query)
            lst = self.mycursor.fetchall()
            if len(lst) == 0:
                messagebox.showwarning("Incorrect credentials","Enter correct name and email!")
            else:
                self.passInput = Label(self.root1, text='New password: ').grid(row=3, column=0)
                self.passInput = Entry(self.root1)
                self.passInput.grid(row=3, column=1)

                updatebutton = Button(self.root1, text="Update", command=lambda: updtp()).grid(row=4, column=1)

                def updtp():
                    newpass = self.passInput.get()
                    query2 = '''update `users` set `password`='{}' where `users`.`email`='{}' '''.format(newpass, email)
                    self.mycursor.execute(query2)
                    self.conn.commit()
                    messagebox.showinfo("Password update","Your password is updated successfully")
                    self.root1.destroy()

    def exit_db(self):
        reply=messagebox.askyesno("Exit", "Do you want to exit?")
        if reply==True:
            exit()

    def view_all_users(self):
        query = '''select * from `users` where `user_id` not like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        all_user_list = self.mycursor.fetchall()
        self.root1 = Tk()
        self.root1.title('All users')
        self.root1.minsize(400, 200)
        self.root1.maxsize(400, 1000)
        j=0
        for i in all_user_list:
            str1='-------------------------------------------------\n'
            str1=str1+str(i[0])+'   '+str(i[1])+'   '+str(i[4])+'   '+str(i[5])
            str1=str1+'\n-------------------------------------------------'
            self.lable = Label(self.root1, text=str1).grid(row=j, column=0)
            j+=1

        self.lable1 = Label(self.root1, text='Enter the ID of the user you want to propose: ').grid(row=j, column=0)
        self.lableInput = Entry(self.root1)
        self.lableInput.grid(row=j, column=1)
        propbutton = Button(self.root1, text="Propose", command=self.propose).grid(row=j+2, column=1)

    def propose(self):
        self.proposed_user_id=self.lableInput.get()
        query = '''insert into `proposal` (`proposal_id`,`romeo_id`,`juliet_id`)
                values
                (NULL,'{}','{}')'''.format(self.current_user_id, self.proposed_user_id)
        self.mycursor.execute(query)
        self.conn.commit()
        messagebox.showinfo("Propposed","Proposal sent")

    def view_proposal(self):
        self.root1 = Tk()
        self.root1.title('Proposals')
        self.root1.minsize(400, 200)
        self.root1.maxsize(400, 1000)
        query = '''select * from `proposal` p join `users` u
                        on p.`romeo_id`=u.`user_id` where p.`juliet_id` like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst = self.mycursor.fetchall()
        if len(proposed_lst)==0:
            self.lable1 = Label(self.root1, text='No proposals yet!').grid(row=0, column=0)
        else:
            j = 0
            for i in proposed_lst:
                str1 = '-------------------------------------------------\n'
                str1 = str1 + str(i[4]) + '   ' + str(i[7]) + '   ' + str(i[8])
                str1 = str1 + '\n-------------------------------------------------'
                self.lable = Label(self.root1, text=str1).grid(row=j, column=0)
                j += 1

    def view_propposed(self):
        self.root1 = Tk()
        self.root1.title('Proposed')
        self.root1.minsize(400, 200)
        self.root1.maxsize(400, 1000)
        query = '''select * from `proposal` p join `users` u
                on p.`juliet_id`=u.`user_id` where p.`romeo_id` like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst = self.mycursor.fetchall()
        if len(proposed_lst)==0:
            self.lable1 = Label(self.root1, text='You have been a jerk till now!').grid(row=0, column=0)
        else:
            j = 0
            for i in proposed_lst:
                str1 = '-------------------------------------------------\n'
                str1 = str1 + str(i[4]) + '   ' + str(i[7]) + '   ' + str(i[8])
                str1 = str1 + '\n-------------------------------------------------'
                self.lable = Label(self.root1, text=str1).grid(row=j, column=0)
                j += 1

    def view_matches(self):
        self.root1 = Tk()
        self.root1.title('Soulmets')
        self.root1.minsize(400, 200)
        self.root1.maxsize(400, 1000)
        query ='''select * from `proposal` p join `users` u on u.`user_id`=p.`juliet_id` 
        where `romeo_id`='{}' and `juliet_id` in (select `romeo_id` from `proposal` where `juliet_id`='{}')'''.format(self.current_user_id,self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst = self.mycursor.fetchall()
        if len(proposed_lst) == 0:
            self.lable1 = Label(self.root1, text='You are ugly and poor!').grid(row=0, column=0)
        else:
            j = 0
            for i in proposed_lst:
                str1 = '-------------------------------------------------\n'
                str1 = str1 + str(i[4]) + '   ' + str(i[7]) + '   ' + str(i[8])
                str1 = str1 + '\n-------------------------------------------------'
                self.lable = Label(self.root1, text=str1).grid(row=j, column=0)
                j += 1

    def logout(self):
        reply=messagebox.askyesno("Warning","Are you sure you want to logout?")
        if reply==True:
            self.is_logged_in=0
            self.root3.destroy()
            obj1=Soulmet()

obj1=Soulmet()