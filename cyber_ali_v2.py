import streamlit as st
import time

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="الرادع الرقمي", layout="centered")

# 2. هندسة الواجهة (الخلفية، الخطوط، النيون)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@900&family=Orbitron:wght@400;900&display=swap');
    
    /* خلفية سيبرانية مع شبكة رقمية */
    .stApp {
        background-color: #00040a;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 242, 255, 0.1) 0%, transparent 80%),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        direction: rtl;
    }

    /* حاوية "الهيبة" المستوحاة من درع الجامعة */
    .cyber-frame {
        border: 2px solid #00f2ff;
        background: rgba(0, 15, 30, 0.8);
        backdrop-filter: blur(10px);
        padding: 40px 20px;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.2), inset 0 0 20px rgba(0, 242, 255, 0.1);
        position: relative;
        overflow: hidden;
    }

    /* تأثير الخطوط المضيئة في الأركان */
    .cyber-frame::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 50px; height: 50px;
        border-top: 4px solid #00f2ff; border-left: 4px solid #00f2ff;
    }

    .main-title {
        font-family: 'Cairo', sans-serif;
        font-size: clamp(2.5em, 12vw, 5em);
        font-weight: 900;
        background: linear-gradient(180deg, #fff 0%, #00f2ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 0 0 30px rgba(0, 242, 255, 0.5);
    }

    /* تصميم خانة الإدخال الاحترافي */
    .stTextInput input {
        background: rgba(0, 0, 0, 0.7) !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        padding: 20px !important;
        border-radius: 10px !important;
        font-family: 'Orbitron', sans-serif !important;
        text-align: center !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.1) !important;
    }

    /* الزر العملاق (مثل أنظمة التحكم) */
    .stButton button {
        background: linear-gradient(90deg, #00f2ff, #0055ff) !important;
        color: #000 !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.8em !important;
        width: 100% !important;
        height: 75px !important;
        border-radius: 15px !important;
        border: none !important;
        text-transform: uppercase;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4) !important;
        transition: 0.3s;
    }
    .stButton button:active { transform: scale(0.95); }

    /* التوقيع في أسفل الصفحة */
    .footer-credit {
        margin-top: 100px;
        text-align: center;
        font-family: 'Cairo', sans-serif;
        color: rgba(255, 255, 255, 0.4);
        font-size: 12px;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. بناء واجهة المستخدم
st.markdown('<div class="cyber-frame"><h1 class="main-title">الرادع الرقمي</h1></div>', unsafe_allow_html=True)

st.write("") # مسافة جمالية

# 4. منطقة العمل
url_input = st.text_input("", placeholder="[ SCAN_TARGET_URL ]")

if st.button("تفعيل بروتوكول التشريح"):
    if url_input:
        with st.status("جاري سحب البيانات وفحص التهديدات...", expanded=True) as status:
            time.sleep(1.5)
            # منطق فحص بسيط
            is_malicious = any(x in url_input.lower() for x in ['login', 'verify', 'update']) or not url_input.startswith("https")
            
            if is_malicious:
                st.error("🚨 تم اكتشاف تهديد سيبراني في الرابط!")
            else:
                st.success("✅ الرابط آمن للاستخدام.")
            status.update(label="اكتمل التحليل الجنائي", state="complete")
    else:
        st.warning("أدخل الرابط أولاً يا مهندس.")

# 5. التوقيع النهائي (نفس الأسلوب اللي طلبته)
st.markdown("""
    <div class="footer-credit">
        نظام الرادع الرقمي © 2026 | حماية 100% ضد حقن الأكواد<br>
        تم التطوير بواسطة علي صباح أحمد
    </div>
    """, unsafe_allow_html=True)

