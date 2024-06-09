#!/usr/bin/env python
# coding: utf-8

# ## Feature list
# 
# -SignUp
# 
#     -Username    
#     -Password    
#         -Chech Stength        
#     -2 Security Question . or Backup Codes    
#     -Two-Factor Authentication    
#     -Backup codes    
#     -Name,Phone,Email Id   
#         - check phone no.
#         - check email
# -SignIn
# 
#     -Username/Email    
#     -Password    
#         -Forget password
#         -Reset password
#         -Security Question Answers update

# In[1]:


db = {'username':['pass',['name','phone','email'],['ans1','ans2'],['bc1','bc2','bc3','bc4']]}


# In[2]:


def usernameCheck():
    pass


# In[3]:


import random as r


# In[4]:


def passSuggest():
    import random as r
    alphaLower = 'abcdefghijklmnopqrstuvwxyz'
    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit      = '0123456789'
    specChar   = '!@#$%^&*_-+=<>'
    
    count = [r.choice(range(2, 6)) for i in range(4)] 
    al3   = [r.choice(alphaLower)    for i in range(count[0])]
    au3   = [r.choice(alphaUpper)    for i in range(count[1])]
    d3    = [r.choice(digit)         for i in range(count[2])]
    s3    = [r.choice(specChar)      for i in range(count[3])]
    
    l = []
    for li in [al3, au3, d3, s3]:
        l.extend(li)
    r.shuffle(l)
    s = ''.join(l)
    return s


# In[5]:


def checkPasswordStength(password):
    while True:
        specChar = '!@#$%^&*_-+=<>'
        ac = uc = lc = dc = sc = 0
        strength = 0
        if len(password)>=8:
            for char in password:
                if char.isalpha():
                    ac += 1
                    if char.isupper(): uc += 1
                    else             : lc += 1
                elif char.isdigit()  : dc += 1
                elif char in specChar: sc += 1
        
            if ac > 0 and dc > 0     : strength += 1
            else                     : print('Combination of alpha and digit is a must')
            
            if uc > 0 and lc > 0     : strength += 1 
            else                     : print('Combination of alpha and digit is a must')
            
            if sc > 0                : strength += 1
            else                     : print('Special Character is a must')
            
            if strength == 3:
                print('password is strong')
                return password
            else:
                e = 1
        else:
            print('password should be atleast 8 characters')
            e = 1
        
        if e == 1:
                password = passSuggest()
                print(f'''Password not strong. Suggested password is {password}
                    press 0 to Exit
                    or''')
                password = input('please enter a strong password again:')
                if password == '0': return 0 


# In[6]:


def checkEmail():
    pass


# In[7]:


def takeDetails(username):
    name = input('Enter name:').title()
    while True:
        phone = input('Enter 10-digit phone number: ')
        if len(phone) != 10: print('Invalid phone...')
        else: break
    email = input('Enter email address:').lower()
    checkEmail()
    l= [name, phone, email]
    db[username].append(l)
    return


# In[8]:


def secQuestion(username):
    questionDb = ['Your first school ?','your first crush name ?']
    ans1 = input(f'Question: {questionDb[0]}').lower()
    ans2 = input(f'Question: {questionDb[1]}').lower()
    ansList = [ans1,ans2]
    db[username].append(ansList)
    return   


# In[9]:


def generateBackupCodes(username):
    import random as r
    backupList = [r.randint(10000, 99999)for i in range (4)]
    print(f"Your backup code are {backupList}, please don't share with anyone")
    db[username].append(backupList)
    return


# In[10]:


def SignUp():
    print('************** Welcome to SignUp Portal ****************')
    first = 1
    while True:
        username = input('Enter a new username: ').lower()
        if username == '0'and first == 0:
            print('SignUp failed....')
            return
        if username not in db:
            password = input('Enter a strong password: ')
            password = checkPasswordStength(password)
            if password == 0:
                print('SignUp failed....')
                return
            db[username]=[password]
            takeDetails(username)
            secQuestion(username)
            generateBackupCodes(username)
            print('SignUp Sucessful_ _ _')
            return
        else:
            print('''Username already taken. please try again ...
            Press 0 to Exit
            Or''')
            first = 0


# In[18]:


def forgotpassword(username):
    print("************** Security Question **************")
    que = ("Q1. your first school name ?","Q2. Enter your first crush name ?")
    print(que[0])
    ans1  = input("Enter ans : ").lower()
    print(que[1])
    ans2  = input("Enter ans : ").lower()
    sqc = db[username]
    if ans1 == sqc[2][0] or ans2 == sqc[2][1]:
        new_password = input('''Enter new password : ''')
        db[username][0] = new_password
        print("************ Password update Successfully *************")
    else :
        print("************ Your Security Answer's are incorrect ************")


# In[19]:


def singhInBackCode(username):
    sqc = db[username]
    sqc1 = sqc[3]  
    code = input('''Enter 4 digit security code : ''')
    if code in sqc1:
        print("********** login Successful ************")
        db[username][3].remove(code)
    else :
        print('''You do not have any backup code
        to generate backup code press 5''')
        bcode = input()
        if bcode == "5":
            generateBackupCodes(username)
        else:
            print("********** Login Failed **********")
            return
    if code == "0":
        print("********** Login Failed **********")
        return
    else:
        print(''' Enter correct Security Code
                To exit press 0
                or
                ''')


# In[20]:


def SignIn():
    print('************** Welcome to SignIn Portal **************')
    while True:
        username = input('Enter an existing username:').lower()
        if username == '0':
            print('SignIn failed')
            return
        if username == '1': SignUp()
        if username in db:
            for i in range(3): 
                password = input('Enter your Password: ')
                if password =="0": break
                if password =='1': singhInBackCode(username)
                else             : return          
                if password =='2': forgotpassword(username)
                else             : return
                if password == db[username][0]:
                    print('signIn Successful....')
                    return
                else:
                    print('''Wrong password. Please try again...
                    Press 1 to SignIn using BackUp code
                    Press 2 to Forgot Password
                    Press 0 to Exit
                    or''')
#             fp = input('''SignIn Failed...
#                           Press 1 to Forgot Password
#                           Press any key to Exit''')
#             if fp =='1': forgotPassword(username)
#             else       :return
    
        else:
            print('''Username not registered. Please try again
            Press 1 to SignUp for a new account
            Press 0 to Exit
            or''')        


# In[21]:


while True:   
    mode = input(''' Welcome to Authentication System
    Enter choice:
    press 1 to SignUp
    press 2 to SignIn
    Press 0 to Exit
    :''')
    if  mode == '1':
        print('SignUp....')
        SignUp()
    elif mode == '2':
        print('SignIn....')
        SignIn()
    elif mode == '0':
        print('Thank you for visiting our website.....')
        break
    else:
        print('Enter valid mode')
        
    


# In[17]:


db


# In[ ]:





# In[ ]:





# In[ ]:




