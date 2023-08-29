import streamlit as st

st.set_page_config(
    page_title="Web Absensi",
    page_icon="🗓️",
)

custom_web = f"""
<style>

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="collapsedControl"] {{
left: 1rem;
}}

</style>
"""

st.title("Tetap Dalam Sentuhan")
st.markdown(custom_web, unsafe_allow_html=True)
st.write("📬Untuk Mengetahui Lebih Lanjut Tentang Absensi Kami, isi Email Anda Di Bawah Sini")
kontak_form = """
<form action="https://formsubmit.co/emailreceiver224@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Nama Anda" required>
    <input type="email" name="email" placeholder="Email Anda" required>
    <textarea name="message" placeholder="Orang Tua Dari Kelas"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(kontak_form, unsafe_allow_html=True)

st.write("#")
st.subheader("🤔Jika Ada Pertanyaan, Silahkan Ketik Email Anda dan pertanyaan anda")
pertanyaan_form =  """
<form action="https://formsubmit.co/emailreceiver224@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Nama Anda" required>
    <input type="email" name="email" placeholder="Email Anda" required>
    <textarea name="message" placeholder="Orang Tua Dari Kelas dan pertanyaan anda"></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(pertanyaan_form, unsafe_allow_html=True)

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("pages/aset/style.css")
