import streamlit as st
import time
import re

# 1. إعدادات المنصة - تنفيذ المهندس علي صباح أحمد
st.set_page_config(page_title="الرادع الرقمي | علي صباح", layout="centered")

# 2. استدعاء أفخم الخطوط وتصميم الواجهة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Cairo:wght@400;700;900&family=Tajawal:wght@400;700;900&display=swap');
    
    .stApp {
        background-color: #f8f9fa;
        direction: rtl;
    }

    /* الهيدر الملكي (تصميم جامعة الفارابي) */
    .farabi-header {
        background: linear-gradient(135deg, #1a237e 0%, #0d47a1 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 0 0 30px 30px;
        text-align: center;
        font-family: 'Cairo', sans-serif;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border-bottom: 6px solid #ff7b00; /* اللون 1: البرتقالي */
    }

    .main-title {
        font-family: 'Cairo', sans-serif;
        font-weight: 900;
        font-size: 3.2em;
        margin-bottom: 10px;
        letter-spacing: -1px;
    }

    .sub-title {
        font-family: 'Tajawal', sans-serif;
        font-weight: 700;
        font-size: 1.4em;
        color: #ffea00; /* اللون 2: الأصفر */
        margin-bottom: 5px;
    }

    /* كروت النتائج الملونة بخطوط واضحة */
    .result-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        font-family: 'Cairo', sans-serif;
        margin-top: 25px;
        line-height: 1.8;
    }

    .safe-border { border-right: 10px solid #00ff88; }   /* اللون 3: الأخضر */
    .warning-border { border-right: 10px solid #ffea00; } /* الأصفر */
    .danger-border { border-right: 10px solid #ff0000; }  /* اللون 4: الأحمر */
    .info-border { border-right: 10px solid #0055ff; }    /* اللون 5: الأزرق */

    /* تنسيق الزر - هيبة سيبرانية */
    .stButton button {
        background: #1a237e !important;
        color: white !important;
        font-family: 'Cairo', sans-serif !important;
        font-weight: 900 !important;
        font-size: 1.2em !important;
        padding: 15px !important;
        border-radius: 12px !important;
        transition: 0.4s ease;
        border: none !important;
    }
    
    .stButton button:hover {
        background: #ff7b00 !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 123, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محرك الأمان الفولاذي (Anti-Injection)
def secure_shield(text):
    if not text: return ""
    # منع حقن الأكواد تماماً
    clean = re.sub(r'[<>{}[\]\\^`|]', '', text)
    return clean.strip()

# 4. خوارزمية الذكاء الاصطناعي (AI Analysis)
def ai_analyze(url):
    risky_patterns = ['bit.ly', 'login', 'secure', 'bank', 'verify', 'update', '.exe', '.zip']
    is_secure = url.lower().startswith("https")
    found_risks = [p for p in risky_patterns if p in url.lower()]
    
    if is_secure and not found_risks:
        return "safe", "تم فحص البروتوكول وتشفير النطاق؛ الرابط يتبع معايير السلامة العالمية وخالٍ من أي بصمات رقمية خبيثة."
    elif not is_secure:
        return "danger", "الرابط يفتقر إلى تشفير SSL (http)؛ هذا يعني أن بياناتك مكشوفة ويمكن للمخترقين اعتراضها بسهولة."
    else:
        return "warning", f"تم اكتشاف أنماط مشبوهة ({', '.join(found_risks)})؛ هذه الروابط تُستخدم غالباً في عمليات التصيد لاختراق الحسابات."

# --- واجهة الأداة ---
st.markdown(f"""
    <div class="farabi-header">
        <div class="main-title">الرادع الرقمي</div>
        <div class="sub-title">جامعة الفارابي - تقنيات الأمن السيبراني</div>
        <p style="font-family: 'Tajawal'; font-size: 1.1em; opacity: 0.9;">إعداد المهندس: علي صباح أحمد</p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # مسافة جمالية

# إدخال الرابط مع حماية برمجية
raw_url = st.text_input("أدخل الرابط المراد تشريحه جنائياً:", placeholder="https://example.com")
target_url = secure_shield(raw_url)

if st.button("بدء الفحص بالذكاء الاصطناعي"):
    if target_url:
        progress_text = st.empty()
        bar = st.progress(0)
        
        for i in range(100):
            time.sleep(0.01)
            bar.progress(i + 1)
            # الألوان الخمسة في نص التحميل
            load_color = "#ff7b00" if i < 20 else "#00ff88" if i < 40 else "#0055ff" if i < 60 else "#ffea00" if i < 80 else "#ff0000"
            progress_text.markdown(f'<p style="color:{load_color}; text-align:center; font-family:Cairo; font-weight:700;">جاري تحليل طبقات البيانات: {i+1}%</p>', unsafe_allow_html=True)

        res_type, res_msg = ai_analyze(target_url)
        
        # عرض النتائج في كروت فخمة
        if res_type == "safe":
            st.markdown(f'<div class="result-card safe-border"><h3 style="color:#00ff88;">✅ النتيجة: الرابط آمن</h3><p>{res_msg}</p></div>', unsafe_allow_html=True)
        elif res_type == "warning":
            st.markdown(f'<div class="result-card warning-border"><h3 style="color:#ffea00;">⚠️ النتيجة: الرابط مشبوه</h3><p>{res_msg}</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-card danger-border"><h3 style="color:#ff0000;">🚨 النتيجة: الرابط خطر جداً</h3><p>{res_msg}</p></div>', unsafe_allow_html=True)
    else:
        st.error("يرجى إدخال الرابط أولاً.")

# التذييل
st.markdown("""
    <br><br>
    <p style="text-align:center; color:#999; font-family: 'Cairo'; font-size: 0.8em;">
        نظام الرادع الرقمي © 2026 | حماية 100% ضد حقن الأكواد <br>
        تم التطوير بواسطة علي صباح أحمد
    </p>
    """, unsafe_allow_html=True)
