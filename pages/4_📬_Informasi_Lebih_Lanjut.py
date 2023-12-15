import streamlit as st

st.set_page_config(
     page_title="Web Absensi",
     page_icon="🗓️",
)

st.header(":mailbox: Info Lebih Lanjut")
st.write("Jika ada pertanyaan atau saran, silahkan isi forum dibawah ini")

form_kontak = """
<form action="https://formsubmit.co/emailreceiver224@gmail.com" method="POST" >
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nama Anda" required>
     <input type="email" name="email" placeholder="Email Anda" required>
     <textarea name="message" placeholder="Ketik Saran dan pertanyaan Anda Disini"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(form_kontak, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages/model/style.css")
