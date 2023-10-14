import streamlit as st
import streamlit.components.v1 as com
from requests import request
import streamlit_authenticator as stauth
from database import  fetch_users ,update_user
from streamlit_javascript import st_javascript
import zibal.zibal as zibal
import webbrowser
st.set_page_config(page_title="profesearc/login page", page_icon=None, layout="wide", menu_items=None)
# real_url = "http://localhost:8501/"
real_url = "https://professearch.streamlit.app/"
pay1 = "200000"
pay2 = "500000"
pay3 = "800000"
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

print("----------------------------------------------")

url = str(st_javascript("window.location.href"))

if len(url.split("%"))>3:
  if 'name' in st.session_state:
    if st.session_state['name']:
       print(st.session_state['name'])
       print(st.session_state['username'])
    else:
       print("false name" , st.session_state['name'])
  print(url.split("%")[-3][2:])
  pay = url.split("%")[-3][2:]
  user = url.split("%")[-2][2:] + "@" +url.split("%")[-1][2:]
  print(user)
  print(url)
  merchant_id =  'zibal'
  callback_url = f'{real_url}verify'
  zb = zibal.zibal(merchant_id, callback_url)
  main_html = f"""
<html>
<head>
  <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>    <meta charset="UTF-8">
</head>
  <body>
  <header >
     <nav style="background-color: #007acc;position: fixed;top: 0px;width: 100%;z-index: 1000;"> 
        <a class="navbar-brand" href="#" style="position: absolute;color: #fff;padding-top: 11px;font-size: x-large;margin-left: 10px;">
          <svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img" style="width: 35px;height: 35px;margin-left: 1%;margin-right: 5%;"><text>ChatGPT</text>
          <path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg> 
          profesearch
        </a>
        <ul>
            <li style="margin-left: 0px;padding-top: 15px;"><a style="text-decoration: none; color: #fff;" href="{real_url}loginpage">login</a></li>
            <li style="margin-left: 0px;padding-top: 15px;"><a style="text-decoration: none; color: #fff;"href="#">about</a></li>
        <ul>
    </nav>
  </header>
    <div class="background">
        <div class="container">
            <div class="panel pricing-table">
                <div class="pricing-plan">
                  <img src="https://s22.postimg.cc/8mv5gn7w1/paper-plane.png" alt="" class="pricing-img">
                  <h2 class="pricing-header">Free trial</h2>
                  <ul class="pricing-features" style="list-style: none;">
                  <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">one month Free trial</li>
                  <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">3 search in a day</li>
                  </ul>
                  <span class="pricing-price">Free</span>
                  <a href="#"class= "pricing-button"  target = "_self" style="text-decoration: none;" >Free trial</a>
                </div>
                <div class="pricing-plan">
                    <img src="https://s28.postimg.cc/ju5bnc3x9/plane.png" alt="" class="pricing-img">
                    <h2 class="pricing-header">Small team</h2>
                    <ul class="pricing-features" style="list-style: none;">
                    <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">one mounth trial</li>
                    <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">200 search</li>
                    </ul>
                    <span class="pricing-price">50000t</span>
                    <a href="{real_url}pricing?500000?{user}" class="pricing-button is-featured"  target = "_self" style="text-decoration: none;">BUY</a>
                </div>
                <br>
                <div class="pricing-plan">
                    <img src="https://s21.postimg.cc/tpm0cge4n/space-ship.png" alt="" class="pricing-img">
                    <h2 class="pricing-header">Enterprise</h2>
                    <ul class="pricing-features" style="list-style: none;">
                    <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">one mounth trial</li>
                    <li class="pricing-features-item" style="margin-left: 0px;padding-left: 0px;margin-bottom: 3px;">350 search</li>
                    </ul>
                    <span class="pricing-price">80000t</span>
                    <a href="{real_url}pricing?800000?{user}" class="pricing-button"  target = "_self" style="text-decoration: none;">BUY</a>
                </div>
            </div>
        </div>
    </div>
</html>
  """
  css = """
    footer{
    display: none;
  }
  div[data-testid="block-container"] {
      padding-left: 0px;
      padding-right: 0px;
  }
  div.block-container.css-z5fcl4.ea3mdgi4
  {
      padding: 0px;
  }
  body { margin:0px; padding:0px; }
  html {
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
  }

  *, *:before, *:after {
    box-sizing: inherit;
  }

  .background {
    padding: 0 25px 25px;
    position: relative;
    width: 100%;
  }

  .background::after {
    content: '';
    background: #60a9ff;
    background: -moz-linear-gradient(top, #60a9ff 0%, #4394f4 100%);
    background: -webkit-linear-gradient(top, #60a9ff 0%,#4394f4 100%);
    background: linear-gradient(to bottom, #60a9ff 0%,#4394f4 100%);
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#60a9ff', endColorstr='#4394f4',GradientType=0 );
    height: 350px;
    left: 0;
    position: absolute;
    top: 0;
    width: 100%;
    z-index: 1;
  }

  @media (min-width: 900px) {
    .background {
      padding: 0 0 25px;
    }
  }

  .container {
    margin: 0 auto;
    padding: 50px 0 0;
    max-width: 960px;
    width: 100%;
  }

  .panel {
    background-color: #fff;
    border-radius: 10px;
    padding: 15px 25px;
    position: relative;
    width: 100%;
    z-index: 10;
  }

  .pricing-table {
    box-shadow: 0px 10px 13px -6px rgba(0, 0, 0, 0.08), 0px 20px 31px 3px rgba(0, 0, 0, 0.09), 0px 8px 20px 7px rgba(0, 0, 0, 0.02);
    display: flex;
    flex-direction: column;
  }

  @media (min-width: 900px) {
    .pricing-table {
      flex-direction: row;
    }
  }

  .pricing-table * {
    text-align: center;
    text-transform: uppercase;
  }

  .pricing-plan {
    border-bottom: 3px solid #e1f1ff;
    padding: 25px;
  }

  .pricing-plan:last-child {
    border-bottom: none;
  }

  @media (min-width: 900px) {
    .pricing-plan {
      border-bottom: none;
      border-right: 1px solid #e1f1ff;
      flex-basis: 100%;
      padding: 25px 50px;
    }

    .pricing-plan:last-child {
      border-right: none;
    }
  }

  .pricing-img {
    margin-bottom: 25px;
    max-width: 100%;
  }

  .pricing-header {
    color: #888;
    font-weight: 600;
    letter-spacing: 1px;
  }

  .pricing-features {
    color: #016FF9;
    font-weight: 600;
    letter-spacing: 1px;
    margin: 50px 0 25px;
    padding-left: 0px;
  }

  .pricing-features-item {
    border-top: 1px solid #e1f1ff;
    font-size: 12px;
    line-height: 1.5;
  }

  .pricing-features-item:last-child {
    border-bottom: 1px solid #e1f1ff;
  }

  .pricing-price {
    color: #016FF9;
    display: block;
    font-size: 32px;
    font-weight: 700;
  }

  .pricing-button {
    border: 1px solid #9dd1ff;
    border-radius: 10px;
    color: #348EFE;
    display: inline-block;
    margin: 25px 0;
    padding: 15px 35px;
    text-decoration: none;
    transition: all 150ms ease-in-out;
  }

  .pricing-button:hover,
  .pricing-button:focus {
    background-color: #e1f1ff;
  }

  .pricing-button.is-featured {
    background-color: #48aaff;
    color: #fff;
  }

  .pricing-button.is-featured:hover,
  .pricing-button.is-featured:active {
    background-color: #269aff;
  }
  nav {
    width: 100%;
    height: 60px;
    background: #292f36;
    postion: fixed;
    z-index: 10;
}

.visible-title {
    visibility: visible;
}

nav ul { 
    list-style-type: none;
    margin: 0 2% auto 0;
    padding-left: 0;
    max-width: 100%;
    margin-right: 0px;
    margin-left: 180px;

}
nav ul li { 
    display: inline-block; 
    margin: 0px;
}
nav ul li a {
    text-decoration: none;
    color: #fff;
}
  """
    #line-height: 60px;
    # st_javascript("""
    #     var node = document.getElementById("pay1");
    #     node.onclick = function(event){
    #       window.open("https://www.geeksforgeeks.org/javascript-window-open-method/");
    #       event.preventDefault();
    #       alert("yes link clicked");
          
          
    #     }
    #     """)

    # else:
    #    print("no username")
  # st_javascript("""function myGeeks() {{
  #           document.querySelector(".button").onclick = function() {{
  #               alert("Button Clicked");
  #           }}
  #       }}""")

  # print(click)
  # com.html("""
      
  #     <input type="button" class="button"
  #       value="Button" 
  #       onclick="myGeeks()" >
  #     <script>
  #       var source = ""
  #       function myGeeks() {{ 
  #           document.querySelector(".button").onclick = function() {{
  #               alert("Button Clicked");
  #               var source = "fdadafd"
  #           }}
  #       }}
  #   </script>""" )
  # print("but",st_javascript("""JSON.parse(JSON.stringify(document.getElementsByClassName("button")));"""))
  if  pay == 'pricing':
    # # com.html(main_html , scrolling=True , height=790) #,height=1990
    st.markdown( main_html , unsafe_allow_html=True)
    st.markdown(f"<style>{css}</style>" , unsafe_allow_html=True)#const url = window.location.href
    
  elif pay == pay1 and (user !="@" and  user !="unknown@"):

    print("200000")
    amount = pay1 # IRR
    request_to_zibal = zb.request(amount)
    print(request_to_zibal)

    track_id = request_to_zibal['trackId']
    request_result_code = request_to_zibal['result']
    print(zb.request_result(request_result_code))

    if request_to_zibal['result'] == 100:
        
          st.session_state["track_id"] = track_id
          update_user(user , {"track_id" : track_id})
          update_user(user , {"payment" : 2})
          webbrowser.open("https://gateway.zibal.ir/start/" + str(request_to_zibal['trackId'])) 

  elif pay == pay2 and (user !="@" and  user !="unknown@"):
    print("500000")
    amount = pay2 # IRR
    request_to_zibal = zb.request(amount)
    print(request_to_zibal)

    track_id = request_to_zibal['trackId']
    request_result_code = request_to_zibal['result']
    print(zb.request_result(request_result_code))
    
    if request_to_zibal['result'] == 100:
      with st.form(key="pay"):
          st.header("500000 Rial")
          buy = st.form_submit_button("buy")
      if buy :
        st.success("درحال انتقال به صفحه پرداخت")
        st.session_state["track_id"] = track_id
        update_user(user , {"track_id" : track_id})
        update_user(user , {"payment" : 5})
        webbrowser.open("https://gateway.zibal.ir/start/" + str(request_to_zibal['trackId'])) 

  elif pay == pay3 and (user !="@" and  user !="unknown@"):
    print("800000")
    amount = pay3 # IRR
    request_to_zibal = zb.request(amount)
    print(request_to_zibal)

    track_id = request_to_zibal['trackId']
    request_result_code = request_to_zibal['result']
    print(zb.request_result(request_result_code))
    
    if request_to_zibal['result'] == 100:
      with st.form(key="pay"):
        st.header("800000 Rial")
        buy = st.form_submit_button("buy")
      if buy :
        st.success("درحال انتقال به صفحه پرداخت")
        st.session_state["track_id"] = track_id
        update_user(user , {"track_id" : track_id})
        update_user(user , {"payment" : 8})
        webbrowser.open("https://gateway.zibal.ir/start/" + str(request_to_zibal['trackId'])) 
  else:
      st.markdown( main_html , unsafe_allow_html=True)
      st.markdown(f"<style>{css}</style>" , unsafe_allow_html=True)
      com.html(f"""
             <script>
              const userConfirmed = confirm("you must login in");
              if (userConfirmed) {{
                  // User clicked "OK", so open the link
                  window.open("{real_url}loginpage", "_blank");
              }} else {{
                  // User clicked "Cancel" or closed the dialog
                  // Handle as needed
              }}
             </script>
             """)

