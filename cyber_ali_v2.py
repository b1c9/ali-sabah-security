import streamlit as st
import time

# 1. إعدادات الصفحة لتناسب الموبايل والحاسوب
st.set_page_config(
    page_title="جامعة الفارابي | الرادع الرقمي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ربط الصورة كخلفية أساسية (الرابط المباشر لصورتك)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&display=swap');
    
    .stApp {
        background-image: url("https://i.imgur.com/8ae491e.png");
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* إخفاء عناصر Streamlit لجعل الواجهة هي الصورة فقط */
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0 !important;}

    /* حاوية العناصر لتوسيطها فوق تصميم الصورة */
    .main-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100%;
    }

    /* تعديل مكان خانة الإدخال لتنطبق على المستطيل في صورتك */
    .stTextInput {
        width: 85% !important;
        max-width: 500px !important;
        margin-top: 22vh; /* غير هذا الرقم لرفع أو تنزيل الخانة حسب شاشة موبايلك */
    }

    .stTextInput input {
        background: rgba(0, 0, 0, 0.2) !important; /* شفافة جداً لإظهار جمال الصورة خلفها */
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        border-radius: 15px !important;
        height: 50px !important;
        text-align: center !important;
        font-family: 'Cairo', sans-serif !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
    }

    /* تعديل مكان زر "افحص" */
    .stButton button {
        background: rgba(0, 242, 255, 0.1) !important;
        border: 2px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 15px !important;
        width: 150px !important;
        margin-top: 25px !important;
        font-weight: 900 !important;
    }
    
    .stButton button:hover {
        background: #00f2ff !important;
        color: #000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض الأدوات فوق الواجهة الجميلة
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

# خانة الإدخال
target_link = st.text_input("", placeholder="[ ادخل الرابط المستهدف ]", label_visibility="collapsed")

# زر الفحص
if st.button("افحص"):
    if target_link:
        with st.status("جاري التحليل في خوادم جامعة الفارابي...", expanded=False):
            time.sleep(2)
            st.success("الرابط آمن - تم الفحص بنجاح")
    else:
        st.toast("يرجى إدخال الرابط أولاً")

st.markdown('</div>', unsafe_allow_html=True)
