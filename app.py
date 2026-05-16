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

profile_img = "WhatsApp Image 2026-05-15 at 18.56.10.jpeg"

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(profile_img, width='stretch')

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

    # SAPAAN
    if any(kata in pertanyaan for kata in [
        "halo", "hai", "hello", "hi", "assalamualaikum"
    ]):

        st.success("""
👋 Halo, selamat datang di Chatbot Program Studi
Sains Data Universitas PGRI Sumatera Barat.

Silakan tanyakan informasi yang Anda butuhkan 🎓
""")

    # PROGRAM STUDI
    elif any(kata in pertanyaan for kata in [
        "program studi",
        "prodi",
        "sains data",
        "jurusan",
        "data science"
    ]):

        st.success("""
📘 PROGRAM STUDI S1 SAINS DATA

• Artificial Intelligence  
• Machine Learning  
• Big Data  
• Data Mining  
• Data Analytics  
• Pemrograman Python  
• Statistik Data  
• Deep Learning  
• Business Intelligence  
""")

    # VISI
    elif "visi" in pertanyaan:

        st.success("""
🎯 VISI

Menjadi Program Studi unggul di bidang
Sains Data dan Artificial Intelligence.
""")

    # MISI
    elif "misi" in pertanyaan:

        st.success("""
🎯 MISI

1. Menyelenggarakan pendidikan berbasis AI  
2. Mengembangkan penelitian Data Science  
3. Menghasilkan lulusan profesional  
""")

    # BIAYA
    elif any(kata in pertanyaan for kata in [
        "biaya",
        "uang kuliah",
        "spp",
        "ukt"
    ]):

        st.success("""
💰 BIAYA KULIAH

Semester 1:
Rp 5.300.000

Semester berikutnya:
Rp 2.950.000
""")

    # PENDAFTARAN
    elif any(kata in pertanyaan for kata in [
        "pendaftaran",
        "daftar",
        "jadwal"
    ]):

        st.success("""
📅 JADWAL PENDAFTARAN

Gelombang 1:
Januari - April

Gelombang 2:
April - September

https://pmb.upgrisba.ac.id
""")

    # FASILITAS
    elif any(kata in pertanyaan for kata in [
        "fasilitas",
        "lab",
        "wifi"
    ]):

        st.success("""
🏫 FASILITAS

• Laboratorium AI  
• WiFi Kampus  
• Perpustakaan  
• Aula Kampus  
""")

    # DOSEN
    elif any(kata in pertanyaan for kata in [
        "dosen",
        "staff"
    ]):

        st.success("""
👨‍🏫 STAFF DOSEN

• Dr. Zulfaneti, M.Si  
• Satrio Junaidi, M.Kom  
• Dr. Delsi K, M.Si  
""")

    # BEASISWA
    elif any(kata in pertanyaan for kata in [
        "beasiswa",
        "kip"
    ]):

        st.success("""
🎓 BEASISWA

• Beasiswa KIP-K  
• Beasiswa Prestasi  
""")

    # PEKERJAAN
    elif any(kata in pertanyaan for kata in [
        "kerja",
        "karir",
        "prospek"
    ]):

        st.success("""
💼 PROSPEK KERJA

• Data Scientist  
• AI Engineer  
• Data Analyst  
• Programmer  
""")

    # KONTAK
    elif any(kata in pertanyaan for kata in [
        "kontak",
        "wa",
        "whatsapp"
    ]):

        st.success("""
☎️ CONTACT PERSON

Zulfaneti :
081363387278

Satrio Junaidi :
082389238003
""")

    # ALAMAT
    elif any(kata in pertanyaan for kata in [
        "alamat",
        "lokasi"
    ]):

        st.success("""
📍 ALAMAT

Universitas PGRI Sumatera Barat

Jl. Gunung Pangilun,
Kota Padang,
Sumatera Barat
""")

    # DEFAULT
    else:

        st.warning("""
❌ Maaf, informasi belum tersedia.
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
">

<h2 style="color:black;">
👨‍🏫 Hubungi Dosen Program Studi
</h2>

<a href="https://wa.me/6281363387278" target="_blank">
<button style="
background:#25D366;
color:white;
padding:15px 25px;
border:none;
border-radius:30px;
margin:10px;
cursor:pointer;
">
Dr. Zulfaneti, M.Si
</button>
</a>

<br>

<a href="https://wa.me/6282389238003" target="_blank">
<button style="
background:#2563eb;
color:white;
padding:15px 25px;
border:none;
border-radius:30px;
margin:10px;
cursor:pointer;
">
Satrio Junaidi, M.Kom
</button>
</a>

</div>
""", unsafe_allow_html=True)