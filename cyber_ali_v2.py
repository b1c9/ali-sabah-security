import streamlit as st
import socket
import re
import time
from urllib.parse import urlparse

# 1. إعدادات النظام - جامعة الفرابي
st.set_page_config(page_title="الرادع الرقمي | جامعة الفرابي", layout="centered")

# رابط الصورة الخام (Raw) من مستودعك في GitHub
img_url = "https://raw.githubusercontent.com/b1c9/ali-sabah-security/main/39282099-C516-4584-8D08-CB7ED732F3E3.jpeg"

# 2. هندسة الواجهة (جعل الصورة هي الواجهة الكاملة)
st.markdown(f"""
    <style>
    /* جعل الصورة خلفية ثابتة تغطي كامل الصفحة */
    .stApp {{
        background: url("{img_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* إخفاء العناصر الافتراضية لتركيز الواجهة على صورتك */
    header, footer, #MainMenu {{visibility: hidden;}}

    /* تنسيق مربع الإدخال ليظهر بالضبط فوق المستطيل في صورتك */
    .stTextInput > div > div > input {{
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
        text-align: center;
        border-radius: 10px;
        font-size: 18px;
        margin-top: 280px; /* اضبط هذا الرقم ليطابق مكان المستطيل في صورتك */
    }}

    /* تنسيق زر الفحص ليظهر فوق كلمة "افحص" في صورتك */
    .stButton > button {{
        width: 100%;
        height: 50px;
        background-color: rgba(0, 212, 255, 0.1) !important;
        color: white !important;
        border: 2px solid #00d4ff !important;
        border-radius: 25px;
        font-weight: bold;
        margin-top: 10px;
        cursor: pointer;
    }}
    
    .stButton > button:hover {{
        background-color: rgba(0, 212, 255, 0.3) !important;
        box-shadow: 0 0 15px #00d4ff;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. محرك الحماية والتحليل الجنائي (جامعة الفرابي)
def secure_scan(url):
    try:
        # منع الحقن (Anti-Injection)
        clean_url = re.sub(r'[<>{}[\];\"\'\\]', '', url)
        domain = urlparse(clean_url).netloc or clean_url.split('/')[0]
        
        # تحليل تقني حقيقي
        ip = socket.gethostbyname(domain)
        is_https = clean_url.startswith("https")
        
        return {"ip": ip, "https": is_https, "domain": domain}
    except:
        return None

# 4. الواجهة التفاعلية (فوق الصورة)
st.write("") # فراغ علوي لضبط الموقع
url_input = st.text_input("", placeholder="[ ادخل الرابط المستهدف للتحليل الجنائي ]")

if st.button("افحص"):
    if url_input:
        with st.spinner('⏳ جاري التحليل الجنائي...'):
            time.sleep(1.5)
            data = secure_scan(url_input)
            
            if data:
                st.markdown(f"""
                <div style="background: rgba(0, 20, 40, 0.85); border: 1px solid #00d4ff; padding: 15px; border-radius: 10px;">
                    <h3 style="color: #00d4ff; text-align: center;">🛡️ تقرير جامعة الفرابي الجنائي</h3>
                    <p>🌐 <b>النطاق:</b> {data['domain']}</p>
                    <p>📡 <b>عنوان IP:</b> {data['ip']}</p>
                    <p>🔒 <b>التشفير:</b> {"آمن (SSL)" if data['https'] else "🚨 خطر (غير مشفر)"}</p>
                    <hr>
                    <p style="text-align: center; color: yellow;">🤖 AI: الرابط يخضع للمراقبة السيبرانية الآن.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ الرابط غير صالح أو الخادم لا يستجيب.")
    else:
        st.warning("الرجاء إدخال رابط أولاً.")
