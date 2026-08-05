import streamlit as st
from PIL import Image
import os

# Konfigurasi Halaman (Wide layout penting untuk Bento Box)
st.set_page_config(
    page_title="Portofolio | Mochammad Syaifuddin Zuhri",
    page_icon="🍱",
    layout="wide"
)

# Injeksi CSS Khusus untuk memperkuat gaya Bento Box & Flexbox
st.markdown("""
<style>
    /* 1. Ubah setiap kolom Streamlit menjadi Flexbox */
    [data-testid="column"] {
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* 2. Pastikan elemen pembungkus di dalam kolom juga merenggang */
    [data-testid="column"] > div {
        display: flex !important;
        flex-direction: column !important;
        flex-grow: 1 !important;
    }

    /* 3. Gaya Bento Box dan paksaan agar mengisi tinggi penuh (flex-grow) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 20px !important;
        transition: all 0.3s ease;
        background-color: #ffffff; /* Ubah ke #1e1e1e jika ingin tema gelap */
        
        /* Ini adalah kunci utamanya */
        flex-grow: 1 !important; 
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08) !important;
        border-color: #d1d5db !important;
    }
    
    /* Sembunyikan garis divider default agar lebih bersih */
    hr {
        margin: 1.5em 0;
        border-color: transparent; 
    }
</style>
""", unsafe_allow_html=True)

st.title("Mochammad Syaifuddin Zuhri")
st.markdown("### Front-End Developer")
st.markdown("---")

# ==========================================
# BENTO GRID 1: Profil & Intro (Atas)
# ==========================================
col_hero, col_stats = st.columns([2.5, 1])

with col_hero:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
        padding: 40px 35px;
        border-radius: 20px;
        color: white;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(124, 58, 237, 0.25);
        transition: transform 0.3s ease;
    ">
        <h1 style="color: white; margin-bottom: 5px; font-size: 2.8rem; font-weight: 800;">Hai! Saya Syaifuddin 👋</h1>
        <h3 style="color: #E0E7FF; margin-top: 0; font-weight: 500; font-size: 1.4rem;">Front-End Web & Mobile Developer</h3>
        <p style="margin-top: 15px; font-size: 1.1rem; line-height: 1.7; color: #F3F4F6;">
            Saya bersemangat dalam menerjemahkan rancangan desain kolaboratif dari <b>Figma/FigJam</b> menjadi antarmuka yang <b>responsif</b> dan berkinerja tinggi. 
            Terbiasa mengawal siklus SDLC dan siap berkolaborasi erat menjembatani visi antara tim UI/UX dan logika Back-End.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_stats:
    # Kotak Atas: Menyoroti Kualifikasi Utama (Mahasiswa Aktif)
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center; margin-bottom: 0px; font-size: 1.1rem;'>🎓 Status Akademik</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #10B981; font-weight: 800; font-size: 1.3rem; margin-top: 5px; margin-bottom: 0;'>🟢 Mahasiswa Aktif</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.85rem; margin-top: 0px; color: #6B7280;'>Mencari Peluang Magang</p>", unsafe_allow_html=True)

    # Kotak Bawah: Quick Facts
    with st.container(border=True):
        st.markdown("📍 **Lokasi:** Indonesia")
        st.markdown("🤝 **Kolaborasi:** UI/UX & Backend")
        st.markdown("⚡ **Fokus:** *Responsive Web Design*")

# ==========================================
# BENTO GRID 2: Tech Stack (Tengah - 3 Kolom)
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
col_tech1, col_tech2, col_tech3 = st.columns(3)

with col_tech1:
    with st.container(border=True):
        st.markdown("#### 🎨 Frameworks & Tools")
        st.write("✨ **Next.js**")
        st.write("✨ **Vue.js**")
        st.write("✨ **Vite.js**")
        st.write("✨ **Laravel**")

with col_tech2:
    with st.container(border=True):
        st.markdown("#### 📱 Mobile & Backend")
        st.write("⚡ **Flutter**")
        st.write("⚡ **Laravel**")
        st.write("⚡ **Express.js**")
        st.write("⚡ **REST API**")

with col_tech3:
    with st.container(border=True):
        st.markdown("#### 💻 Languages")
        st.write("🚀 **TypeScript**")
        st.write("🚀 **JavaScript**")
        st.write("🚀 **Dart**")
        st.write("🚀 **Php**")

# ==========================================
# BENTO GRID 3: Proyek & Pengalaman (Bawah - 2 Kolom)
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📂 Studi Kasus Proyek (SDLC)")
col_proj1, col_proj2 = st.columns(2)

# Proyek 1
with col_proj1:
    with st.container(border=True):
        st.subheader("🏋️ Chain Fit - Gym Management Platform")
        st.markdown("**Role:** Front-End Developer | **Stack:** Vue.js, Flutter, Git")
        
        # Render Gambar
        img_path_1 = "assets/project1.jpg"
        if os.path.exists(img_path_1):
            image1 = Image.open(img_path_1)
            st.image(image1, use_container_width=True)
        else:
            st.info("[Tempat Gambar: Masukkan gambar UI Chain Fit di folder assets/]")

        st.markdown("""
        **Siklus SDLC:**
        *   **Requirement:** Menggali permasalahan operasional pemilik *gym* (skala tunggal hingga multi-cabang/multi-owner) untuk merumuskan spesifikasi fitur yang membantu pemilik *gym* dalam mengelola operasional mereka.
        *   **Design:** Mengimplementasikan rancangan UI/UX ke dalam bentuk website dan mobile. Berfokus pada pemberian *UI feedback* yang jelas (seperti *error handling* pada form) untuk menjaga pengalaman pengguna tetap optimal.
        *   **Implementation:** Membangun antarmuka Register yang mengintegrasikan otentikasi OAuth menggunakan **Vue.js** (Web) dan **Flutter** (Mobile), serta memastikan desain **responsif** di semua resolusi.
        *   **Testing:** Melakukan pengujian tampilan (*Black Box Testing*) pada berbagai perangkat untuk memvalidasi fungsionalitas dan performa antarmuka.
        *   **Deployment:** Menggunakan **Git/GitHub** untuk manajemen kode, serta mengatur alur integrasi CI/CD untuk otomatisasi pengujian (*Automated Testing*).
        """)
        st.markdown("<br>", unsafe_allow_html=True)

# Proyek 2
with col_proj2:
    with st.container(border=True):
        st.subheader("📊 Sistem Manajemen Organisasi & Keuangan PMI")
        st.markdown("**Role:** Front-End Developer | **Stack:** Laravel, SQL, Git")
        
        # Render Gambar
        img_path_2 = "assets/project2.jpg"
        if os.path.exists(img_path_2):
            image2 = Image.open(img_path_2)
            st.image(image2, use_container_width=True)
        else:
            st.info("[Tempat Gambar: Masukkan gambar UI Sistem Organisasi di folder assets/]")

        st.markdown("""
        **Siklus SDLC:**
        *   **Requirement:** Menganalisis alur kerja untuk merancang strategi digitalisasi, mengubah proses pencatatan manual berbasis Excel (manajemen keuangan dan basis data) menjadi platform web terpusat.
        *   **Design:** Menerapkan prinsip *Responsive Web Design* untuk mengubah struktur data Excel menjadi antarmuka UI/UX yang modern, bersih, dan mudah digunakan oleh anggota pengurus.
        *   **Implementation:** Mengembangkan tampilan website menggunakan struktur HTML, CSS, dan JavaScript di dalam ekosistem **Laravel** (Blade template). Berkolaborasi erat antara sisi *front-end* dan logika *back-end* (SQL) untuk integrasi data yang mulus.
        *   **Testing:** Menulis skrip *Automated Testing* dan melakukan pengujian tampilan secara komprehensif pada berbagai perangkat (mobile, tablet, desktop) untuk memastikan performa dan pengalaman pengguna tetap optimal.
        *   **Deployment:** Menggunakan **Git/GitHub** untuk kolaborasi dan *version control*, serta melakukan *deployment* mandiri ke server *production* di **Hostinger**.
        """)

# ==========================================
# BENTO GRID 4: Kontak (Bawah - Penuh)
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown("### 📫 Mari Berkolaborasi!")
    st.write("Jika Anda mencari kolaborator UI/UX atau Front-End Developer untuk proyek Anda, jangan ragu untuk menghubungi saya:")
    
    col_contact1, col_contact2, col_contact3 = st.columns(3)
    with col_contact1:
        st.markdown("[**GitHub Profile** ↗](https://github.com/Epulvis/)")
    with col_contact2:
        st.markdown("[**LinkedIn Profile** ↗](https://www.linkedin.com/in/mochammadsyaifuddinzuhri/)")
    with col_contact3:
        st.markdown("[**Email Saya** ↗](mailto:zuhrisaifuddin010@gmail.com)")