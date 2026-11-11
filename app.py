import streamlit as st

# إعدادات الصفحة الأساسية للأداء السريع
st.set_page_config(
    page_title="PC TechAssist - Pro",
    page_icon="💻",
    layout="wide"
)

# تخصيص الألوان والتصميم العصري السريع
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
    </style>
""", unsafe_allow_html=True)

# شريط التنبيه بأن النسخة تجريبية وقابلة للتطوير
st.warning("⚠️ **تنبيه:** هذه النسخة تجريبية وقابلة للتطوير المستمر ضمن مشاريع صيانة العتاد التعليمية.")

# الشريط الجانبي
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    st.info("مساعد صيانة عتاد الحواسيب السريع.")
    st.markdown("---")
    st.write("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.write("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("---")
    st.caption("الإصدار: 2.2 (Options Pro)")

# التبويبات الرئيسية
tab1, tab2, tab3 = st.tabs([
    "👋 الترحيب", 
    "🔍 التشخيص اليدوي بالخيارات", 
    "⚡ إرشادات الأمان (ESD)"
])

# --- التبويب الأول: الترحيب ---
with tab1:
    st.title("💻 مرحباً بك في منصة PC TechAssist")
    st.subheader("المساعد الاحترافي لتشخيص وصيانة عتاد الحواسيب")
    
    st.markdown("""
    <div class="developer-card">
        <h3>🚀 تطوير البرمجة بواسطة المطور</h3>
        <h2 style="color: #58a6ff;">Montazer Thamer Yousif</h2>
        <p><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("أداة سريعة وخفيفة لتنظيم خطوات فحص وأعطال قطع الحاسوب بدقة وسهولة تامة عبر القوائم المختارة.")

# --- التبويب الثاني: التشخيص السريع بالخيارات ---
with tab2:
    st.header("🔍 منصة التشخيص السريع عبر الخيارات")
    
    col1, col2 = st.columns(2)
    with col1:
        component = st.selectbox(
            "اختر القطعة المستهدفة بالفحص:",
            [
                "الذاكرة العشوائية (RAM)",
                "المعالج (CPU) ومشتت الحرارة",
                "مزود الطاقة (Power Supply - PSU)",
                "كارت الشاشة (GPU)",
                "اللوحة الأم (Motherboard)"
            ]
        )
    with col2:
        symptom = st.selectbox(
            "طبيعة المشكلة الملاحظة:",
            [
                "عدم إقلاع الجهاز أو صفارات متقطعة",
                "انقطاع تام للطاقة وعدم اشتغال المراوح",
                "ارتفاع حرارة مفاجئ واطفاء تلقائي",
                "شاشة سوداء وعدم ظهور بيانات"
            ]
        )

    if st.button("🚀 عرض خطوات الإصلاح المباشرة"):
        st.success("✅ تم جلب خطوات الصيانة الفورية بنجاح:")
        st.markdown(f"### 📋 إجراءات فحص قطعتك (`{component}` - العطل: `{symptom}`):")
        
        if "RAM" in component:
            st.write("1. افصل الطاقة عن الجهاز تماماً وقم بإخراج شرائح الذاكرة.")
            st.write("2. نظف الأطراف الذهبية بعناية فائقة باستخدام ممحاة نظيفة.")
            st.write("3. أعد تركيب الشريحة في شقوق (Slots) بديلة وتأكد من سماع صوت الإحكام.")
        elif "CPU" in component:
            st.write("1. تحقق من توصيل كابل مروحة المعالج (CPU_FAN) بشكل صحيح.")
            st.write("2. افحص حالة المعجون الحراري واستبدله في حال جفافه.")
            st.write("3. تأكد من ثبات مشتت الحرارة على المعالج باتزان تام.")
        elif "Power" in component:
            st.write("1. افحص كابل الطاقة الرئيسي وتأكد من سلامة مقبس الكهرباء.")
            st.write("2. تأكد من توصيل موصلات البورد (24-pin و 8-pin) بإحكام.")
            st.write("3. تفقد سلامة الفيوز والمكثفات الداخلية لمزود الطاقة.")
        else:
            st.write("1. أعد ضبط الـ BIOS عن طريق إزالة بطارية CMOS لدقائق معدودة.")
            st.write("2. تأكد من سلامة توصيل الأسلاك الأمامية (Front Panel).")
            st.write("3. افحص خلو اللوحة الأم من أي التماسات كهربائية أو أتربة متراكمة.")
        
        st.balloons()

# --- التبويب الثالث: الأمان ESD ---
with tab3:
    st.header("⚡ إرشادات السلامة والتفريغ الكهروستاتيكي (ESD)")
    st.warning("⚠️ تنبيه: الشحنات الساكنة قد تدمر اللوحات والقطع الدقيقة فور لمسها!")
    st.markdown("""
    1. **التفريغ الأرضي:** المس جسماً معدنياً غير مفصول لتفريغ الشحنات الساكنة من جسمك.
    2. **فصل الطاقة:** انزع كابل الكهرباء الرئيسي من الحائط قبل التعامل مع اللوحة الأم.
    3. **الأدوات:** استخدم مفكات معزولة وتجنب العمل على أسطح قماشية تولد كهرباء استاتيكية.
    """)
        
