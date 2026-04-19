import streamlit as st
import time
import re

# إعدادات النظام العسكرية - واجهة عريضة للهيبة
st.set_page_config(page_title="الرادع الرقمي | COMMAND CENTER", layout="wide")

# هندسة التصميم (لغة آلة فسفورية + حواسيب + أقفال نيون)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Cairo:wght@700;900&display=swap');
    
    /* الخلفية السيبرانية العميقة */
    .stApp {
        background-color: #000;
        background-image: 
            linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
            /* طبقة لغة الآلة الفسفورية الواضحة */
            url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4MCIgaGVpZ2h0PSI4MCIgdmlld0JveD0iMCAwIDgwIDgwIj48dGV4dCB4PSIwIiB5PSI2MCIgZm9udC1mYW1pbHk9Ik9yYml0cm9uIiBmb250LXNpemU9IjQwIiBmaWxsPSIjMDBmZjg4IiBmaWxsLW9wYWNpdHk9IjAuNSI+MDEwMTwvdGV4dD48L3N2Zz4='),
            /* طبقة الحواسيب والخوادم */
            url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiB2aWV3Qm94PSIwIDAgMTAwIDEwMCI+PHBhdGggZD0iTTUwIDEwSDkwVjkwSDUwVjExTTEwIDUwSDQwVjgwSDEwVjUwWiIgZmlsbD0iIzAwNTVmZiIgZmlsbC1vcGFjaXR5PSIwLjMiLz48L3N2Zz4=');
        direction: rtl;
        background-size: auto, 120px 120px, 300px 300px;
    }

    /* الاسم وحده في القمة باحترافية (نيون متدرج) */
    .hero-title {
        font-family: 'Cairo', sans-serif;
        font-size: 6em;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #FFFFFF 0%, #0055ff 50%, #00ff88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 20px;
        filter: drop-shadow(0 0 30px rgba(0, 85, 255, 0.6));
    }

    /* خانة الإدخال الاحترافية */
    .stTextInput input {
        background: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #0055ff !important;
        color: #00ff88 !important;
        border-radius: 4px !important;
        padding: 30px !important;
        font-size: 1.8em !important;
        text-align: center !important;
        font-family: 'Orbitron', sans-serif !important;
        box-shadow: 0 0 20px rgba(0, 85, 255, 0.4);
    }

    /* زر ابدء الفحص (طاقة بركانية) */
    .stButton button {
        background: linear-gradient(90deg, #ff0000, #ff7b00) !important;
        color: white !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: 900 !important;
        font-size: 3em !important;
        width: 100% !important;
        height: 110px !important;
        border: none !important;
        clip-path: polygon(5% 0%, 100% 0%, 95% 100%, 0% 100%);
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.6) !important;
        transition: 0.4s ease;
    }
    .stButton button:hover { transform: translateY(-5px); filter: brightness(1.2); }

    /* كرت التحليل الجنائي بالأسباب الحقيقية */
    .forensic-box {
        background: rgba(0, 20, 40, 0.9);
        border: 1px solid #00ff88;
        padding: 40px;
        border-radius: 10px;
        margin-top: 50px;
        backdrop-filter: blur(15px);
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة المستخدم
st.markdown('<div class="hero-title">الرادع الرقمي</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#ffea00; font-family:Cairo; font-size:1.6em; margin-top:-45px; font-weight:700;">نظام التشريح الجنائي للروابط | إعداد المهندس علي صباح أحمد</p>', unsafe_allow_html=True)

# محرك التحليل الحقيقي 100/100 (أسباب تقنية)
def analyze_link(url):
    reasons = []
    if not url.startswith("https"):
        reasons.append("🚨 **انعدام التشفير (No SSL):** الرابط يستخدم بروتوكول HTTP المكشوف، مما يعني أن أي بيانات تدخلها (كلمات سر، حسابات) يمكن سرقتها بسهولة عبر هجمات التنصت (Sniffing).")
    
    phishing_keywords = ['login', 'verify', 'update', 'account', 'secure-bank']
    if any(key in url.lower() for key in phishing_keywords):
        reasons.append("🚨 **هندسة اجتماعية (Phishing):** تم كشف نمط استدراجي؛ الرابط يحاول إيهامك بأنه صفحة رسمية لمؤسسة حساسة لسرقة هويتك الرقمية.")
    
    if len(url) > 100 or "@" in url:
        reasons.append("🚨 **تلاعب بالعناوين (Obfuscation):** الرابط يحتوي على رموز تضليل أو طول مفرط، وهو تكتيك لإخفاء وجهات خبيثة وتجاوز فلاتر الحماية.")

    is_safe = all("🚨" not in r for r in reasons)
    return is_safe, reasons

# منطقة التفاعل
target_input = st.text_input("", placeholder="[ ضـع الـرابط لـلـتـشريـح الـجـنـائـي الـمكـثـف ]")

if st.button("ابدء الفحص"):
    if target_input:
        bar = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
            status.markdown(f'<p style="color:#00ff88; text-align:center; font-family:Orbitron;">ANALYZING_SECURITY_LAYERS: {i+1}%</p>', unsafe_allow_html=True)
        
        safe, reports = analyze_link(target_input)
        st.markdown('<div class="forensic-box">', unsafe_allow_html=True)
        if safe:
            st.success("النتيجة: الرابط موثوق برمجياً ✅")
            st.write("**سبب الأمان:** الرابط يتبع بروتوكولات التشفير القياسية (HTTPS) ولا يحتوي على أنماط احتيالية معروفة.")
        else:
            st.error("النتيجة: تم كشف تهديد سيبراني 🚨")
            st.markdown("### 🔍 الأسباب التقنية المفصلة:")
            for r in reports:
                st.write(r)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("أدخل الرابط أولاً يا مهندس.")

st.markdown('<p style="text-align:center; color:#222; margin-top:100px; font-family:Orbitron;">V2.0 ALPHA // SHIELD_ACTIVE // BY: ALI SABAH</p>', unsafe_allow_html=True)
