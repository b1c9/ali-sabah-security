import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(page_title="الرادع الرقمي", layout="centered")

# 2. بناء الواجهة السيبرانية (مطابقة للصورة 100/100)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    .stApp {
        background-color: #000b1a;
        background-image: radial-gradient(circle, #001d3d, #000814);
        direction: rtl;
    }

    /* حاوية المحتوى الرئيسي */
    .main-container {
        text-align: center;
        padding: 20px;
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 20px;
        background: rgba(0, 0, 0, 0.5);
    }

    .title-text {
        font-family: 'Cairo', sans-serif;
        font-size: 3.5em;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 20px #00f2ff;
        margin-bottom: 30px;
    }

    /* خانة الإدخال البيضاوية */
    .stTextInput > div > div > input {
        background: rgba(0, 30, 60, 0.6) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-size: 1.1em !important;
        text-align: center !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* زر افحص المخصص */
    .stButton > button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 50px !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: bold !important;
        width: 120px !important;
        height: 45px !important;
        margin: 20px auto !important;
        display: block !important;
    }

    /* الأيقونات التجميلية (القفل والعين) */
    .icon-section {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 40px;
        color: #00f2ff;
    }

    /* تذييل الصفحة (نفس طلبك بالضبط) */
    .footer-section {
        text-align: center;
        color: #ffffff;
        font-family: 'Cairo', sans-serif;
        margin-top: 60px;
        font-size: 1.1em;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محاكاة الهيكل البصري
st.markdown('<h1 class="title-text">الرادع الرقمي</h1>', unsafe_allow_html=True)

# 4. منطقة الإدخال
target_url = st.text_input("", placeholder="ادخل الرابط هنا للتحقق...")

if st.button("افحص"):
    if target_url:
        with st.spinner("جاري فحص حالة الأمان..."):
            time.sleep(1.5)
            st.info("نظام الرادع الرقمي يقوم بتحليل التهديدات الآن...")
    else:
        st.warning("أدخل الرابط أولاً.")

# 5. أيقونات الزينة السيبرانية
st.markdown("""
    <div class="icon-section">
        <span style="font-size: 1.5em;">🔒</span>
        <span style="font-size: 2.5em; text-shadow: 0 0 15px #00f2ff;">👁️</span>
        <span style="font-size: 1.5em;">🔒</span>
    </div>
    <div style="text-align: center; color: #00f2ff; font-family: 'Cairo'; margin-top: 10px;">
        جاري فحص حالة الأمان...
    </div>
    """, unsafe_allow_html=True)

# 6. التوقيع النهائي (مطابق لطلبك)
st.markdown("""
    <div class="footer-section">
        نظام الرادع الرقمي © 2026<br>
        تم التطوير بواسطة علي صباح أحمد
    </div>
    """, unsafe_allow_html=True)
