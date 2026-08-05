import streamlit as st
from PIL import Image
import os
import base64

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

def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ==========================================
# BENTO GRID 1: Profil & Intro (Atas)
# ==========================================
col_text, col_img = st.columns([1.8, 1.2])

with col_text:
    st.markdown("""
    <div style="padding: 20px 10px 40px 10px;">
        <p style="color: #A78BFA; font-size: 1.2rem; font-weight: 600; margin-bottom: 0px;">
            Halo Semua 👋, Saya
        </p>
        <h1 style="font-size: 3.8rem; font-weight: 800; line-height: 1.1; margin-top: 5px; margin-bottom: 10px; color: #F8FAFC;">
            Mochammad Syaifuddin Zuhri
        </h1>
        <p style="font-size: 1.3rem; font-weight: 400; color: #9CA3AF; margin-top: 0px; margin-bottom: 25px;">
            Mahasiswa Aktif & Front-End Developer | <span style="text-decoration: underline; color: #E5E7EB;">Mencari Peluang Magang</span>
        </p>
        <p style="font-size: 1.1rem; color: #D1D5DB; max-width: 90%; line-height: 1.6; margin-bottom: 35px;">
            Portofolio ini menampilkan proyek dan kontribusi saya dalam menerjemahkan rancangan desain UI/UX menjadi antarmuka website yang responsif, berkinerja tinggi, dan ramah pengguna.
        </p>
        <a href="mailto:emailanda@domain.com" style="
            display: inline-block; 
            background-color: #7C3AED; 
            color: #FFFFFF; 
            padding: 12px 30px; 
            border-radius: 8px; 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 1.05rem;
            transition: background-color 0.3s ease;
        " onmouseover="this.style.backgroundColor='#6D28D9'" onmouseout="this.style.backgroundColor='#7C3AED'">
            Hubungi Saya
        </a>
    </div>
    """, unsafe_allow_html=True)

with col_img:
    profile_img_path = "assets/profile.jpg"
    
    if os.path.exists(profile_img_path):
        img_base64 = get_img_as_base64(profile_img_path)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        # HTML & CSS untuk membuat Blob Shape dengan animasi
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%; padding-top: 10px;">
            <img src="data:image/png;base64,{img_base64}" style="
                width: 100%;
                max-width: 320px;
                height: 320px;
                object-fit: cover;
                object-position: top;
                box-shadow: 0 15px 35px rgba(124, 58, 237, 0.15);
                border: 2px solid #374151;
                /* Ini yang membuat bentuknya jadi tidak beraturan (Blob) */
                border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; 
                animation: morph 8s ease-in-out infinite;
            ">
        </div>
        
        <style>
            /* Keyframes ini akan membuat bentuk oval-nya bergerak mengalir layaknya cairan */
            @keyframes morph {{
                0% {{ border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }}
                50% {{ border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }}
                100% {{ border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }}
            }}
        </style>
        """, unsafe_allow_html=True)
    else:
        # Fallback jika gambar belum ada
        st.info("💡 Tambahkan foto profil Anda dengan nama 'profile.png' di folder 'assets/' untuk melihat efeknya.")

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