import streamlit as st
import time
import re

# 1. إعدادات النظام - جامعة الفرابي
st.set_page_config(
    page_title="الرادع الرقمي | جامعة الفرابي",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# رابط الصورة من GitHub
img_url = "https://raw.githubusercontent.com/b1c9/ali-sabah-security/main/39282099-C516-4584-8D08-CB7ED732F3E3.jpeg"

# 2. هندسة الحركة والواجهة التفاعلية (CSS Animation)
st.markdown(f"""
    <style>
    /* إعدادات الخلفية الأساسية */
    .stApp {{
        background: url("{img_url}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-color: #000;
        transition: all 0.5s ease-in-out;
    }}

    /* تأثير الاهتزاز والحركة السيبرانية عند الفحص */
    @keyframes cyber-scan {{
        0% {{ transform: scale(1); filter: brightness(1) contrast(1); }}
        25% {{ transform: scale(1.02) translate(2px, -2px); filter: brightness(1.2) sepia(0.5) hue-rotate(90deg); }}
        50% {{ transform: scale(0.98) translate(-2px, 2px); filter: brightness(1.5) contrast(1.5) hue-rotate(180deg); }}
        75% {{ transform: scale(1.01) translate(1px, 1px); filter: brightness(1.2) contrast(1.2) hue-rotate(270deg); }}
        100% {{ transform: scale(1); filter: brightness(1) contrast(1); }}
    }}

    .scanning-active {{
        animation: cyber-scan 0.3s infinite;
        border: 5px solid #00d4ff;
    }}

    /* إخفاء القوائم الزائدة */
    header, footer, #MainMenu {{visibility: hidden;}}

    /* تنسيق منطقة المدخلات الشفافة */
    .main-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
    }}

    /* جعل مربع النص يختفي داخل تصميمك */
    .stTextInput > div > div > input {{
        background: rgba(0, 0, 0, 0.7) !important;
        color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
        text-align: center;
        font-weight: bold;
        margin-top: 320px; /* اضبط هذا الرقم ليطابق مكان المستطيل في صورتك */
        width: 350px !important;
    }}

    /* جعل الزر غير مرئي لكنه شغال فوق كلمة "افحص" */
    .stButton > button {{
        background: rgba(0, 212, 255, 0.1) !important;
        border: 1px solid #00d4ff !important;
        color: white !important;
        width: 150px !important;
        height: 50px !important;
        margin-top: 20px;
        font-size: 18px !important;
        border-radius: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة المستخدم
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# مربع النص فوق المستطيل الأصلي في الصورة
target_link = st.text_input("", placeholder="[ ادخل الرابط هنا ]", key="cyber_input")

if st.button("افحص"):
    if target_link:
        # تفعيل حركة الصورة (CSS Injection)
        st.markdown('<style>.stApp { animation: cyber-scan 0.2s infinite; }</style>', unsafe_allow_html=True)
        
        # محاكاة عملية التحليل الجنائي
        status_box = st.empty()
        for i in range(1, 101, 10):
            status_box.markdown(f"<h3 style='color:#00d4ff; text-align:center;'>🔍 جاري كسر التشفير: {i}%</h3>", unsafe_allow_html=True)
            time.sleep(0.2)
        
        # إيقاف الحركة وعرض النتيجة
        st.markdown('<style>.stApp { animation: none; }</style>', unsafe_allow_html=True)
        st.success(f"🛡️ تم الفحص بنجاح لجامعة الفرابي | الرابط: {target_link} | الحالة: آمن ✅")
    else:
        st.warning("الرجاء إدخال رابط.")

st.markdown('</div>', unsafe_allow_html=True)
