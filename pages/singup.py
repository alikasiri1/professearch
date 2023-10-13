from database import sign_up
import streamlit as st
# real_url = "http://localhost:8501/"
real_url = "https://profesearch.streamlit.app/"
st.set_page_config(page_title="sing up", menu_items=None)
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
sign_up()

st.markdown(f"""<a href="{real_url}loginpage"   target = "_self">login</a> """ , unsafe_allow_html=True)

