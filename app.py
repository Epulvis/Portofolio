import streamlit as st
from PIL import Image
import os

# Konfigurasi Halaman (Wide layout penting untuk Bento Box)
st.set_page_config(
    page_title="Portofolio | Mochammad Syaifuddin Zuhri",
    page_icon="🍱",
    layout="wide"
)

# Injeksi CSS Khusus untuk memperkuat gaya Bento Box
st.markdown("""
<style>
    /* Mengubah border container Streamlit menjadi gaya Bento (sudut membulat & bayangan) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 20px !important;
        transition: all 0.3s ease;
        background-color: #ffffff; /* Ubah ke #1e1e1e jika ingin tema gelap */
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
with st.container(border=True):
    col_prof1, col_prof2 = st.columns([2, 1])
    with col_prof1:
        st.subheader("👋 Halo!")
        st.write("""
        Saya berfokus pada pembuatan antarmuka modern, responsif, dan interaktif. 
        Berpengalaman dalam mengelola seluruh siklus pengembangan perangkat lunak (SDLC) dari tahap desain UI/UX hingga deployment ke production.
        """)
    with col_prof2:
        st.write("📍 **Lokasi:** Indonesia")
        st.write("💼 **Status:** Open to Work")
        st.write("🌐 **Fokus:** Web & Mobile App")

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

with col_tech2:
    with st.container(border=True):
        st.markdown("#### 📱 Mobile & Backend")
        st.write("⚡ **Flutter**")
        st.write("⚡ **Laravel**")
        st.write("⚡ **REST API**")

with col_tech3:
    with st.container(border=True):
        st.markdown("#### 💻 Languages")
        st.write("🚀 **TypeScript**")
        st.write("🚀 **JavaScript**")
        st.write("🚀 **Dart**")

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
        *   **Requirement:** Menggali permasalahan operasional pemilik *gym* (skala tunggal hingga multi-cabang/multi-owner) untuk merumuskan spesifikasi fitur registrasi dan *onboarding* yang efisien.
        *   **Design:** Mengimplementasikan rancangan UI/UX ke dalam bentuk website. Berfokus pada pemberian *UI feedback* yang jelas (seperti *error handling* pada form) untuk menjaga pengalaman pengguna tetap optimal.
        *   **Implementation:** Membangun antarmuka Register yang mengintegrasikan otentikasi OAuth menggunakan **Vue.js** (Web) dan **Flutter** (Mobile), serta memastikan desain **responsif** di semua resolusi.
        *   **Testing:** Melakukan pengujian tampilan (*Black Box Testing*) pada berbagai perangkat untuk memvalidasi fungsionalitas dan performa antarmuka.
        *   **Deployment:** Menggunakan **Git/GitHub** untuk manajemen kode, serta mengatur alur integrasi CI/CD untuk otomatisasi pengujian (*Automated Testing*).
        """)

# Proyek 2
with col_proj2:
    with st.container(border=True):
        st.subheader("🤝 Platform Koperasi UMKM")
        
        # Render Gambar
        img_path_2 = "assets/project2.jpg"
        if os.path.exists(img_path_2):
            image2 = Image.open(img_path_2)
            st.image(image2, use_container_width=True)
        else:
            st.info("[Tempat Gambar: Masukkan project2.jpg di folder assets/]")

        st.markdown("""
        **Siklus SDLC:**
        *   **Requirement:** Perencanaan strategis digitalisasi pencatatan untuk sektor UMKM.
        *   **Design:** Merancang arsitektur navigasi mobile dan alur pengguna.
        *   **Implementation:** Pengembangan *cross-platform* dengan **Flutter** & **Dart**, integrasi API **Laravel**.
        *   **Testing:** Evaluasi langsung (UAT) dengan perwakilan tim/pengguna akhir.
        *   **Deployment:** Persiapan rilis aplikasi dan manajemen *task tracking*.
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