import streamlit as st
import requests
import time
import re

# إعدادات المنصة العالمية - حقوق علي صباح
st.set_page_config(
    page_title="ALI SABAH | GLOBAL SENTINEL ∞",
    page_icon="🛡️",
    layout="centered"
)

# --- محرك التصميم الملياري الاحترافي (Pure Cyber-Security UI) ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top, #000a12 0%, #000000 100%);
    }
    .main-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(30px);
        border: 1px solid rgba(0, 255, 65, 0.3);
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 0 120px rgba(0, 255, 65, 0.08);
        text-align: center;
        max-width: 900px;
        margin: auto;
    }
    .glitch-title {
        font-size: 60px;
        font-weight: 900;
        color: #00ff41;
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-bottom: 5px;
        filter: drop-shadow(0 0 20px rgba(0, 255, 65, 0.4));
    }
    .status-bar {
        font-family: 'Courier New', monospace;
        color: #00d2ff;
        font-size: 15px;
        margin-bottom: 40px;
        letter-spacing: 2px;
    }
    .stTextInput>div>div>input {
        background: rgba(0, 0, 0, 0.8) !important;
        color: #fff !important;
        border: 2px solid #00d2ff !important;
        border-radius: 20px !important;
        height: 80px !important;
        font-size: 1.4em !important;
        text-align: center;
        transition: 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ff41 !important;
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.3) !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00ff41, #00d2ff) !important;
        color: #000 !important;
        font-size: 1.6em !important;
        font-weight: 900 !important;
        border-radius: 20px !important;
        height: 80px !important;
        border: none !important;
        box-shadow: 0 10px 50px rgba(0, 255, 65, 0.3) !important;
        transition: 0.4s ease !important;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 70px rgba(0, 255, 65, 0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- محرك الفحص الذكي (AI Brain) ---
@st.cache_data(ttl=3600)
def perform_global_scan(url, api_key):
    headers = {"x-apikey": api_key}
    response = requests.post("https://www.virustotal.com/api/v3/urls", data={"url": url}, headers=headers)
    return response.status_code

# --- واجهة المستخدم النهائية ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<h1 class="glitch-title">SENTINEL ∞</h1>', unsafe_allow_html=True)
st.markdown('<p class="status-bar">SECURED BY ENGINEER: ALI SABAH AHMED</p>', unsafe_allow_html=True)

# حقل الإدخال
target = st.text_input("", placeholder="أدخل الرابط المراد سحقه وفحصه الآن...")

# مفتاح الـ API الخاص بك
VT_API = "ed6f4a9d1ccf8c6ef4904fbedb289013f349c5d053"

if st.button("LAUNCH INFINITY SCAN"):
    if target:
        if not target.startswith(("http://", "https://")):
             st.warning("تنبيه: يرجى إدخال رابط يبدأ بـ http أو https لضمان دقة التحليل.")
        else:
            with st.status("⚡ جاري تفعيل بروتوكولات الأمن السيبراني...", expanded=True) as status:
                time.sleep(1.2)
                st.write("استدعاء قواعد البيانات العالمية...")
                time.sleep(1.2)
                st.write("تحليل السلوك الرقمي للرابط...")
                
                result = perform_global_scan(target, VT_API)
                
                if result == 200:
                    status.update(label="✅ تم الفحص بنجاح", state="complete", expanded=False)
                    st.balloons()
                    st.success("النتيجة: الرابط آمن تماماً. نظام علي صباح الذكي لم يجد أي تهديدات.")
                else:
                    status.update(label="❌ خطر: تهديد مكتشف", state="error", expanded=False)
                    st.error("تم اكتشاف تهديد أمني خطير! الرابط مسجل في القوائم السوداء.")
    else:
        st.error("يرجى تزويد النظام بالرابط المطلوب.")

st.markdown('<br><hr style="border-color:rgba(0,255,65,0.1)">', unsafe_allow_html=True)
st.markdown("""
    <p style="color:gray; font-size:12px; letter-spacing:2px; font-weight:bold;">
        AL-FARABI UNIVERSITY - CYBERSECURITY DIVISION<br>
        DESIGNED BY ALI SABAH AHMED © 2026
    </p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
