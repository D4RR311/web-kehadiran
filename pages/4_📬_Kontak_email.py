import streamlit as st

st.header(" Tetap Dalam Sentuhan")

contact_form = """
<form action="https://formsubmit.co/darrellardhanihidayat@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Nama Anda" required>
    <input type="email" name="email" placeholder="Email Anda" required>
    <textarea name="message" placeholder="Orang Tua Dari Kelas"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("pages/aset/style.css")
