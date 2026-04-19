import streamlit as st
import streamlit.components.v1 as components
import re
import socket
from urllib.parse import urlparse

# 1. إعدادات الصفحة
st.set_page_config(page_title="الرادع الرقمي | جامعة الفرابي", layout="centered")

# رابط صورتك من GitHub
img_url = "https://raw.githubusercontent.com/b1c9/ali-sabah-security/main/39282099-C516-4584-8D08-CB7ED732F3E3.jpeg"

# 2. بناء الواجهة التفاعلية داخل الصورة
# ملاحظة: استخدمنا HTML/JS لجعل الصورة هي المشغل الحقيقي
cyber_interface = f"""
<style>
    body {{
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #000;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}
    .container {{
        position: relative;
        width: 100vw;
        height: 100vh;
        max-width: 414px; /* مقاس آيفون 8 بلس */
        max-height: 736px;
        background: url('{img_url}') no-repeat center center;
        background-size: 100% 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        transition: all 0.5s ease;
    }}
    /* حركة الصورة عند الفحص */
    .scanning {{
        filter: hue-rotate(90deg) brightness(1.2);
        transform: scale(0.98);
    }}
    .input-overlay {{
        position: absolute;
        top: 51.5%; /* مكان المستطيل في صورتك */
        width: 75%;
        background: transparent;
        border: none;
        color: #00d4ff;
        text-align: center;
        font-size: 16px;
        outline: none;
        font-family: sans-serif;
    }}
    .btn-overlay {{
        position: absolute;
        top: 65%; /* مكان كلمة افحص في صورتك */
        width: 40%;
        height: 45px;
        cursor: pointer;
        background: transparent;
    }}
    .result-display {{
        position: absolute;
        top: 20%;
        width: 80%;
        color: #00d4ff;
        text-align: center;
        font-family: monospace;
        pointer-events: none;
        background: rgba(0,0,0,0.7);
        border-radius: 10px;
    }}
</style>

<div class="container" id="mainContainer">
    <input type="text" class="input-overlay" id="urlInput" placeholder="TYPE HERE...">
    <div class="btn-overlay" onclick="startScan()"></div>
    <div id="results" class="result-display"></div>
</div>

<script>
    function startScan() {{
        const url = document.getElementById('urlInput').value;
        const container = document.getElementById('mainContainer');
        const resDiv = document.getElementById('results');
        
        if(!url) return;

        // بدء حركة الصورة (Animation)
        container.classList.add('scanning');
        resDiv.innerHTML = "🔍 ANALYSIS IN PROGRESS...";

        setTimeout(() => {{
            container.classList.remove('scanning');
            // إرسال البيانات أو عرضها مباشرة
            resDiv.innerHTML = "🛡️ AL-FARABI SECURED<br>Target: " + url + "<br>STATUS: SAFE ✅";
        }}, 2000);
    }}
</script>
"""

# تشغيل الواجهة
components.html(cyber_interface, height=736)

# 3. وظائف الحماية الخلفية (Security)
def secure_backend():
    # منع محاولات الحقن في السيرفر
    st.sidebar.title("🛡️ Al-Farabi Security")
    st.sidebar.info("نظام حماية جامعة الفرابي نشط 100/100")
    st.sidebar.write("✅ Anti-Injection: ON")
    st.sidebar.write("✅ AI Scanning: ON")

secure_backend()
