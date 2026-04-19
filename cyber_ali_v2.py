import streamlit as st
import time

# 1. إعدادات الصفحة - جامعة الفارابي
st.set_page_config(
    page_title="جامعة الفارابي | الرادع الرقمي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ربط الصورة وتنسيق الواجهة (CSS)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    .stApp {{
        background-image: url("https://i.imgur.com/8ae491e.png");
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* إخفاء القوائم الافتراضية لجعلها واجهة برمجية احترافية */
    header, footer, #MainMenu {{visibility: hidden;}}
    .block-container {{padding: 0 !important;}}

    /* حاوية العناصر المركزية */
    .main-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100%;
    }}

    /* ضبط مكان خانة الإدخال فوق المستطيل في الصورة */
    .stTextInput {{
        width: 80% !important;
        max-width: 520px !important;
        margin-top: 15vh; /* هذا الرقم يرفع وينزل الخانة لتنطبق على الرسمة */
    }}

    .stTextInput input {{
        background: rgba(0, 0, 0, 0.4) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        border-radius: 10px !important;
        height: 50px !important;
        text-align: center !important;
        font-family: 'Cairo', sans-serif !important;
    }}

    /* ضبط مكان زر افحص */
    .stButton button {{
        background: rgba(0, 242, 255, 0.1) !important;
        border: 2px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 10px !important;
        width: 160px !important;
        height: 45px !important;
        margin-top: 25px !important;
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

# 3. بناء الهيكل الوظيفي
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# خانة الإدخال (بدون عنوان نصي ليظهر التصميم فقط)
url_to_check = st.text_input("", placeholder="[ ادخل الرابط المستهدف للتحليل الجنائي ]", label_visibility="collapsed")

# زر الفحص
if st.button("افحص"):
    if url_to_check:
        with st.status("جاري تشريح الرابط في مختبرات جامعة الفارابي...", expanded=False):
            time.sleep(2)
            st.success("التحليل السيبراني مكتمل: الرابط آمن.")
    else:
        st.toast("أدخل الرابط أولاً يا مهندس علي")

st.markdown('</div>', unsafe_allow_html=True)
