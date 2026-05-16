import streamlit as st

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Chatbot Sains Data UPGRISBA",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("style.css") as f:
    css = f.read()

st.markdown(
    f"""
    <style>
    {css}
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# FOTO PROFIL
# =====================================================

profile_img = r"C:\Users\hp\Pictures\WhatsApp Image 2026-05-15 at 18.56.10.jpeg"

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(profile_img, use_container_width=True)

    st.markdown("""
    <div class="sidebar-title">
        🎓 SAINS DATA
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-subtitle">
        Universitas PGRI Sumatera Barat
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="menu-box">

    <div class="menu-title">
    📚 MENU INFORMASI
    </div>

    ✅ Program Studi<br>
    ✅ Visi dan Misi<br>
    ✅ Biaya Kuliah<br>
    ✅ Jadwal Pendaftaran<br>
    ✅ Jalur Pendaftaran<br>
    ✅ Fasilitas Kampus<br>
    ✅ Staff Dosen<br>
    ✅ Beasiswa KIP-K<br>
    ✅ Sertifikasi Dosen<br>
    ✅ Prospek Kerja<br>
    ✅ Kontak Program Studi<br>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="title">
CHATBOT SAINS DATA
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Universitas PGRI Sumatera Barat
</div>
""", unsafe_allow_html=True)

# =====================================================
# INFO BOX
# =====================================================

st.markdown("""
<div class="info-box">

Selamat datang di Chatbot Informasi Program Studi
Sains Data Universitas PGRI Sumatera Barat.

💡 Anda dapat bertanya tentang:

🎓 Program Studi  
🎯 Visi dan Misi  
💰 Biaya Kuliah  
📅 Jadwal Pendaftaran  
🛣️ Jalur Pendaftaran  
🏫 Fasilitas Kampus  
👨‍🏫 Staff Dosen  
🎓 Beasiswa KIP-K  
📜 Sertifikasi Dosen  
💼 Prospek Kerja  
☎️ Kontak Program Studi  

</div>
""", unsafe_allow_html=True)

# =====================================================
# INPUT USER
# =====================================================

user_input = st.text_input(
    "💬 Silakan masukkan pertanyaan Anda"
)

# =====================================================
# RESPON CHATBOT
# =====================================================

if user_input:

    pertanyaan = user_input.lower()

    # =================================================
    # SAPAAN
    # =================================================

    if any(kata in pertanyaan for kata in [
        "halo", "hai", "hello", "hi", "assalamualaikum"
    ]):

        st.success("""
👋 Halo, selamat datang di Chatbot Program Studi
Sains Data Universitas PGRI Sumatera Barat.

Silakan tanyakan informasi yang Anda butuhkan 🎓
""")

    # =================================================
    # PROGRAM STUDI
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "program studi",
        "prodi",
        "sains data",
        "jurusan",
        "data science"
    ]):

        st.success("""
📘 PROGRAM STUDI S1 SAINS DATA

Program Studi Sains Data mempelajari:

• Artificial Intelligence  
• Machine Learning  
• Big Data  
• Data Mining  
• Data Analytics  
• Pemrograman Python  
• Statistik Data  
• Deep Learning  
• Business Intelligence  

Program Studi Sains Data Universitas PGRI
Sumatera Barat merupakan satu-satunya
Program Studi Sains Data di Sumatera Barat.

Lulusan dipersiapkan menjadi tenaga ahli
di bidang teknologi dan data modern.
""")

    # =================================================
    # VISI
    # =================================================

    elif "visi" in pertanyaan:

        st.success("""
🎯 VISI

Menjadi Program Studi yang menghasilkan
lulusan unggul di bidang Sains Data dan
Artificial Intelligence yang inovatif dan
kompetitif di tingkat nasional.
""")

    # =================================================
    # MISI
    # =================================================

    elif "misi" in pertanyaan:

        st.success("""
🎯 MISI

1. Menyelenggarakan pendidikan berbasis AI  
2. Mengembangkan penelitian Data Science  
3. Menghasilkan lulusan profesional  
4. Menjalin kerjasama industri dan akademik  
5. Mengembangkan IPTEKS bidang Sains Data  
""")

    # =================================================
    # BIAYA
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "biaya",
        "uang kuliah",
        "spp",
        "ukt",
        "bayar"
    ]):

        st.success("""
💰 BIAYA KULIAH

Semester 1:

• Pengembangan : Rp 1.950.000  
• Orientasi & Jaket : Rp 500.000  
• SPP : Rp 2.850.000  

Total : Rp 5.300.000

Semester 2 - 8:

• SPP : Rp 2.850.000  
• Kemahasiswaan : Rp 100.000  
""")

    # =================================================
    # PENDAFTARAN
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "pendaftaran",
        "daftar",
        "registrasi",
        "jadwal"
    ]):

        st.success("""
📅 JADWAL PENDAFTARAN

Gelombang 1:
Awal Januari - 05 April 2026

Gelombang 2:
08 April - Awal September 2026

Pendaftaran dilakukan secara online melalui:
https://pmb.upgrisba.ac.id
""")

    # =================================================
    # JALUR PENDAFTARAN
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "jalur",
        "kip",
        "roadshow",
        "undangan",
        "wali nagari"
    ]):

        st.success("""
🛣️ JALUR PENDAFTARAN

1. Jalur KIP-K  
2. Jalur Siswa Berprestasi  
3. Jalur Roadshow  
4. Jalur Mahasiswa Undangan  
5. Jalur Rekomendasi Wali Nagari  
""")

    # =================================================
    # FASILITAS
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "fasilitas",
        "lab",
        "laboratorium",
        "wifi",
        "kampus"
    ]):

        st.success("""
🏫 FASILITAS KAMPUS

• Laboratorium Big Data dan AI  
• Laboratorium Komputer  
• WiFi Kampus  
• Perpustakaan  
• Aula Kampus  
• Ruang Multimedia  
• UPCC  
• Masjid Kampus  
• Ruang Classroom  
""")

    # =================================================
    # DOSEN
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "dosen",
        "staff",
        "pengajar"
    ]):

        st.success("""
👨‍🏫 STAFF DOSEN

• Dr. Zulfaneti, M.Si  
• Satrio Junaidi, M.Kom  
• Dr. Delsi K, M.Si  
• Ainil Mardiyah, M.Si  
• Irfan Fadhli, M.Kom  
• Nia Febriyani, M.Kom  
""")

    # =================================================
    # SERTIFIKASI DOSEN
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "sertifikasi",
        "internasional",
        "nasional"
    ]):

        st.success("""
📜 SERTIFIKASI DOSEN

Dosen memiliki sertifikasi nasional dan internasional:

• IBM Artificial Intelligence Engineer  
• Applied Data Science with Python  
• Internet of Things (IOT)  
• Data Scientist BNSP  
• Multimedia BNSP  
""")

    # =================================================
    # BEASISWA
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "beasiswa",
        "kip-k",
        "kip",
        "bantuan"
    ]):

        st.success("""
🎓 BEASISWA

• Beasiswa KIP-K  
• Beasiswa Prestasi Akademik  
• Bantuan Pendidikan  
• Jalur Siswa Berprestasi  
""")

    # =================================================
    # PEKERJAAN
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "kerja",
        "pekerjaan",
        "prospek",
        "lulusan",
        "karir"
    ]):

        st.success("""
💼 PROSPEK KERJA LULUSAN

• Data Scientist  
• AI Engineer  
• Data Analyst  
• Machine Learning Engineer  
• Software Developer  
• Big Data Engineer  
• Konsultan Data  
• Programmer  
""")

    # =================================================
    # KONTAK
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "kontak",
        "nomor",
        "wa",
        "whatsapp",
        "hubungi"
    ]):

        st.success("""
☎️ CONTACT PERSON

Zulfaneti :
081363387278

Satrio Junaidi :
082389238003

Email:
prodisaindata.upgrisba@gmail.com
""")

    # =================================================
    # ALAMAT
    # =================================================

    elif any(kata in pertanyaan for kata in [
        "alamat",
        "lokasi",
        "dimana"
    ]):

        st.success("""
📍 ALAMAT KAMPUS

Universitas PGRI Sumatera Barat

Jl. Gunung Pangilun,
Kota Padang,
Sumatera Barat
""")

    # =================================================
    # DEFAULT
    # =================================================

    else:

        st.warning("""
❌ Maaf, informasi belum tersedia.

Silakan tanyakan:

• Program Studi  
• Biaya Kuliah  
• Pendaftaran  
• Jalur Pendaftaran  
• Beasiswa  
• Fasilitas  
• Dosen  
• Kontak  
""")

# =====================================================
# WHATSAPP DOSEN
# =====================================================

st.markdown("""
<div style="
background: rgba(255,255,255,0.35);
padding:30px;
border-radius:25px;
text-align:center;
margin-top:40px;
box-shadow:0 8px 20px rgba(0,0,0,0.1);
">

<h2 style="
color:black;
margin-bottom:25px;
">
👨‍🏫 Hubungi Dosen Program Studi
</h2>

<!-- DOSEN 1 -->

<a href="https://wa.me/6281363387278" target="_blank" style="text-decoration:none;">

<button style="
background: linear-gradient(90deg,#25D366,#128C7E);
color:white;
padding:16px 28px;
border:none;
border-radius:40px;
font-size:17px;
font-weight:bold;
cursor:pointer;
margin:12px;
width:300px;
display:flex;
align-items:center;
justify-content:center;
gap:12px;
box-shadow:0 5px 15px rgba(0,0,0,0.2);
">

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
width="28">

Dr. Zulfaneti, M.Si

</button>

</a>

<br>

<!-- DOSEN 2 -->

<a href="https://wa.me/6282389238003" target="_blank" style="text-decoration:none;">

<button style="
background: linear-gradient(90deg,#2563eb,#1d4ed8);
color:white;
padding:16px 28px;
border:none;
border-radius:40px;
font-size:17px;
font-weight:bold;
cursor:pointer;
margin:12px;
width:300px;
display:flex;
align-items:center;
justify-content:center;
gap:12px;
box-shadow:0 5px 15px rgba(0,0,0,0.2);
">

<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
width="28">

Satrio Junaidi, M.Kom

</button>

</a>

</div>
""", unsafe_allow_html=True)