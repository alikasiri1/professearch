import streamlit as st
import streamlit_authenticator as stauth
import datetime
from datetime import date
import re
from deta import Deta
from verify_email import verify_email
import nest_asyncio

DATA_KEY =st.secrets["database_key"]
deta = Deta(DATA_KEY)

db = deta.Base("singin")

def insert_user(email, username, password):
    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:
    """
    date_joined = str(datetime.datetime.now())
    date_j = date_joined.split(" ")[0]

    return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined , 'payment':0 , 'track_id' : 0, 'date_payment' : '0' , 'num_search':f"{date_j}&&0"})

def update_user2(email , payment):
    try:
        users = db.fetch()
    except:
        users = db.fetch()
    dic = {}
    for i in range(len(users.items)):
        if users.items[i]["key"] == email:
            dic["key"] = email
            dic["username"] = users.items[i]["username"]
            dic["password"] = users.items[i]["password"]
            dic["date_joined"] = users.items[i]["date_joined"]
            dic["payment"] = payment
            db.delete(email)
            # del users.items[i]
            break
    # users.items.append(dic)
    return db.insert(dic)

    # return db.update( updates= dic, key= email)

# @st.cache_resource
# @st.cache(allow_output_mutation=True)
def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items

# print(fetch_users())
# @st.cache_resource
def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails

# @st.cache_resource
def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['username'])
    return usernames

def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return db.update(updates, username)

def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return db.delete(username)

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False

def verify_em(email):
    nest_asyncio.apply()
    return verify_email(email)
    # return email


def sign_up():
    with st.form(key='signup'): #, clear_on_submit=True
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
        password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')
        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            sing = st.form_submit_button('Sign Up')

    if sing:
        with st.spinner("verifying ..."):
            if email:
                print(email)
                if verify_em(email):
                    if email not in get_user_emails():
                        if validate_username(username):
                            if username not in get_usernames():
                                if len(username) >= 2:
                                    if len(password1) >= 6:
                                        if password1 == password2:
                                            # Add User to DB
                                            hashed_password = stauth.Hasher([password2]).generate()
                                            insert_user(email, username, hashed_password[0] , )
                                            st.success('Account created successfully!!')
                                            st.balloons()

                                        else:
                                            st.warning('Passwords Do Not Match')
                                    else:
                                        st.warning('Password is too Short')
                                else:
                                    st.warning('Username Too short')
                            else:
                                st.warning('Username Already Exists')
                        else:
                            st.warning('Invalid Username')
                    else:
                        st.warning('Email Already exists!!')
                else:
                    st.warning("Email dos not exist")

    

# def login():
#     users = fetch_users()
#     emails = []
#     usernames = []
#     passwords = []

#     for user in users:
#         emails.append(user['key'])
#         usernames.append(user['username'])
#         passwords.append(user['password'])
#     with st.form("login"):
#         st.subheader(":green[login]")
#         username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
#         password = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
#         btn1, bt2, btn3, btn4, btn5 = st.columns(5)

#         with btn3:
#             bot = st.form_submit_button('login')
#         # with btn5:
#             # singup = st.form_submit_button("sing up")
#             # if singup:
#             #     singup()
#         if bot:
#             if username:
#                 if password:
#                     for i in range(len(emails)):
#                         if username == usernames[i] and password == passwords[i]:
#                             print(username , password)

#                             return username
#                     st.error('Invalid Username or Password')
#                 else:
#                     st.warning('Please enter Password')
#             else:
#                 st.warning('Please enter Username ')



