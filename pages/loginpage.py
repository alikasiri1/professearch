import streamlit as st
from streamlit_custom_notification_box import custom_notification_box
import webbrowser
from database import sign_up, fetch_users ,update_user
import streamlit_authenticator as stauth
from datetime import date
from streamlit_javascript import st_javascript
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)

# from streamlit_chat import message
# real_url = "http://localhost:8501/"
real_url = "https://professearch.streamlit.app/"
import streamlit.components.v1 as com
# from zibal import zibal
st.set_page_config(page_title="profesearc/login page",layout="wide", page_icon=None, menu_items=None , initial_sidebar_state="expanded") # layout="wide"
import zibal.zibal as zibal

users = fetch_users()
emails = []
usernames = []
passwords = []
track_i = []
payments = []
num_search=[]
date_joined = []
date_payment = []
print(users)
for user in users:
    print("-")
    emails.append(user['key'])
    usernames.append(user['username'])
    passwords.append(user['password'])
    track_i.append(user["track_id"])
    payments.append(user["payment"])
    num_search.append(user["num_search"])
    date_joined.append(user["date_joined"])
    date_payment.append(user["date_payment"])

credentials = {'usernames': {}}
for index in range(len(emails)):
    credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

Authenticator = stauth.Authenticate(credentials , cookie_name='Streamlit', key='abcdef')#, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4
# Authenticator._check_cookie()

email, authentication_status, username = Authenticator.login(':green[Login]', 'main')
stt = st.empty()
stt2 = st.empty()
stt.markdown(f"""<a href="{real_url}singup"   target = "_self" style="text-decoration: none;">create acount</a> """ , unsafe_allow_html=True)
# st.markdown("""<a href="https://emailverify.streamlit.app/singup"   target = "_self">create acount</a> """ , unsafe_allow_html=True)
# stt2.markdown(f"""<a href="{real_url}verify"   target = "_self">verify</a> """ , unsafe_allow_html=True)

print(email)
print(username)

# info, info1 = st.columns(2)  block-container

if authentication_status == False:
    no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
        div[data-testid="block-container"] {
            padding-left: 0px;
            padding-right: 0px;
            width: 60%;
        }
        header[data-testid="stHeader"] {display: none;}
        footer{
            display: none;
        }
    </style>
        """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    st.error("Username/password is incorrect")

elif authentication_status == None:
    no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {
            display: none;
            
        }
        div[data-testid="block-container"] {
            padding-left: 0px;
            padding-right: 0px;
            width: 60%;
        }
        header[data-testid="stHeader"] {display: none;}
        footer{
            display: none;
        }
    </style>
        """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    st.warning("Please enter your username and password")

if authentication_status:
    stt.empty()
    stt2.empty()
   
    if "conversation" not in st.session_state:
        st.session_state["conversation"] = ''
    if "querys" not in st.session_state:
        st.session_state["querys"] = ''

    def res(input , rol):
        if rol == "assistant":
            return f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link href="/your-path-to-uicons/css/uicons-[your-style].css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            <div class="card" style="border: 0px;background-color: #343541;padding-left: 13%;padding-right: 13%;color:white;">
                <div class="card-body" style="display: flex;">
                    <div style="width: 35px;height: 35px;background-color:#1abc9c;color: white;border-radius: 1px;text-align: center;padding-top: 5px;margin-right: 5px;">
                        {username[:2].upper()}
                    </div>
                    <p style="color: white;margin-bottom: 0px;flex-grow: 1;padding: 5px">{input}</p>
                </div>
            </div>
            <script>
            var paragraf = document.getElementsByTagName("p")
            paragraf.addClass("card-text")
            var h5_ = document.getElementsByTagName("h5")
            h5_.addClass("card-title")
            </script>
        """
        else: #class="card"
            return f"""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            <style>
                li p {{
                    font-size: 22px; /* 1.5 times the parent font size */
                    }}
                li::marker{{
                    font-size: 20px;
                }}
                ol{{
                    padding-left: 10px;
                }}
            </style>
            <div class="card" style="background-color: #3f414d;padding-left: 13%;padding-right: 13%;color:white;">
                <div class="card-body">
                    <div style="width: 35px;height: 35px;border-radius: 1px;background-color: #19c37d;color: white;">
                        <svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img" style="width: 35px;height: 30px;padding-top: 5px;"><text x="-9999" y="-9999">ChatGPT</text>
                        <path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg>
                    </div>
                    <p style="color: white;margin-bottom: 0px;flex-grow: 1;padding: 10px">{input}</p>
                </div>
            </div>
            <script>
            var paragraf = document.getElementsByTagName("p")
            paragraf.addClass("card-text")
            var h5_ = document.getElementsByTagName("h5")
            h5_.addClass("card-title")
            </script>
        """

    main_html = f"""
    <html>
        <head>
            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        </head>
        <body>
            <div class="clear"></div>
            <nav>
                <div class="site-title">Finland</div>
                <ul>
                    <li><a href="{real_url}pricing?{email}" target = "_self"  >Pricing</a></li>
                    <li><a href="/events">Events</a></li>
                    <li><a href="/contact">Contact</a></li>
                <ul>
            </nav>
            <script>
                $(window).scroll(function(){{
                if ($(window).scrollTop() >= 300) {{
                    $('nav').addClass('fixed-header');
                    $('nav div').addClass('visible-title');
                }}
                else {{
                    $('nav').removeClass('fixed-header');
                    $('nav div').removeClass('visible-title');
                }}
            }});
            </script>
        </body>
    </html>
    """
    style_css = """
    header.css-18ni7ap.ezrtsby2{
        visibility: hidden;

    }

    div.block-container.css-z5fcl4.ea3mdgi4
    {
        padding-top: 0px;
        padding-left: 0px;
        padding-right: 0px;

    }
    /* resets */
    body { margin:0px; padding:0px; }

    /* main */
    header {
        height: 360px;
        z-index: 10;
    }

    header h1 {
        background-color: rgba(18,72,120, 0.8);
        color: #fff;
        padding: 0 1rem;
        position: absolute;
        top: 2rem; 
        left: 2rem;
    }

    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%; 
    }

    nav {
        width: 100%;
        height: 60px;
        background: #292f36;
        postion: unset;
        z-index: 10;
    }

    nav div {
        color: white;
        font-size: 2rem;
        line-height: 60px;
        position: absolute;
        top: 0;
        left: 2%;
        visibility: hidden;
    }
    .visible-title {
        visibility: visible;
    }

    nav ul { 
        list-style-type: none;
        margin: 0 2% auto 0;
        padding-left: 0;
        text-align: right;
        max-width: 100%;
    }
    nav ul li { 
        display: inline-block; 
        line-height: 60px;
        margin-left: 10px;
    }
    nav ul li a {
        text-decoration: none; 
        color: #a9abae;
    }

    /* demo content */
    body { 
        color: #292f36;
        font-family: helvetica;
        line-height: 1.6;
    }
    .content{ 
        margin: 0 auto;
        padding: 4rem 0;
        width: 960px;
        max-width: 100%;
    }
    article {
        float: left;
        width: 720px;
    }
    article p:first-of-type {
        margin-top: 0;
    }
    aside {
        float: right;
        width: 120px;
    }
    p img {
        max-width: 100%;
    }

    @media only screen and (max-width: 960px) {
        .content{ 
            padding: 2rem 0;
        }
        article {
            float: none;
            margin: 0 auto;
            width: 96%;
        }
        article:last-of-type {  
            margin-bottom: 3rem;
        }
        aside {  
            float: none;
            text-align: center;
            width: 100%;
        }
    }


    """

        # com.html(main_html , height=360)

    st.sidebar.subheader(f'Welcome {username}')
    n_search = ''
    trackid = 0
    payment = 0
    date_j = ''
    date_pay = ''
    for i in range(len(emails)):
        if emails[i] == email:
            trackid = track_i[i]
            payment = payments[i]
            n_search = num_search[i]
            date_j = str(date_joined[i])
            date_pay = str(date_payment[i])
            break
    
    if trackid != 0 and payment < 10:
        merchant_id = 'zibal'
        callback_url = f'{real_url}verify.py'
        zb = zibal.zibal(merchant_id, callback_url)
        verify_zibal = zb.verify(trackid)
        if verify_zibal["result"] == 100 or verify_zibal["result"] == 201:
            data = {}
            data['merchant'] = 'zibal'
            data['trackId'] =   trackid
            update_user(st.session_state['name'], {"payment" : payment*100000})
            update_user(st.session_state['name'], {"date_payment" : zb.postTo("inquiry" , data )["verifiedAt"]})
            
            if payment == 5:
                update_user(st.session_state['name'], {"num_search" : 200})
            elif payment == 8:
                update_user(st.session_state['name'], {"num_search" : 350})

            payment = payment * 100000
            date_pay = zb.postTo("inquiry" , data )["verifiedAt"]
    

    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """##202123  
    st.markdown(no_sidebar_style, unsafe_allow_html=True)#background-color: #5a5656;
            # div[data-testid="block-container"]{{
            #     border: 1px solid #ccc;
            # }}
    html= f"""
        <style>
            div[data-testid="stMarkdownContainer"] h3 {{
                color: white;
            }}
            section[data-testid="stSidebar"] {{
             background-color: #202123;
             color: white;
             top: 0px;
            }}
            div[data-testid="collapsedControl"]{{
                color : white;
            }}
            [data-testid="stAppViewContainer"] > .main {{  
                background-color: #343541;
            }}
            header.css-18ni7ap.ezrtsby2{{
                visibility: hidden;
            }}
            div.stChatFloatingInputContainer.css-90vs21.e1d2x3se2{{
                background-color: #343541;
                padding-bottom: 50px;
                padding-top: 8px;

            }}
            div.block-container.css-z5fcl4.ea3mdgi4
            {{
                padding-top: 0px;
                padding-bottom: 135px;

            }}
            div[data-testid="block-container"]{{
                padding-left: 0px;
                padding-right: 3px;
            }}
            div[data-testid="stSpinner"]{{
                bottom: 500px;
                position: flex;
            }}
            footer{{
                
                    padding-top: 0px;
                    padding-bottom: 0px;
                    height: 0px;
                    visibility: hidden;
                }}

        </style>
    """

    st.markdown(html, unsafe_allow_html=True)
    from utils import *
    question = st.chat_input("Send a Massage ..." , max_chars=300 )
    
    today = str(date.today())
    print(today)

    if payment == 0 :
        if  ( (int(today.split("-")[1]) > int(date_j.split(" ")[0].split("-")[1]) ) and (int(today.split("-")[2]) == int(date_j.split(" ")[0].split("-")[2]) ) ) or ( ( int(today.split("-")[0]) > int(date_j.split(" ")[0].split("-")[0]) ) and (int(today.split("-")[2]) == int(date_j.split(" ")[0].split("-")[2]) ) ):
            payment = -1
            update_user(email , {"payment" : -1})
        else:
            if n_search.split("&&")[0] == today:
                if int(n_search.split("&&")[1]) < 3:
                    payment = 150
                else:
                    payment = 50
            else:    
                update_user(email , {"num_search" : f"{today}&&0"})
                print("day changed")
                payment = 150
    elif payment > 10000:
        if  ( (int(today.split("-")[1]) > int(date_pay.split("T")[0].split("-")[1]) ) and (int(today.split("-")[2]) == int(date_pay.split("T")[0].split("-")[2]) ) ) or ( ( int(today.split("-")[0]) > int(date_pay.split("T")[0].split("-")[0]) ) and (int(today.split("-")[2]) == int(date_pay.split("T")[0].split("-")[2]) ) ):
            payment = -2
            update_user(email , {"payment" : -2})
        elif n_search == 0 :
            payment = -2

    persent = 0
    numper_pay = 0
    if payment == 500000:
        numper_pay = 200
        persent = ((numper_pay - n_search) / numper_pay) * 100
    elif payment == 800000:
        numper_pay = 350
        persent = ((numper_pay - n_search) / numper_pay) * 100

    
    print(persent)


    if payment > 1000:
        usage_html = f"""
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    .progress-container {{
                        width: 100%;
                        background-color: #f0f0f0;
                        border: 1px solid #ccc;
                        padding: 3px;
                        border-radius: 3px;
                    }}

                    .progress-bar {{
                        width: {persent}%; /* Adjust the width to set the progress percentage */
                        height: 20px;
                        background-color: #4CAF50;
                        text-align: center;
                        line-height: 30px;
                        color: white;
                        border-radius: 3px;
                    }}
                    button[data-testid="baseButton-secondary"]{{
                        color: black;
                    }}
                </style>
            </head>
            <body>
                <div>
                    <a href="{real_url}pricing?{email}" target = "_blank"  >Pricing</a></li>
                </div>
                <h1 style="color: white;">Usage</h1>
                <div class="progress-container">
                    <div class="progress-bar" style="background-color: #4CAF50;"></div>
                </div>
                <div>{numper_pay - n_search}/{numper_pay}</div>
            </body>
            """
    else:
        usage_html = f"""
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                button[data-testid="baseButton-secondary"]{{
                    color: black;
                }}
                a{{
                    background-color: #202123;
                }}
                a:hover{{
                    background-color: #42464f;
                    color: red;
                }}
                li{{
                    margin-left: 0px;padding-left: 0px;
                }}
            </style>
        </head>
        <body>
            <div>
                <ul style="list-style: none;">
                    <li style="margin-left: 0px;padding-left: 0px;">
                        <a href="{real_url}pricing?{email}"  target = "_self" style="display: flex;text-decoration: none;" >
                            <p style="color: white;margin-bottom: 0px;flex-grow: 1;padding: 5px">Upgrade to Plus</p>
                        <a>
                    </li>
                    <li style="margin-left: 0px;padding-left: 0px;">
                        <a style="display: flex;text-decoration: none;" >
                            <div style="width: 35px;height: 35px;background-color:#1abc9c;color: white;border-radius: 1px;text-align: center;padding-top: 5px;margin-right: 5px;">
                                {username[:2].upper()}
                            </div>
                            <p style="color: white;margin-bottom: 0px;flex-grow: 1;padding: 5px">{email}</p>
                        <a>
                    </li>
                </ul>
            </div>
        </body>
        """

    st.sidebar.markdown(usage_html,unsafe_allow_html=True)
    Authenticator.logout('Log Out', 'sidebar')
    print("n_search",n_search)
    print("payment",payment)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # payment = 150
    if question:
        if payment == 150:

            # for message in st.session_state.messages:
            #     st.markdown(res(message["content"],message["role"]),unsafe_allow_html=True)
            # # st.session_state["querys"] = st.session_state["querys"] + "==" + question

            # refined_query = query_refiner_2(question)
            # context = find_match(refined_query)
            # prompt = f"""your task is helping a user to find appropriate a list of professors interested in the specified research area . just anser based Text.\n\n Text:\n```{context}``` \n\n user request:\n ```{refined_query}```"""
            # #--------------------------------------
            # st.session_state.messages.append({"role": "assistant", "content": question})
            # st.markdown(res(refined_query,"assistant"),unsafe_allow_html=True)
            # # st.markdown(res(context,"user"),unsafe_allow_html=True)
            # response = get_completion(prompt)
            # print("-----------------------------------------------------------------------------------")
            # print(response.choices[0].message["content"])
            # st.session_state.messages.append({"role": "user", "content": response.choices[0].message["content"]})
            # st.markdown(res(response.choices[0].message["content"],"user"),unsafe_allow_html=True)


                # st.session_state["conversation"] = st.session_state["conversation"] +"=="+ context
                # for i in range(len(st.session_state["conversation"].split("=="))):
                #     if st.session_state["querys"].split("==")[i] != "":
                #         with st.chat_message(username):
                #             st.markdown(st.session_state["querys"].split("==")[i] )
                #         with st.chat_message("robot"):
                #             st.markdown(st.session_state["conversation"].split("==")[i])
                          # st.markdown(res(st.session_state["querys"].split("==")[i]) , unsafe_allow_html=True)
                #         # st.markdown(res(st.session_state["conversation"].split("==")[i]) , unsafe_allow_html=True)

            for message in st.session_state.messages:
                st.markdown(res(message["content"],message["role"]),unsafe_allow_html=True)

            with st.spinner(":green[typing...]"):
                refined_query = query_refiner_2(question)
                st.session_state.messages.append({"role": "assistant", "content": question})
                st.markdown(res(refined_query,"assistant"),unsafe_allow_html=True)

            with st.spinner(":green[typing...]"):
                context = find_match(refined_query)
                prompt = f"""your task is helping a user to find appropriate a list of professors interested in the specified research area . just anser based Text.\n\n Text:\n```{context}``` \n\n user request:\n ```{refined_query}```"""
                #--------------------------------------
                response = get_completion(prompt)
                print("-----------------------------------------------------------------------------------")
                print(response.choices[0].message["content"])
                st.session_state.messages.append({"role": "user", "content": response.choices[0].message["content"]})
                st.markdown(res(response.choices[0].message["content"],"user"),unsafe_allow_html=True)

            update_user(email, {"num_search" :f"""{today}&&{int(n_search.split("&&")[1])+1}"""})

        elif payment >10000:
            for message in st.session_state.messages:
                st.markdown(res(message["content"],message["role"]),unsafe_allow_html=True)

            with st.spinner(":green[typing...]"):
                refined_query = query_refiner_2(question)
                st.session_state.messages.append({"role": "assistant", "content": question})
                st.markdown(res(refined_query,"assistant"),unsafe_allow_html=True)

            with st.spinner(":green[typing...]"):
                context = find_match(refined_query)
                prompt = f"""your task is helping a user to find appropriate a list of professors interested in the specified research area . just anser based Text.\n\n Text:\n```{context}``` \n\n user request:\n ```{refined_query}```"""
                #--------------------------------------
                response = get_completion(prompt)
                print("-----------------------------------------------------------------------------------")
                print(response.choices[0].message["content"])
                st.session_state.messages.append({"role": "user", "content": response.choices[0].message["content"]})
                st.markdown(res(response.choices[0].message["content"],"user"),unsafe_allow_html=True)
       
            update_user(email, {"num_search" : n_search - 1 })

        elif payment == 50:
            st.warning("you used your 3 search today in free trial")
        elif payment == -1 :
            styles ={
            'material-icons':{'color': 'red'},
            'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}
            }
            custom_notification_box(icon='info', textDisplay='you finished your 1 mouns free trial. you must upgrade your account', externalLink='pricing', url=f'{real_url}pricing?{email}', styles=styles, key="foo")
        elif payment == -2:
            st.error("you finished your trial")
        else:
            styles ={
            'material-icons':{'color': 'red'},
            'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}
            }
            custom_notification_box(icon='info', textDisplay='you must upgrade your account', externalLink='pricing', url=f'{real_url}pricing?{email}', styles=styles, key="foo")
