import streamlit as st
from PIL import Image
import os

# Konfigurasi Halaman
st.set_page_config(
    page_title="Portofolio | Mochammad Syaifuddin Zuhri",
    page_icon="💻",
    layout="wide"
)

# Header Section
st.title("Mochammad Syaifuddin Zuhri")
st.subheader("Front-End Developer")
st.markdown("""
Saya adalah seorang Front-End Developer yang berfokus pada pembuatan antarmuka modern, responsif, dan interaktif. 
Berpengalaman dalam mengelola seluruh siklus pengembangan perangkat lunak (SDLC) dari tahap desain hingga deployment.
""")

st.divider()

# Tech Stack Section
st.header("🛠️ Tech Stack & Languages")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Frameworks & Tools:**")
    st.write("✔️ Next.js")
    st.write("✔️ Vue.js")
    st.write("✔️ Vite.js")

with col2:
    st.markdown("**Mobile & Backend:**")
    st.write("✔️ Flutter")
    st.write("✔️ Laravel")

with col3:
    st.markdown("**Programming Languages:**")
    st.write("✔️ TypeScript")
    st.write("✔️ JavaScript")
    st.write("✔️ Dart")

st.divider()

# Projects / Experience Section
st.header("📂 Pengalaman & Proyek (SDLC Case Studies)")

# Proyek 1: Aplikasi Manajemen Keuangan
st.subheader("1. Finwise - Financial Management App")

# Image rendering (Pastikan gambar ada di folder assets)
img_path_1 = "assets/project1.png"
if os.path.exists(img_path_1):
    image1 = Image.open(img_path_1)
    st.image(image1, caption="Tampilan Dashboard Finwise", use_container_width=True)
else:
    st.info("Tambahkan gambar 'project1.png' di dalam folder 'assets/' untuk menampilkan pratinjau proyek.")

st.markdown("""
**Siklus SDLC:**
*   **Requirement Analysis:** Berkolaborasi dengan pemangku kepentingan untuk mengidentifikasi kebutuhan fitur pelacakan anggaran dan manajemen pengeluaran harian.
*   **Design:** Mengonversi prototipe UI/UX interaktif dari Figma ke dalam desain komponen berbasis Atomic Design.
*   **Implementation:** Membangun antarmuka menggunakan **Next.js** dan **TypeScript** untuk performa tinggi, serta mengintegrasikan state management.
*   **Testing:** Melakukan pengujian fungsional pada komponen UI dan memastikan responsivitas di berbagai perangkat (Mobile & Desktop).
*   **Deployment & Maintenance:** Melakukan deployment aplikasi ke **Vercel** dan memantau analitik performa web secara berkala.
""")

st.write("---")

# Proyek 2: Inisiatif Koperasi UMKM
st.subheader("2. Platform Digital Koperasi UMKM")

img_path_2 = "assets/project2.png"
if os.path.exists(img_path_2):
    image2 = Image.open(img_path_2)
    st.image(image2, caption="Tampilan Aplikasi Mobile Koperasi UMKM", use_container_width=True)
else:
    st.info("Tambahkan gambar 'project2.png' di dalam folder 'assets/' untuk menampilkan pratinjau proyek.")

st.markdown("""
**Siklus SDLC:**
*   **Requirement Analysis:** Menganalisis kebutuhan digitalisasi pencatatan transaksi untuk koperasi skala kecil dan menengah.
*   **Design:** Merancang arsitektur navigasi aplikasi mobile dan alur transaksi pengguna.
*   **Implementation:** Mengembangkan aplikasi mobile cross-platform menggunakan **Flutter** dan **Dart**, berkolaborasi dengan tim backend **Laravel** melalui REST API.
*   **Testing:** Melakukan UAT (User Acceptance Testing) secara langsung dengan para pelaku UMKM untuk memvalidasi kemudahan penggunaan.
*   **Deployment & Maintenance:** Mengunggah versi rilis ke App Store / Play Store dan merilis patch pembaruan berdasarkan feedback pengguna.
""")

st.divider()

# Footer / Kontak
st.header("📫 Hubungi Saya")
st.markdown("""
Jika Anda tertarik untuk berkolaborasi atau mendiskusikan peluang proyek, silakan hubungi saya melalui:
*   **GitHub:** [github.com/username-anda](https://github.com/)
*   **LinkedIn:** [linkedin.com/in/username-anda](https://linkedin.com/)
*   **Email:** email.anda@domain.com
""")