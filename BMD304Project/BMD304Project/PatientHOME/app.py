import streamlit as st


st.set_page_config(
    page_title="Hello Fit",
    page_icon="👩‍⚕️",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# 'Log In', 'Upload report',
# 'box-arrow-in-right', 'file-earmark ',


st.header(":mailbox: Get In Touch With Get well!")

contact_form = """
<form action="https://formsubmit.co/a7medh474279@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <input type="text" name="phone" placeholder="your phone number" required>
        <textarea name="complaint" placeholder="your complaint" required></textarea>
        <textarea name="comment" placeholder="If you have a coment enter here "></textarea>
        <button type="submit" style="background-color: #334543;" >Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(r"C:\Users\20100\Desktop\pythonstreamlit\style\style.css")
