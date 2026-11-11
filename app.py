import streamlit as st
from google import genai
from PIL import Image

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PC TechAssist - AI Pro",
    page_icon="🤖",
    layout="wide"
)

# تخصيص الألوان والواجهة المرئية (Dark/Pro Theme)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22;
        border-radius: 8px;
        padding: 10px 20px;
        color: #c9d1d9;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #238636 !important;
        color: #ffffff !important;
    }
    .developer-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# شريط تنبيه أعلى الصفحة
st.warning("⚠️ **ملاحظة:** هذه النسخة التجريبية المدعومة بالرؤية الحاسوبية والذكاء الاصطناعي تحت التطوير المستمر ضمن مشاريع صيانة العتاد.")

# الشريط الجانبي (Sidebar)
with st.sidebar:
    st.header("⚙️ لوحة التحكم الذكية")
    st.info("مساعد ذكي متقدم لتشخيص أعطال العتاد وتحليل الصور بالذكاء الاصطناعي.")
    st.markdown("---")
    st.write("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.write("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("---")
    st.caption("الإصدار: 4.0 (Vision AI Pro)")

# تقسيم الواجهة إلى تبويبات رئيسية
tab1, tab2, tab3, tab4 = st.tabs(["👋 الترحيب ونظرة عامة", "🤖 التشخيص النصي بالـ AI", "📸 تحليل صور الأعطال (Vision)", "⚡ إرشادات الأمان (ESD)"])

# --- التبويب الأول: الترحيب ومعلومات المطور ---
with tab1:
    st.title("💻 مرحباً بك في منصة PC TechAssist الذكية")
    st.subheader("المساعد الأول المدعوم بالذكاء الاصطناعي والرؤية الحاسوبية لصيانة الحواسيب")
    
    # بطاقة تعريفية بارزة للمطور في واجهة الترحيب
    st.markdown("""
    <div class="developer-card">
        <h3>🚀 مشروع التطوير البرمجي بواسطة المطور</h3>
        <h2 style="color: #58a6ff;">Montazer Thamer Yousif</h2>
        <p><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    صُممت هذه الأداة خصيصاً لمساعدة طلاب ومهندسي صيانة الحاسوب على تحليل الأخطاء بدقة فائقة وعرض حلول هندسية فورية عبر النص أو الصور.
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("""
        🚀 **ميزات الإصدار الحديث:**
        * واجهات مستخدم مطورة وعصرية (Dark UI).
        * تحليل ذكي مدعوم بالصور الفورية للقطع.
        * قوائم فحص هندسية خطوة بخطوة.
        """)
    with col_b:
        st.info("""
        🎯 **الرؤية والأهداف:**
        * تقليل أعطال القطع أثناء الصيانة اليدوية.
        * توفير إرشادات بصرية للمبتدئين.
        * تعزيز معايير السلامة المهنية.
        """)

# --- التبويب الثاني: التشخيص النصي بالذكاء الاصطناعي ---
with tab2:
    st.header("🤖 محرك التشخيص النصي الفوري")
    st.write("اختر العطل وطبيعة المشكلة ليقوم الذكاء الاصطناعي بتوليد الحلول:")

    col1, col2 = st.columns(2)
    with col1:
        issue_type = st.selectbox("اختر طبيعة العطل الرئيسي:", [
            "مشكلة إقلاع الجهاز وأصوات الصفارة (POST/Boot)",
            "ارتفاع حرارة المعالج أو النظام (Overheating)",
            "انقطاع أو عدم استقرار الطاقة (Power/PSU)",
            "شاشة سوداء وعدم ظهور بيانات (No Display)"
        ], key="issue_text")

    with col2:
        component_type = st.selectbox("حدد القطعة المستهدفة:", [
            "الذاكرة العشوائية (RAM)",
            "المعالج (CPU) ومشتت الحرارة",
            "مزود الطاقة (Power Supply - PSU)",
            "كارت الشاشة (GPU)",
            "اللوحة الأم (Motherboard)"
        ], key="comp_text")

    user_details = st.text_area("📝 صف الأعراض الملاحظة بالتفصيل:", placeholder="مثلاً: الحاسوب يعمل وتدور المراوح لكن الشاشة لا تعرض شيئاً...")

    if st.button("✨ توليد تقرير التشخيص الذكي", key="btn_text"):
        if not user_details.strip():
            st.warning("⚠️ يرجى كتابة تفاصيل الأعراض لكي يتمكن الذكاء الاصطناعي من تحليلها!")
        else:
            with st.spinner("🔄 جاري تحليل العطل عبر النماذج الذكية..."):
                try:
                    client = genai.Client()
                    prompt = f"أنت خبير صيانة حواسيب محترف. لدينا مشكلة: العطل ({issue_type}) في القطعة ({component_type})، والتفاصيل: ({user_details}). أعطني تقريراً هندسياً مرتباً باللغة العربية يتضمن السبب المحتمل وخطوات الحل."
                    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                    st.success("✅ تم تحليل المشكلة بنجاح!")
                    st.markdown("### 📋 تقرير الصيانة الذكي:")
                    st.write(response.text)
                    st.balloons()
                except Exception as e:
                    st.error("حدث خطأ في الاتصال بمحرك الذكاء الاصطناعي. تأكد من المفتاح أو جرب لاحقاً.")

# --- التبويب الثالث: تحليل الصور والتشخيص البصري (Vision AI) ---
with tab3:
    st.header("📸 تحليل صور الأعطال والقطع بالذكاء الاصطناعي")
    st.write("ارفع صورة واضحة للوحة الأم (Motherboard)، المكثفات التالفة، أو مكان المشكلة، وسيقوم الذكاء الاصطناعي بفحصها وإعطائك تقريراً فورياً!")

    uploaded_file = st.file_uploader("📂 اختر صورة العطل (PNG, JPG, JPEG):", type=["png", "jpg", "jpeg"])
    image_prompt = st.text_input("💬 سؤال أو وصف إضافي للصورة (اختياري):", placeholder="مثلاً: هل توجد مشكلة في مكثفات هذه اللوحة الأم أو آثار احتراق؟")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="الصورة المرفوعة للفحص", use_container_width=True)

        if st.button("🔍 ابدأ الفحص البصري بالذكاء الاصطناعي"):
            with st.spinner("🧠 جاري قراءة وتحليل تفاصيل الصورة هندسياً..."):
                try:
                    client = genai.Client()
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, image_prompt if image_prompt else "قم بفحص هذه الصورة الخاصة بعتاد الحاسوب، وحدد أي تلف ظاهر أو مشكلة فنية ووضح كيفية إصلاحها."]
                    )
                    st.success("✅ تم الفحص البصري بنجاح!")
                    st.markdown("### 🔬 تقرير الفحص البصري للقطع:")
                    st.write(response.text)
                    st.balloons()
                except Exception as e:
                    st.error(f"حدث خطأ أثناء معالجة الصورة: {e}")

# --- التبويب الرابع: إرشادات الأمان ESD ---
with tab4:
    st.header("⚡ إرشادات السلامة والتفريغ الكهروستاتيكي (ESD)")
    st.warning("⚠️ **تنبيه هام جداً:** الشحنات الساتيكية في جسم الإنسان قادرة على إتلاف الدوائر الدقيقة فوراً!")
    st.markdown("""
    1. **التفريغ الأرضي:** المس جسماً معدنياً غير مفصول لتفريغ الشحنات الساكنة.
    2. **فصل الطاقة الكلية:** افصل كابل الطاقة من الحائط تماماً قبل فتح أجزاء اللوحة.
    3. **استخدام أدوات معزولة:** احرص على استخدام مفكات معزولة والعمل على أسطح غير موصلة.
    """)
                    
