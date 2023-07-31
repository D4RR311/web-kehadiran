import streamlit as st
from pathlib import Path
from PIL import Image

dir_file = Path(__file__).parent if "_file_" in locals() else Path.cwd()
file_css = dir_file /"pages"/ "model" / "main.css"
hasil_laporan = dir_file /"pages"/ "aset" / "LAPORAN KIR OK.pdf"
gmbr_profil = dir_file / "foto" / "darrell.jpeg"


st.set_page_config(
    page_title="Web Absensi",
    page_icon="🗓️",
)


NAMA = "Darrell Ardhani Hidayat"
DESKRIPSI = """
Peneliti SMPN 3 Kalasan, Operator Web Absensi dan Reposity Github, Pemula Dalam Bahasa Pemrograman Python
"""
EMAIL = "darrellardhanihidayat@gmail.com"
SOSIAL_MEDIA = {
    "GitHub": "https://github.com/D4RR311",
}

st.title("Bagian Profil Kreator")

st.sidebar.succes("Pilih Bagian Yang Inginn Dituju.")

with open(file_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(hasil_laporan, "rb") as file_pdf:
    PDFByte = file_pdf.read()
gmbr_profil = Image.open(gmbr_profil)  



col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(gmbr_profil, width=230)

with col2:
    st.title(NAMA)
    st.write(DESKRIPSI)
    st.download_button(
        label="📃 Download Laporan",
        data=PDFByte,

        file_name=hasil_laporan.name,
        mime="application/octet-stream",
    )
st.write("📬",EMAIL)

st.write("#")
cols = st.columns(len(SOSIAL_MEDIA))
for index, (platform, link) in enumerate(SOSIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Pengalaman")
st.write(
    """
- 8 Bulan Pengalaman Terhadap Bahasa Pemrograman Python
- Sedikit Menguasai Bahasa Pemrograman Pyhton
"""
)

st.write("#")
st.subheader("Keterampilan")
st.write(
    """
- 💻Pemrograman: Python (cv2, Pandas, Datetime, Numpy, Face_Recognition), Streamlit
"""
)

st.write("#")
st.subheader("Riwayat Kegiatan")
st.write("---")

st.write("🥸", "Junior Operator Pemrograman | SMP N 3 KALASAN")
st.write("25/04/2023 - Sampai Sekarang")

st.write("#")
st.subheader("Prestasi")
st.write("🏆 Juara 2 Dalam Perlombaan Karya Ilmiah Remaja Tingkat Kabupaten Bidang IPTEK Dan Rekayasa Tingkat SMP")
