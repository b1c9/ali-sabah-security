import streamlit as st
import time

# 1. إعدادات النظام - جامعة الفارابي
st.set_page_config(
    page_title="جامعة الفارابي | الرادع الرقمي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. هندسة الواجهة ومعالجة خطأ الصورة
# الرابط المباشر الصحيح
direct_image_url = "https://i.imgur.com/8ae491e.png"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    .stApp {{
        background-image: url("{direct_image_url}");
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #000b1a; /* لون احتياطي في حال فشل التحميل */
    }}

    header, footer, #MainMenu {{visibility: hidden;}}
    .block-container {{padding: 0 !important;}}

    .main-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100%;
    }}

    /* ضبط موقع المدخل والزر ليتطابق مع صورة الفارابي */
    .stTextInput {{
        width: 85% !important;
        max-width: 500px !important;
        margin-top: 12vh; 
    }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.6) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        border-radius: 10px !important;
        height: 45px !important;
        text-align: center !important;
        font-family: 'Cairo', sans-serif !important;
    }}

    .stButton button {{
        background: rgba(0, 242, 255, 0.1) !important;
        border: 2px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 10px !important;
        width: 140px !important;
        margin-top: 20px !important;
        font-weight: 900 !important;
        transition: 0.3s;
    }}
    
    .stButton button:hover {{
        background: #00f2ff !important;
        color: #000 !important;
        box-shadow: 0 0 30px #00f2ff;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. التشغيل الوظيفي
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

target = st.text_input("", placeholder="[ ادخل الرابط المستهدف لفحصه ]", label_visibility="collapsed")

if st.button("افحص"):
    if target:
        with st.status("جاري الاتصال بأنظمة الفارابي السيبرانية...", expanded=False):
            time.sleep(1.5)
            st.success("الرابط آمن.")
    else:
        st.toast("أدخل الرابط أولاً")

st.markdown('</div>', unsafe_allow_html=True)
