import streamlit as st
import time

# 1. إعدادات الهيبة السيبرانية
st.set_page_config(page_title="الرادع الرقمي", layout="wide")

# 2. هندسة التصميم (Glassmorphism Neon)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Cairo:wght@700;900&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001219 0%, #000000 100%);
        direction: rtl;
    }

    /* حاوية العنوان الزجاجية */
    .hero-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
    }

    .main-title {
        font-family: 'Cairo', sans-serif;
        font-size: clamp(3em, 10vw, 6em);
        font-weight: 900;
        background: linear-gradient(180deg, #FFFFFF 0%, #0055ff 50%, #00ff88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        filter: drop-shadow(0 0 25px rgba(0, 85, 255, 0.6));
    }

    .sub-title {
        font-family: 'Cairo', sans-serif;
        color: #ffea00;
        font-size: 1.4em;
        margin-top: 10px;
    }

    /* واجهة الإدخال */
    .stTextInput input {
        background: rgba(0, 0, 0, 0.8) !important;
        border: 2px solid #0055ff !important;
        color: #00ff88 !important;
        padding: 25px !important;
        font-size: 1.5em !important;
        text-align: center !important;
        font-family: 'Orbitron', sans-serif !important;
    }

    /* الزر البركاني */
    .stButton button {
        background: linear-gradient(90deg, #ff0000 0%, #ff7b00 100%) !important;
        color: white !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: 900 !important;
        font-size: 2em !important;
        width: 100% !important;
        height: 80px !important;
        border: none !important;
        clip-path: polygon(5% 0%, 100% 0%, 95% 100%, 0% 100%);
        box-shadow: 0 0 40px rgba(255, 0, 0, 0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="hero-container"><h1 class="main-title">الرادع الرقمي</h1><p class="sub-title">المركز الوطني للأمن السيبراني | قسم تشريح الروابط</p></div>', unsafe_allow_html=True)

def forensic_engine(url):
    logs = []
    if not url.startswith("https"):
        logs.append("🚨 **خطر:** الرابط يفتقر لتشفير SSL العالمي.")
    if any(k in url.lower() for k in ["login", "verify"]):
        logs.append("🚨 **تحذير:** تم رصد أنماط هندسة اجتماعية.")
    return len(logs) == 0, logs

target = st.text_input("", placeholder="[ ادخل الرابط المستهدف ]")

if st.button("ابدء الفحص"):
    if target:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
            is_safe, reports = forensic_engine(target)
            if is_safe:
                st.success("النتيجة: الرابط آمن ✅")
            else:
                st.error("النتيجة: تم كشف تهديد 🚨")
                for r in reports: st.markdown(f"> {r}")
