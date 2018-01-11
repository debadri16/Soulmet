import mysql.connector

class Soulmet:
    def __init__(self):
        #connect to db
        self.conn=mysql.connector.connect(user='root',password='',host='localhost',database='soulmet')
        self.mycursor=self.conn.cursor()
        self.program_menu()

    def program_menu(self):
        program_input=int(input('''what would you like to do?
        1. Register
        2. Login to your account
        3. Forgot password?
        4. Exit '''))
        if program_input==1:
            self.register()
        elif program_input==2:
            self.login()
        elif program_input==3:
            self.updatepass()
        else:
            exit()

    def user_menu(self):
        user_input=input('''What would you like to do?
        1. View all users
        2. View who proposed you
        3. View whom you proposed
        4. Show matches
        5. Logout ''')
        if user_input=='1':
            self.view_all_users()
        elif user_input=='2':
            self.view_proposal()
        elif user_input=='3':
            self.view_proposed()
        elif user_input=='4':
            self.view_matches()
        else:
            self.logout()

    def register(self):
        name=input('What is your name? ')
        email=input('What is your email? ')
        password=input('What will be your password? ')
        gender=input('What is your gender? ')
        city=input('Where do you live? ')

        query='''insert into `users` (`user_id`,`name`,`email`,`password`,`gender`,`city`) 
        values (NULL,'{}','{}','{}','{}','{}')'''.format(name,email,password,gender,city)
        self.mycursor.execute(query)
        self.conn.commit()
        print('Registered')
        self.program_menu()

    def login(self):
        email=input('enter email id ')
        password=input('enter the password ')

        query = '''select * from `users` where `email` like '{}' and `password` like '{}' '''.format(email, password)
        self.mycursor.execute(query)
        lst=self.mycursor.fetchall()
        if len(lst)==1:
            print('welcome')
            self.current_user_id=lst[0][0]
            self.is_logged_in=1
            self.user_menu()
        else:
            print('incorrect login')
        self.program_menu()

    def updatepass(self):
        name=input('Enter your name ')
        email=input('Enter your email ')
        query = '''select * from `users` where `email` like '{}' and `name` like '{}' '''.format(email, name)
        self.mycursor.execute(query)
        lst = self.mycursor.fetchall()
        if len(lst)==0:
            print('Incorrect credentials')
        else:
            newpass=input('Enter new password ')
            query2='''update `users` set `password`='{}' where `users`.`email`='{}' '''.format(newpass,email)
            self.mycursor.execute(query2)
            self.conn.commit()
            print('Password successfully updated')
        self.program_menu()

    def view_all_users(self):
        query = '''select * from `users` where `user_id` not like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        all_user_list=self.mycursor.fetchall()
        for i in all_user_list:
            print('-------------------------------------------------')
            print(i[0],'|',i[1],'|',i[4],'|',i[5])
            print('-------------------------------------------------')
        x=input('Do you want to propose any user?(y/n) ')
        if x=='y':
            self.proposed_user_id=input('Enter the id of the user whom you want to propose ')
            self.propose()
        else:
            self.user_menu()

    def propose(self):
        query='''insert into `proposal` (`proposal_id`,`romeo_id`,`juliet_id`)
        values
        (NULL,'{}','{}')'''.format(self.current_user_id,self.proposed_user_id)
        self.mycursor.execute(query)
        self.conn.commit()
        print('Proposal sent successfully')
        self.user_menu()

    def view_proposed(self):
        query='''select * from `proposal` p join `users` u
        on p.`juliet_id`=u.`user_id` where p.`romeo_id` like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst=self.mycursor.fetchall()
        for i in proposed_lst:
            print('-------------------------------------------------')
            print(i[4],'|',i[7],'|',i[8])
            print('-------------------------------------------------')
        self.user_menu()

    def view_proposal(self):
        query = '''select * from `proposal` p join `users` u
                on p.`romeo_id`=u.`user_id` where p.`juliet_id` like '{}' '''.format(self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst = self.mycursor.fetchall()
        for i in proposed_lst:
            print('-------------------------------------------------')
            print(i[4], '|', i[7], '|', i[8])
            print('-------------------------------------------------')
        self.user_menu()

    def view_matches(self):
        query='''select * from `proposal` p join `users` u on u.`user_id`=p.`juliet_id` 
        where `romeo_id`='{}' and `juliet_id`=(select `romeo_id` from `proposal` where `juliet_id`='{}')'''.format(self.current_user_id,self.current_user_id)
        self.mycursor.execute(query)
        proposed_lst = self.mycursor.fetchall()
        for i in proposed_lst:
            print('-------------------------------------------------')
            print(i[4], '|', i[7], '|', i[8])
            print('-------------------------------------------------')
        self.user_menu()

    def logout(self):
        self.is_logged_in=0
        self.program_menu()

obj1=Soulmet()