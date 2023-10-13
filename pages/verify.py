import zibal.zibal as zibal
# from pages.loginpage import email ,username 
from database import  fetch_users ,update_user
import streamlit as st
import streamlit_authenticator as stauth
import datetime
# real_url = "http://localhost:8501/"
real_url = "https://profesearch.streamlit.app/"
no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
        header[data-testid="stHeader"] {display: none;}
        footer{
            display: none;
        }
    </style>
            """
st.markdown(no_sidebar_style, unsafe_allow_html=True)

users = fetch_users()
emails = []
usernames = []
passwords = []
track_i = []
payments = []
for user in users:
    emails.append(user['key'])
    usernames.append(user['username'])
    passwords.append(user['password'])
    track_i.append(user["track_id"])
    payments.append(user["payment"])

credentials = {'usernames': {}}
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

Authenticator = stauth.Authenticate(credentials , cookie_name='Streamlit', key='abcdef')#, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4
Authenticator._check_cookie()

if 'name' in st.session_state:
    if st.session_state['name']:
        print(st.session_state['name'] , "didi")
        # st.write(st.session_state['name'])
        payment = 0
        track_id = 0
        for i in range(len(emails)):
            if st.session_state['name'] == emails[i]:
                track_id = track_i[i]
                payment = payments[i]

        # print(email , username)
        # st.write(email)
        merchant_id = 'zibal'
        callback_url = f'{real_url}verify.py'
        zb = zibal.zibal(merchant_id, callback_url)

        verify_zibal = zb.verify(track_id)
        print(verify_zibal)
        # st.write(verify_zibal) 
        if verify_zibal["result"] == 100 or verify_zibal["result"] == 201:
            update_user(st.session_state['name'], {"payment" : payment*100000})
            
            if payment == 5:
                update_user(st.session_state['name'], {"num_search" : 200})
            elif payment == 8:
                update_user(st.session_state['name'], {"num_search" : 350})
            
            data = {}
            data['merchant'] = 'zibal'
            data['trackId'] =   track_id
            print(zb.postTo("inquiry" , data )["verifiedAt"])
            update_user(st.session_state['name'], {"date_payment" : zb.postTo("inquiry" , data )["verifiedAt"]})
            # date_pae = str()
            st.success(zb.verify_result(verify_zibal["result"]))
            st.markdown(f"""<a href="{real_url}loginpage"   target = "_self"> login</a> """ , unsafe_allow_html=True)
            #st.markdown("""<a href="https://emailverify.streamlit.app/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
        else:
            st.error(zb.verify_result(verify_zibal["result"]))
    else:
        print("false name" , st.session_state['name'])


# verify_result = verify_zibal['result']
# if 'refNumber' in verify_zibal:
#     ref_number = verify_zibal['refNumber']
#     print(ref_number)

# verify_result_code = verify_result

# print(zb.verify_result(verify_result_code))