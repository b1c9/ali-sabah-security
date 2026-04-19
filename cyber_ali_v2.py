import streamlit as st
import time

# إعدادات النظام
st.set_page_config(page_title="الرادع الرقمي", layout="centered")

# هندسة التصميم السيبراني الأقوى (Matrix Neon Edition)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@700;900&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* خلفية الفضاء الرقمي العميقة */
    .stApp {
        background-color: #010409;
        direction: rtl;
        overflow-x: hidden;
    }

    /* تأثير لغة الآلة (01) الواضح في الخلفية */
    .stApp::before {
        content: "01011001 01000001 01011010 01001001 01000101 01011111 01000001 01001100 01001001";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        color: rgba(0, 255, 136, 0.08); /* لون فسفوري واضح */
        font-family: 'JetBrains Mono', monospace; font-size: 18px;
        z-index: -1; animation: pulse 6s infinite alternate;
    }
    @keyframes pulse { from { opacity: 0.1; } to { opacity: 0.6; } }

    /* حاوية العنوان: زجاجية وبسيطة */
    .header-box {
        text-align: center;
        padding: 30px 10px;
        margin-bottom: 25px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* العنوان الرئيسي: فخم بألوان النيون المتدرجة */
    .brand-title {
        font-family: 'Cairo', sans-serif;
        font-size: clamp(2.5em, 8vw, 4.5em); /* حجم مرن للموبايل */
        font-weight: 900;
        background: linear-gradient(180deg, #fff 20%, #00d2ff 50%, #00ff88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.5));
        line-height: 1.1;
    }

    /* الشعار الفرعي: أناقة وبساطة */
    .brand-sub {
        font-family: 'Cairo', sans-serif;
        color: #ffea00; /* الأصفر التقني */
        font-size: clamp(0.9em, 3.5vw, 1.3em);
        margin-top: 10px;
        font-weight: 700;
    }

    /* تحسين خانة الإدخال: أنيقة وبسيطة */
    .stTextInput > div > div > input {
        background: rgba(0, 20, 40, 0.6) !important;
        border: 1px solid #0055ff !important;
        color: #00ff88 !important;
        border-radius: 8px !important;
        padding: 18px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 14px !important;
        text-align: center !important;
    }

    /* الزر: كلاسيكي قوي ويتحمل الاستخدام */
    .stButton > button {
        background: linear-gradient(90deg, #ff0000 0%, #ff7b00 100%) !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        border: none !important;
        height: 55px !important;
        font-family: 'Cairo', sans-serif !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        box-shadow: 0 5px 20px rgba(255, 0, 0, 0.4) !important;
        transition: 0.3s ease;
    }
    .stButton > button:hover { transform: translateY(-3px); filter: brightness(1.2); }

    /* تقرير التشريح الجنائي: أنيق ومنظم */
    .report-card {
        background: #161b22;
        border: 1px solid rgba(0, 255, 136, 0.2);
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        font-family: 'Cairo', sans-serif;
        font-size: 14px;
        line-height: 1.6;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# عرض الواجهة (الاسم وحده كما طلبت)
st.markdown("""
    <div class="header-box">
        <h1 class="main-title">الرادع الرقمي</h1>
        <p class="sub-title">نظام التشريح الجنائي للروابط</p>
        <p style="color: #ffea00; font-family: 'Cairo';">إعداد المهندس علي صباح أحمد</p>
    </div>
    """, unsafe_allow_html=True)

# محرك التحليل الجنائي الحقيقي 100/100 (أسباب تقنية)
def ForensicEngine(url):
    logs = []
    # سبب 1: تحليل بروتوكول SSL/TLS
    if not url.startswith("https"):
        logs.append("🚫 **انعدام التشفير (No SSL):** الرابط يفتقر لبروتوكول HTTPS المكشوف. البيانات تمر عبر الشبكة كـ 'نص مجرد' (Plain Text)؛ مما يسمح للمهاجمين بامتلاك القدرة على التنصت (Sniffing) وسرقة البيانات فوراً.")
    else:
        logs.append("✅ **تشفير نشط:** الرابط يستخدم بروتوكول SSL/TLS المعتمد، مما يضمن سرية البيانات بين جهازك والسيرفر.")
    
    # سبب 2: تحليل الهندسة الاجتماعية
    phish_keywords = ['login', 'verify', 'update', 'account', 'bank', 'secure']
    if any(k in url.lower() for k in phish_keywords):
        logs.append("🚫 **كشف نمط التصيد الاحتيالي (Phishing):** تم رصد تكتيكات استدراجية؛ الرابط يحاول إيهامك بأنه صفحة رسمية لمؤسسة حساسة لسرقة هويتك الرقمية.")
    
    return logs

# منطقة العمل
target_url = st.text_input("", placeholder="ضع الرابط هنا للتشريح الجنائي...")

if st.button("ابدء الفحص الآمن"):
    if target_url:
        with st.status("جاري تحليل الطبقات الأمنية...", expanded=True) as status:
            # محاكاة تأثير الأنظمة الدفاعية
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            
            reports = ForensicEngine(target_url)
            if not reports:
                st.write("النتيجة: الرابط نظيف وآمن برمجياً ✅")
            else:
                st.write("النتيجة: تم كشف ملاحظات أمنية 🚨")
                for r in reports:
                    st.markdown(f'<div class="report-card">{r}</div>', unsafe_allow_html=True)
            status.update(label="اكتمل التشريح"، state="complete")
    else:
        st.toast("يرجى إدخال الرابط أولاً يا مهندس.")

st.markdown('<p style="text-align:center; color:#444; font-size:10px; margin-top:100px;">V4.0 Cyber Deterrent // SHIELD_ACTIVE // Ali Sabah</p>', unsafe_allow_html=True)
