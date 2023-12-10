 import streamlit as st

st.header(":mailbox: Info Lebih Lanjut")


form_kontak = """
<form action="https://formsubmit.co/emailreceiver224@gmail.com" method="POST" />
     <input type="hidden" name="_capctcha" value="false">
     <input type="text" name="name" placeholder="Nama Anda" required>
     <input type="email" name="email" placeholder="Email Anda" required>
     <textarea name="message" placeholder="Ketik Pesan Anda Disini"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(form_kontak, unsafe_allow_html=True)

def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages/aset/style.css")
