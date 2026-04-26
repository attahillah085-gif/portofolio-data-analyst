import streamlit as st
import pandas as pd
import numpy as np
import os

# ==========================================
# 🛠️ KONFIGURASI PATH (Untuk Server Cloud)
# ==========================================
FOTO_PROFIL = "foto.png"  # Pastikan ekstensi sesuai dengan nama di komputermu (foto.png atau foto.jpg)
FILE_CV = "cv athaillah tri naufaldo.pdf"

# ==========================================
# 🎨 SETTING HALAMAN & TEMA
# ==========================================
st.set_page_config(page_title="Athaillah | Data Portfolio", page_icon="📈", layout="wide")

# Custom CSS untuk mempercantik UI
# Custom CSS untuk mempercantik UI
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📌 Menu Utama")
    selected = st.selectbox("Navigasi Ke:", ["🏠 Beranda", "🚀 Portofolio Proyek", "📊 Keahlian Teknis", "📧 Kontak"])
    st.write("---")
    st.info("Athaillah Tri Naufaldo\n\nIT Student @ Univ. Aisyiyah Palembang")

# ==========================================
# 🏠 HALAMAN BERANDA
# ==========================================
if selected == "🏠 Beranda":
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        if os.path.exists(FOTO_PROFIL):
            st.image(FOTO_PROFIL, width=280)
        else:
            st.image("https://via.placeholder.com/280x350.png?text=Foto+Profil", caption="Simulasi Foto")
            st.warning("Foto tidak ditemukan di folder path.")

    with col2:
        st.title("Athaillah Tri Naufaldo")
        st.subheader("Data Analyst | Business Consultant | IT Enthusiast")
        st.write("""
        Saya adalah mahasiswa IT yang berfokus pada **Data Analytics** dan **Pasar Keuangan**. 
        Memiliki ketertarikan kuat dalam mengubah data mentah menjadi wawasan bisnis yang berharga, 
        serta merancang model bisnis startup yang berkelanjutan.
        """)
        
        # Download Button CV
        if os.path.exists(FILE_CV):
            with open(FILE_CV, "rb") as f:
                st.download_button("📂 Download Professional CV (PDF)", f, "CV_Athaillah.pdf", "application/pdf")
        else:
            st.button("📂 CV Belum Tersedia", disabled=True)

# ==========================================
# 🚀 HALAMAN PROYEK (VERSI INTERAKTIF)
# ==========================================
elif selected == "🚀 Portofolio Proyek":
    st.title("Proyek Unggulan")
    tab1, tab2, tab3 = st.tabs(["🎾 Venuu (Startup)", "💰 Finansial (Data)", "🧠 Digital Detox (PKM)"])

    # --- TAB 1: VENUU ---
    with tab1:
        st.header("Venuu - Sport Venue Marketplace")
        st.write("Solusi booking lapangan olahraga untuk masyarakat Palembang.")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Target Market", "Palembang")
        m2.metric("Revenue Model", "3k - 7k IDR", "Per Booking")
        m3.metric("Project Status", "Research & BMC")
        
        with st.expander("Lihat Analisis Model Bisnis"):
            st.write("""
            - **Problem:** Kesulitan mencari lapangan kosong secara real-time.
            - **Solution:** Platform satu pintu untuk booking dan pembayaran.
            - **Unique Value:** Biaya admin yang kompetitif dan integrasi dengan komunitas lokal.
            """)

    # --- TAB 2: FINANSIAL (INTERAKTIF) ---
    with tab2:
        st.header("Simulasi Investasi Dividen (INDF)")
        st.write("Analisis pertumbuhan yield investasi berdasarkan data historis.")
        
        # Simulasi Data Interaktif (Python Power!)
        st.subheader("Grafik Proyeksi Yield")
        tahun = np.arange(2020, 2026)
        yield_data = [3.5, 3.8, 4.2, 4.0, 4.5, 4.8] # Data dummy simulasi
        df_indf = pd.DataFrame({"Tahun": tahun, "Yield (%)": yield_data})
        
        st.line_chart(df_indf.set_index("Tahun"))
        st.caption("Visualisasi ini dibuat secara dinamis menggunakan Python & Pandas.")

    # --- TAB 3: DIGITAL DETOX ---
    with tab3:
        st.header("PKM: Digital Detox")
        st.write("Program edukasi kontrol diri (Self-Control) untuk remaja.")
        
        col_step1, col_step2, col_step3 = st.columns(3)
        col_step1.info("**Minggu 1**\nAudit penggunaan layar.")
        col_step2.success("**Minggu 2**\nPenerapan detoks konten.")
        col_step3.warning("**Minggu 3**\nEvaluasi & Habit Building.")

# ==========================================
# 📊 HALAMAN KEAHLIAN
# ==========================================
elif selected == "📊 Keahlian Teknis":
    st.title("Technical Stack")
    
    col_skill1, col_skill2 = st.columns(2)
    with col_skill1:
        st.subheader("Data & Coding")
        st.progress(90, text="Python (Data Analysis)")
        st.progress(85, text="Microsoft Excel (Advanced)")
        st.progress(70, text="SQL & Database")
    
    with col_skill2:
        st.subheader("Business & Creative")
        st.progress(95, text="Business Model Canvas")
        st.progress(80, text="CapCut Video Editing")
        st.progress(65, text="Web3 & Blockchain")

# ==========================================
# 📧 HALAMAN KONTAK
# ==========================================
elif selected == "📧 Kontak":
    st.title("Let's Collaborate!")
    with st.form("contact"):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Alamat Email")
        msg = st.text_area("Pesan Anda")
        submit = st.form_submit_button("Kirim Pesan")
        if submit:
            st.success(f"Halo {name}, pesan Anda sudah terkirim (Simulasi)!")

# --- FOOTER ---
st.write("---")
st.caption(f"© 2026 Athaillah Tri Naufaldo | Built with ❤️ using Streamlit & Python")