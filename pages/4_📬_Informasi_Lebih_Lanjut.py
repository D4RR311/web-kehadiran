import streamlit as st

st.set_page_config(
     page_title="Web Absensi",
     page_icon="🗓️",
)

st.header(":mailbox: Info Lebih Lanjut")

st.write("Jika ada pertanyaan atau saran, silahkan isi forum dibawah ini")

form_kontak = """
<form action="https://formsubmit.co/receiveremail612@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(form_kontak, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("pages/model/style.css")
