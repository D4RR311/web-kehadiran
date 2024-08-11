import streamlit as st
from pathlib import Path
from PIL import Image

dir_file = Path(__file__).parent if "_file_" in locals() else Path.cwd()
file_css = dir_file /"pages"/ "model" / "main.css"
hasil_laporan = dir_file /"pages"/ "aset" / "LAPORAN KIR OK.pdf"
gmbr_profil = dir_file / "foto" / "darrell kacamata.jpg"
gmbr_profil_2 = dir_file / "foto" / "ROGHIB.jpg"

NAMA1 = "Darrell Ardhani Hidayat"
DESKRIPSI1 = """
Peneliti di bidang IPTEK dan rekayasa, Operator Web Absensi dan Repository Github, Pemula Dalam Bahasa Pemrograman Python
"""
EMAIL1 = "darrellardhanihidayat@gmail.com"
SOSIAL_MEDIA1 = {
    "GitHub": "https://github.com/D4RR311",
    "Instagram": "https://www.instagram.com/d4r.m409?igsh=MWQ4OTZpenFrd3Z2ZQ==",
    "Youtube": "https://youtube.com/@d4rr3119?si=HvQrVPC1kEcaDPIr"
}

NAMA2="Roghib Khoirul Adnan"
DESKRIPSI2="""
Peneliti di bidang IPTEK dan rekayasa, Operator Web Absensi dan Repository Github, Pemula Dalam Bahasa Pemrograman Python
"""
EMAIL2= "rohibkoirul4@gmail.com"
SOSIAL_MEDIA2 = {
    "GitHub": "https://github.com/Rxyzen01",
    "Instagram": "https://www.instagram.com/roghibkhoirul.a?igsh=MTc4Y3FmNzR2NzlhOQ=="
}

st.set_page_config(
    page_title="Web Absensi",
    page_icon="🗓️",
)

custom_web = f"""
<style>
[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="collapsedControl"]{{
left: 1rem;
}}
</style>
"""

st.title("Bagian Profil Kreator")
st.markdown(custom_web, unsafe_allow_html=True)

with open(file_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(hasil_laporan, "rb") as file_pdf:
    PDFByte = file_pdf.read()
gmbr_profil = Image.open(gmbr_profil)  



col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(gmbr_profil, width=230)

with col2:
    st.title(NAMA1)
    st.write(DESKRIPSI1)
    st.download_button(
        label="📃 Download Laporan",
        data=PDFByte,

        file_name=hasil_laporan.name,
        mime="application/octet-stream",
    )
st.write("📬Email Kreator:",EMAIL1)

st.write("#")
st.subheader("Sosial Media:")
cols = st.columns(len(SOSIAL_MEDIA1))
for index, (platform, link) in enumerate(SOSIAL_MEDIA1.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Pengalaman")
st.write(
    """
- Memiliki Pengalaman Terhadap Bahasa Pemrograman Python
- Operator Web Absensi
"""
)

st.write("#")
st.subheader("Keterampilan")
st.write(
    """
- 💻Pemrograman: Python, JSON, CSS
"""
)

st.write("#")
st.subheader("Kegemaran")
st.write(
    """
- 💻Programming
- 🏀Basketball
- 📺Nonton anime
- 🎮Main Valorant
- 📽️Livestream Youtube
"""
)

st.write("#")
st.subheader("Prestasi")
st.write(
    """
- 🏆 Juara 2 Dalam Perlombaan Karya Ilmiah Remaja Tingkat Kabupaten Bidang IPTEK Dan Rekayasa Tingkat SMP
"""
)

st.write("---")
col3, col4 = st.columns(4, gap="small")
with col3:
    st.image(gmbr_profil_2, width=230)
with col4:
    st.title(NAMA2)
    st.write(DESKRIPSI2)
