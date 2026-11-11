
import streamlit as st
from google import genai
from PIL import Image

# إعدادات الصفحة الأساسية للأداء السريع
st.set_page_config(
    page_title="PC TechAssist - Ultra Pro",
    page_icon="⚡",
    layout="wide"
)

# تصميم عصري وسريع جداً (UI/UX)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
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
    .quick-fix-box {
        background-color: #1f242c;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #238636;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# الشريط الجانبي السريع
with st.sidebar:
    st.header("⚡ لوحة التحكم السريعة")
    st.info("أداة التشخيص الهندسي الفائق لطلاب صيانة الحاسوب.")
    st.markdown("---")
    st.write("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.write("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("---")
    st.caption("الإصدار: 5.0 (Ultra Speed Pro)")

# التبويبات الرئيسية للسرعة والأداء
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👋 الترحيب", 
    "⚡ التشخيص السريع (ورشة المدرسة)", 
    "🤖 الذكاء الاصطناعي", 
    "📸 تحليل الصور", 
    "⚡ الأمان ESD"
])

# --- 1. الترحيب ---
with tab1:
    st.title("⚡ منصة PC TechAssist Ultra")
    st.subheader("المساعد الهندسي الفائق لصيانة وتفريغ أعطال العتاد فورياً")
    
    st.markdown("""
    <div class="developer-card">
        <h3>🚀 مشروع الصيانة والتطوير بواسطة المطور</h3>
        <h2 style="color: #58a6ff;">Montazer Thamer Yousif</h2>
        <p><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("🎯 **الأداة مصممة لتفتح بسرعة البرق وتخدمك في الفحص العملي داخل الورشة المدرسية!**")

# --- 2. التشخيص السريع للورشة (بدون انتظار وبنقرة زر) ---
with tab2:
    st.header("⚡ بنك التشخيص الفوري لأعطال الورشة المدرسية")
    st.write("اضغط على أي مشكلة شائعة تواجهك في الحواسيب لتحصل على الحل الهندسي الفوري بضغطة زر:")

    quick_issue = st.selectbox(
        "اختر العطل السريع الملاحظ في الورشة:",
        [
            "اختر عطلاً للإظهار الفوري...",
            "الحاسوب يعمل وتدور المراوح لكن لا يوجد عرض على الشاشة (No Display)",
            "الحاسوب يصدر أصوات صفارة متقطعة عند الإقلاع (POST Beeps)",
            "الحاسوب ينطفئ لوحده بعد دقائق من التشغيل (Overheating/Thermal)",
            "لا يوجد طاقة نهائياً ولا تضيء ليدات اللوحة الأم (Dead PSU/Power)"
        ]
    )

    if quick_issue != "اختر عطلاً للإظهار الفوري...":
        st.markdown("---")
        st.markdown("### 🛠️ الحل الهندسي السريع والمباشر:")
        
        if "No Display" in quick_issue:
            st.markdown("""
            <div class="quick-fix-box">
            <b>1. فحص الذاكرة (RAM):</b> أخرج شرائح الرام ونظف الأطراف الذهبية بممحاة ناعمة وجرب شريحة واحدة.<br>
            <b>2. كارت الشاشة الخارجي:</b> تأكد من إحكام توصيل كابل الشاشة أو أخرجه وجرب الشاشة على كارت البورد الداخلي (On-board).<br>
            <b>3. تفريغ الشحنات:</b> افصل طاقة البورد واỏنزع بطارية الـ CMOS لمدة دقيقة لإعادة ضبط الـ BIOS.
            </div>
            """, unsafe_allow_html=True)
        elif "POST Beeps" in quick_issue:
            st.markdown("""
            <div class="quick-fix-box">
            <b>• صفارات متقطعة قصيرة متتالية:</b> مشكلة في الذاكرة العشوائية (RAM) أو عدم تركيزها بالشكل السليم في الشقوق.<br>
            <b>• صفارة طويلة تليها قصيرة:</b> خطأ في اللوحة الأم (Motherboard) or Chipset.<br>
            <b>• صفارة طويلة مستمرة:</b> مشكلة في مزود الطاقة (Power Supply) أو الفولتية الداخلة.
            </div>
            """, unsafe_allow_html=True)
        elif "Overheating" in quick_issue:
            st.markdown("""
            <div class="quick-fix-box">
            <b>1. مروحة المعالج:</b> تأكد من دوران مروحة الـ CPU وإحكام توصيل سلك الـ (CPU_FAN).<br>
            <b>2. المعجون الحراري:</b> نظف المعجون القديم تماماً وضع طبقة جديدة طازجة فوق سطح المعالج.<br>
            <b>3. التثبيت:</b> تأكد من ربط قواعد المشتت الحراري بنمط متقاطع (X-Pattern) لضمان التلامس التام.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="quick-fix-box">
            <b>1. كابلات الباور:</b> تأكد من توصيل كابل الـ 24-pin الرئيسي وكابل الـ 4/8-pin الخاص بالمعالج جيداً.<br>
            <b>2. مفتاح التشغيل:</b> افحص توصيلات أسلاك لوحة المفتاح الأمامية (Front Panel - Power SW).<br>
            <b>3. الفيوز والكيبل:</b> جرب كابل طاقة آخر أو تأكد من سلامة فيوز مزود الطاقة (PSU).
            </div>
            """, unsafe_allow_html=True)

# --- 3. التشخيص النصي بالذكاء الاصطناعي ---
with tab3:
    st.header("🤖 محرك التشخيص الذكي المتقدم")
    user_details = st.text_area("اكتب أعراض المشكلة بدقة لكي يحللها الذكاء الاصطناعي:", placeholder="مثلاً: بورد أسوس لا يقرأ الهارد ديسك...")
    if st.button("✨ توليد التحليل الذكي"):
        if user_details:
            with st.spinner("جاري التحليل..."):
                client = genai.Client()
                res = client.models.generate_content(model='gemini-2.5-flash', contents=f"أنت خبير صيانة حواسيب. حلل المشكلة التالية باختصار وأعطني خطوات إصلاح: {user_details}")
                st.write(res.text)

# --- 4. تحليل الصور ---
with tab4:
    st.header("📸 الفحص البصري للقطع بالذكاء الاصطناعي")
    img_file = st.file_uploader("اختر صورة القطعة أو اللوحة التالفة:", type=["png", "jpg", "jpeg"])
    if img_file:
        img = Image.open(img_file)
        st.image(img, use_container_width=True)
        if st.button("🔍 فحص الصورة الآن"):
            with st.spinner("جاري قراءة الصورة..."):
                client = genai.Client()
                res = client.models.generate_content(model='gemini-2.5-flash', contents=[img, "افحص صورة عتاد الحاسوب هذه وحدد التلف وكيفية إصلاحه."])
                st.write(res.text)

# --- 5. أمان ESD ---
with tab5:
    st.header("⚡ إرشادات السلامة (ESD)")
    st.warning("تفريغ الشحنات الساكنة أساسي قبل صيانة أي بورد أو معالج في الورشة!")
    st.markdown("1. المس هيكل معدني لتفريغ الشحنات.\n2. افصل الكهرباء تماماً.\n3. استخدم مفكات معزولة.")
    
