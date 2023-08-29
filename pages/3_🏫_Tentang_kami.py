import streamlit as st
from pathlib import Path
from PIL import Image

dir_file = Path(__file__).parent if "_file_" in locals() else Path.cwd()
file_css = dir_file /"pages"/ "model" / "main.css"
laporan_sekolah = dir_file /"pages"/ "aset" /"Laporan Data Sekolah.pdf"
gambar_logo = dir_file /"foto"/"logo gaka.png"

NAMA = "SMPN 3 KALASAN"
DESKRIPSI = """
SMP NEGERI 3 KALASAN adalah salah satu satuan pendidikan dengan jenjang SMP di Purwo Martani, Kec. Kalasan, Kab. Sleman, Di Yogyakarta. Dalam menjalankan kegiatannya, SMP NEGERI 3 KALASAN berada di bawah naungan Kementerian Pendidikan dan Kebudayaan.
"""
EMAIL="http://informasismpn3kalasan.scn.id"
SOSMED={
    "Instagram": "https://www.instagram.com/smpn3kalasan/",
    "Youtube": "https://youtube.com/@osissmpnegeri3kalasan600?si=6d9Eei1t2KCMjUCb",
    "TikTok": "https://www.tiktok.com/@osis.smpn3kalasan?_t=8fDYs9g08j1&_r=1",
    "X": "https://twitter.com/osis_spegaka?s=11&t=BF7ffm53yQohDmJpP8gtSA"
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

st.markdown(custom_web, unsafe_allow_html=True)
st.title("Tentang Sekolah Kami")

with open(file_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(laporan_sekolah, "rb") as file_pdf:
    PDFByte = file_pdf.read()
gmbr_profil = Image.open(gambar_logo)

col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(gmbr_profil, width=230)

with col2:
    st.title(NAMA)
    st.write(DESKRIPSI)
    st.download_button(
        label="📃 Download Data Sekolah",
        data=PDFByte,

        file_name=laporan_sekolah.name,
        mime="application/octet-stream",
    )
st.write("📬 Email Sekolah: ",EMAIL,"/","akhyariakhyari@yahoo.co.id")

st.write("#")
cols = st.columns(len(SOSMED))
for index, (platform, link) in enumerate(SOSMED.items()):
    cols[index].write(f"[{platform}]({link})")

#alamat sekolahh
st.write("#")
st.subheader("ALAMAT SMP NEGERI 3 KALASAN")
st.write("MP NEGERI 3 KALASAN beralamat di Sidokerto, Purwomartani, Purwo Martani, Kec. Kalasan, Kab. Sleman, Di Yogyakarta, dengan kode pos 55571.")

#fasilitas sekolah
st.write("#")
st.subheader("Fasilitas yang disediakan SMP NEGERi 3 KALASAN")
st.write("SMP NEGERI 3 KALASAN menyediakan listrik untuk membantu kegiatan belajar mengajar. Sumber listrik yang digunakan oleh SMP NEGERI 3 KALASAN berasal dari PLN.")

#akreditasi
st.write("#")
st.subheader("AKREDITASI")
st.write("SMP NEGERI 3 KALASAN memiliki akreditasi A, berdasarkan sertifikat 5.01/BAP-SM/TU/XI/2016.")

#kontak email
st.write("#")
st.subheader("Kontak yang dapat dihubungi")
st.write("Apabila anda ingin bertanya atau menghubungi langsung SMP NEGERI 3 KALASAN, dapat melalui beberapa media. Website sekolah dapat dibuka melalui url http://informasismpn3kalasan.scn.id. Apabila ingin mengirimkan surat elektronik (email), dapat dikirimkan ke akhyariakhyari@yahoo.co.id.")
