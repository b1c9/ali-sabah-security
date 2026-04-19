import streamlit as st
import time

# 1. إعدادات الهيبة السيبرانية - جعل الصفحة عريضة
st.set_page_config(page_title="الرادع الرقمي", layout="wide")

# 2. هندسة الواجهة (CSS) - جعل الصورة هي الموقع بالكامل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    /* جعل الصورة خلفية كاملة ومثبتة للمتصفح */
    .stApp {
        background-image: url('https://i.imgur.com/8ae491e.png'); /* رابط الصورة مالتك */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        direction: rtl;
    }

    /* إخفاء عناصر Streamlit الافتراضية المزعجة (Header/Footer) */
    #MainMenu, header, footer {visibility: hidden;}
    
    /* حاوية "ذكية" لوضع خانة الإدخال فوق الصورة بدقة */
    .target-container {
        position: absolute;
        top: 45%; /* تعديل الارتفاع بناءً على شاشة الموبايل */
        right: 15%; /* محاكاة موقع الخانة في الصورة */
        width: 70%; /* عرض الخانة */
        text-align: center;
    }

    /* تصميم خانة الإدخال البيضاوية النيون (نفس الصورة) */
    .stTextInput > div > div > input {
        background: rgba(0, 30, 60, 0.4) !important;
        border: 2px solid #00f2ff !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        padding: 15px 25px !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
        font-size: 1.2em !important;
        box-shadow: inset 0 0 15px rgba(0, 242, 255, 0.2);
    }

    /* تصميم زر "افحص" (شفاف وبيضوي) */
    .stButton > button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: bold !important;
        font-size: 1.1em !important;
        border-radius: 50px !important;
        width: 120px !important;
        height: 45px !important;
        position: absolute;
        top: 55%; /* تحت خانة الإدخال */
        right: 15%; /* نفس محاذاة الخانة */
    }
    .stButton > button:hover {
        background: rgba(0, 242, 255, 0.1) !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض خانة الإدخال والزر فوق الصورة
st.markdown('<div class="target-container">', unsafe_allow_html=True)

# خانة الإدخال (بدون عنوان فوقها)
target_url = st.text_input("", placeholder="[ ادخل الرابط المستهدف لفحصه سيبرانياً ]")

# زر افحص
if st.button("افحص"):
    if target_url:
        with st.status("جاري تشريح البيانات...", expanded=False):
            time.sleep(2)
            st.success("اكتمل التحليل الجنائي")
    else:
        st.warning("أدخل الرابط أولاً يا مهندس علي.")

st.markdown('</div>', unsafe_allow_html=True)
