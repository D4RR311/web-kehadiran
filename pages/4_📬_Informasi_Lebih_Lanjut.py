import streamlit as st

st.header(":mailbox: Info Lebih Lanjut")


form_kontak = """
<form action="https://formsubmit.co/nekahudu@mailgolem.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(form_kontak, unsafe_allow_html=True)
