import streamlit as st
import time

# 1. الإعدادات الأساسية
st.set_page_config(page_title="الرادع الرقمي", layout="centered")

# 2. بناء الواجهة السيبرانية الكاملة (محاكاة الصورة بدقة)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&family=Orbitron:wght@400;900&display=swap');
    
    .stApp {
        background-color: #000b1a;
        background-image: url('https://i.imgur.com/8ae491e.png'); /* محاكاة الخلفية الرقمية */
        background-size: cover;
        direction: rtl;
    }

    /* الحاوية الرئيسية للهيكل السيبراني */
    .main-frame {
        border: 2px solid rgba(0, 242, 255, 0.3);
        padding: 20px;
        border-radius: 15px;
        position: relative;
        background: rgba(0, 10, 25, 0.7);
        backdrop-filter: blur(5px);
    }

    /* تصميم العنوان (الرادع الرقمي) بنفس الخط والظل */
    .title-text {
        font-family: 'Cairo', sans-serif;
        font-size: 3.5em;
        font-weight: 900;
        color: #ffffff;
        text-align: center;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0055ff;
        margin-top: 20px;
    }

    /* خانة الإدخال البيضاوية (نفس الصورة تماماً) */
    .stTextInput > div > div > input {
        background: rgba(0, 30, 60, 0.5) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-size: 1.1em !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* أيقونة العدسة والدرع الجانبي */
    .input-icon {
        position: absolute;
        left: 40px;
        top: 50%;
        transform: translateY(-50%);
        color: #00f2ff;
        font-size: 1.5em;
    }

    /* زر الفحص الدائري الصغير بجانب الخانة */
    .stButton > button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 50px !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: bold !important;
        width: 100px !important;
        margin: 10px auto !important;
        display: block !important;
    }

    /* أيقونة العين والأقفال (توزيع الصورة) */
    .cyber-icons {
        display: flex;
        justify-content: space-around;
        margin-top: 30px;
        opacity: 0.7;
    }

    /* تذييل الصفحة (المطلوب: نظام الرادع الرقمي + اسمك) */
    .footer-final {
        text-align: center;
        color: #ffffff;
        font-family: 'Cairo', sans-serif;
        margin-top: 50px;
        font-size: 1.1em;
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محاكاة الهيكل البصري للصورة
st.markdown("""
    <div class="main-frame">
        <div style="text-align: center;">
            <img src="https://i.imgur.com/8ae491e.png" style="width: 100px; filter: drop-shadow(0 0 10px #00f2ff);">
        </div>
        <h1 class="title-text">الرادع الرقمي</h1>
    </div>
    """, unsafe_allow_html=True)

# 4. منطقة الإدخال والفحص
target_link = st.text_input("", placeholder="ادخل الرابط هنا للتحقق...")

if st.button("افحص"):
    if target_link:
        with st.spinner("جاري فحص حالة الأمان..."):
            time.sleep(1.5)
            st.info("نظام الرادع الرقمي يقوم بتحليل التهديدات الآن...")
    else:
        st.warning("أدخل الرابط أولاً.")

# 5. أيقونات الزينة السيبرانية (القفل والعين كما في الصورة)
st.markdown("""
    <div class="cyber-icons">
        <span>🔒</span>
        <span style="font-size: 2em; color: #00f2ff;">👁️</span>
        <span>🔒</span>
    </div>
    <div style="text-align: center; color: #00f2ff; font-family: 'Cairo'; font-size: 0.9em; margin-top: 10px;">
        جاري فحص حالة الأمان...
    </div>
    """, unsafe_allow_html=True)

# 6. التوقيع النهائي الصافي
st.markdown("""
    <div class="footer-final">
        نظام الرادع الرقمي © 2026<br>
        تم التطوير بواسطة علي صباح أحمد
    </div>
    """, unsafe_allow_html=True)
