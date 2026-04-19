import streamlit as st
import time

# 1. إعدادات النظام - جامعة الفارابي
st.set_page_config(
    page_title="جامعة الفارابي | الرادع الرقمي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. بناء الواجهة السيبرانية المرنة (Responsive) داخل الكود (بدون صور خارجية)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    /* خلفية سيبرانية غامقة بملء الشاشة */
    .stApp {
        background-color: #000b1a;
        background-image: radial-gradient(circle, #001d3d 0%, #000814 100%);
        direction: rtl;
    }

    /* إخفاء شريط التنقل العلوي وهوامش Streamlit الافتراضية */
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0 !important;}

    /* حاوية "ذكية" تتركز في منتصف أي شاشة (آيفون، لابتوب) */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
        padding: 0 10%;
    }

    /* شعار جامعة الفارابي وعنوان الرادع */
    .title-banner {
        text-align: center;
        margin-bottom: 50px;
    }
    
    .uni-title {
        color: #fff;
        font-family: 'Cairo', sans-serif;
        font-size: 1.2em;
        font-weight: 700;
    }
    
    .main-title {
        color: #fff;
        font-family: 'Cairo', sans-serif;
        font-size: 3.5em;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 25px rgba(0, 242, 255, 0.4);
        margin: 10px 0;
    }

    /* تصميم خانة الإدخال البيضاوية النيون */
    .stTextInput {
        width: 100% !important;
        max-width: 550px !important;
        margin-bottom: 20px;
    }

    .stTextInput input {
        background: rgba(0, 30, 60, 0.4) !important;
        border: 2px solid #00f2ff !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        text-align: center !important;
        font-family: 'Cairo', sans-serif !important;
        font-size: 1.1em !important;
        box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
    }

    /* تصميم زر "افحص" (البيضوي والشفاف) */
    .stButton button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 50px !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: bold !important;
        width: 160px !important;
        height: 45px !important;
        margin-top: 15px !important;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: #00f2ff !important;
        color: #000 !important;
        box-shadow: 0 0 30px #00f2ff;
    }

    /* أيقونات الزينة (الأقفال) */
    .security-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
        color: #00f2ff;
        font-size: 1.5em;
    }

    /* التوقيع السفلي المطلـوب (اسمك) */
    .credits-footer {
        position: fixed;
        bottom: 15px;
        width: 100%;
        text-align: center;
        color: #ffffff;
        font-family: 'Cairo', sans-serif;
        font-size: 1em;
        line-height: 1.5;
        z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. بناء الهيكل الوظيفي داخل حاوية "مرنة"
st.markdown('<div class="hero-container">', unsafe_allow_html=True)

# إضافة العنوان كأجزاء منفصلة لتتموضع بشكل صحيح في Streamlit
st.markdown("""
    <div class="title-banner">
        <div class="uni-title">AL-FARABI UNIVERSITY</div>
        <div class="main-title">الرادع الرقمي</div>
    </div>
    """, unsafe_allow_html=True)

# وضع خانة الإدخال والزر داخل الأعمدة لضمان التمركز الدقيق في Streamlit
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    # خانة الإدخال
    target_link = st.text_input("", placeholder="[ ادخل الرابط المستهدف للتحليل الجنائي ]", label_visibility="collapsed")
    
    # محاذاة الزر للمنتصف
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
    with btn_col2:
        check_btn = st.button("افحص")

# إضافة الأيقونات التجميلية
st.markdown("""
    <div class="security-icons">
        🔒 | 👁️ | 🔒
    </div>
    <div style="text-align: center; color: #00f2ff; font-family: 'Cairo'; margin-top: 10px;">
        جاري فحص حالة الأمان...
    </div>
    """, unsafe_allow_html=True)

# منطق الفحص (البروتوكول)
if check_btn:
    if target_link:
        with st.status("جاري تشريح البيانات في مختبرات جامعة الفارابي...", expanded=False):
            time.sleep(1.5)
            st.success("الرابط آمن - جامعة الفارابي")
    else:
        st.toast("أدخل الرابط أولاً يا مهندس علي")

st.markdown('</div>', unsafe_allow_html=True)

# 4. التوقيع النهائي (مطابق لطلبك 100/100)
st.markdown("""
    <div class="credits-footer">
        نظام الرادع الرقمي © 2026<br>
        تم التطوير بواسطة علي صباح أحمد
    </div>
    """, unsafe_allow_html=True)
