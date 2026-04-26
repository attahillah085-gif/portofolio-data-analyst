import streamlit as st
import pandas as pd
import numpy as np
import os

# ==========================================
# 🎨 SETTING HALAMAN & TEMA CLOUD-SAFE
# ==========================================
st.set_page_config(page_title="Athaillah | Data Portfolio", page_icon="📈", layout="wide")

# CSS Khusus agar warna muncul di Streamlit Cloud
st.markdown("""
    <style>
    /* Background utama abu-abu muda */
    [data-testid="stAppViewContainer"] { 
        background-color: #f5f7f9 !important; 
    }
    /* Kotak Metrik Putih dengan bayangan */
    [data-testid="stMetric"] { 
        background-color: #ffffff !important; 
        padding: 20px !important; 
        border-radius: 12px !important; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important; 
        border-left: 6px solid #1E3A8A !important;
    }
    /* Warna Judul Biru Gelap Profesional */
    h1, h2, h3 { 
        color: #1E3A8A !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📌 Menu Utama")
    selected = st.selectbox("Navigasi Ke:", ["🏠 Beranda", "🚀 Portofolio Proyek", "📊 Keahlian Teknis", "📧 Kontak"])
    st.write("---")
    st.info("Athaillah Tri Naufaldo\n\nIT Student @ Univ. Aisyiyah Palembang")

# --- HOME PAGE ---
if selected == "🏠 Beranda":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        if os.path.exists("foto.png"):
            st.image("foto.png", width=280)
        else:
            st.image("https://via.placeholder.com/280x350.png?text=Foto+Athaillah", caption="Simulasi Foto Profil")
    
    with col2:
        st.title("Athaillah Tri Naufaldo")
        st.subheader("Data Analyst | Business Consultant | IT Enthusiast")
        st.write("""
        Mahasiswa IT yang fokus pada analisis data dan pasar keuangan. 
        Berpengalaman dalam merancang roadmap bisnis startup dan program edukasi self-control.
        """)
        
        if os.path.exists("cv.pdf"):
            with open("cv.pdf", "rb") as f:
                st.download_button("📂 Download CV (PDF)", f, "CV_Athaillah.pdf", "application/pdf")

# --- PROJECTS PAGE ---
elif selected == "🚀 Portofolio Proyek":
    st.title("Proyek Unggulan")
    tab1, tab2, tab3 = st.tabs(["🎾 Venuu (Startup)", "💰 Finansial (Data)", "🧠 Digital Detox (PKM)"])

    with tab1:
        st.header("Venuu - Sport Venue Marketplace")
        m1, m2, m3 = st.columns(3)
        m1.metric("Target Market", "Palembang")
        m2.metric("Revenue Model", "3k - 7k IDR", "Per Booking")
        m3.metric("Project Status", "Research & BMC")

    with tab2:
        st.header("Simulasi Investasi Dividen (INDF)")
        tahun = np.arange(2020, 2026)
        yield_data = [3.5, 3.8, 4.2, 4.0, 4.5, 4.8] 
        df_indf = pd.DataFrame({"Tahun": tahun, "Yield (%)": yield_data})
        st.line_chart(df_indf.set_index("Tahun"))

    with tab3:
        st.header("PKM: Digital Detox")
        st.info("**Self-Control Program** untuk membantu remaja mengelola penggunaan teknologi.")

# --- SKILLS PAGE ---
elif selected == "📊 Keahlian Teknis":
    st.title("Technical Stack")
    col_a, col_b = st.columns(2)
    with col_a:
        st.progress(90, text="Python (Data Analysis)")
        st.progress(85, text="Microsoft Excel")
    with col_b:
        st.progress(95, text="Business Model Canvas")
        st.progress(80, text="Video Editing (CapCut)")

# --- CONTACT PAGE ---
elif selected == "📧 Kontak":
    st.title("Mari Terhubung")
    st.write("📧 Email: athaillah@example.com")
    st.write("🔗 LinkedIn: linkedin.com/in/athaillah")

st.write("---")
st.caption("© 2026 Athaillah Tri Naufaldo | Built with Streamlit")
