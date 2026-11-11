import streamlit as st

# إعدادات الصفحة الأساسية للأداء السريع
st.set_page_config(
    page_title="PC TechAssist - Cyber Pro",
    page_icon="⚡",
    layout="wide"
)

# تصميم وتغيير جذري للواجهة والألوان (Modern Cyber UI)
st.markdown("""
    <style>
    /* خلفية التطبيق العامة */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
    }
    
    /* تنسيق التبويبات الفخمة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: rgba(17, 24, 39, 0.7);
        padding: 10px;
        border-radius: 12px;
        border: 1px solid rgba(55, 65, 81, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 12px 24px;
        color: #9ca3af;
        font-weight: 700;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #374151;
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        border: 1px solid #60a5fa !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    /* بطاقة المطور بتصميم سايبر فخم */
    .cyber-card {
        background: linear-gradient(145deg, #161e2e 0%, #0f172a 100%);
        border: 1px solid #3b82f6;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }

    /* تحسين الأزرار والقوائم المنسدلة */
    .stButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(16, 185, 129, 0.5);
    }

    /* الشريط الجانبي */
    [data-testid="stSidebar"] {
        background-color: #0d1322;
        border-right: 1px solid #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

# شريط التنبيه التجريبي بتصميم أنيق
st.markdown("""
    <div style="background-color: rgba(245, 158, 11, 0.15); border-left: 5px solid #f59e0b; padding: 12px; border-radius: 8px; margin-bottom: 20px; color: #fbbf24; font-weight: bold;">
        ⚠️ تنبيه: هذه النسخة تجريبية وقابلة للتطوير المستمر ضمن مشاريع صيانة العتاد التعليمية.
    </div>
""", unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    st.info("المساعد الهندسي المتقدم لعتاد الحواسيب.")
    st.markdown("---")
    st.markdown("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.markdown("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("---")
    st.caption("الإصدار: 3.0 (Cyber Modern)")

# التبويبات الرئيسية بالواجهة الجديدة
tab1, tab2, tab3 = st.tabs([
    "🚀 الواجهة الرئيسية", 
    "🛠️ نظام التشخيص الذكي للقطع", 
    "⚡ بروتوكولات الأمان (ESD)"
])

# --- التبويب الأول: الواجهة الرئيسية ---
with tab1:
    st.title("⚡ منصة PC TechAssist Cyber")
    st.subheader("النظام الهندسي المطور لتشخيص وصيانة عتاد الحواسيب")
    
    st.markdown("""
    <div class="cyber-card">
        <h3 style="color: #93c5fd; margin-bottom: 10px;">🚀 تطوير وهندسة البرمجيات بواسطة</h3>
        <h1 style="color: #60a5fa; text-shadow: 0 0 15px rgba(96, 165, 250, 0.5); margin: 10px 0;">Montazer Thamer Yousif</h1>
        <p style="color: #9ca3af; font-size: 1.1em;"><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("✨ تم تصميم هذه الواجهة كلياً بستايل عصري وخطوط تدرج لونية متطورة لتمنحك أداءً صاروخياً وتجربة استخدام استثنائية!")

# --- التبويب الثاني: التشخيص بالخيارات ---
with tab2:
    st.header("🛠️ محطة التشخيص الهندسي المباشر")
    st.write("حدد القطعة المستهدفة والعطل الملاحظ لاستخراج خطوات الصيانة الفورية:")
    
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

    if st.button("🚀 تنفيذ التشخيص الهندسي الفوري"):
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 15px;">
            <h3 style="color: #34d399; margin-top: 0;">✅ نتائج الفحص الميداني لـ ({component}):</h3>
            """, unsafe_allow_html=True)
        
        if "RAM" in component:
            st.markdown("1. **إخراج شرائح الذاكرة:** افصل الطاقة تماماً وأخرج الرمات من أماكنها بحذر.<br>2. **تنظيف التلامسات:** نظف الأطراف الذهبية بممحاة ناعمة لإزالة طبقة الأكسدة.<br>3. **إعادة التثبيت:** جرب تركيبها في شقوق (Slots) بديلة وتأكد من إحكام القفل.")
        elif "CPU" in component:
            st.markdown("1. **مروحة المعالج:** تأكد من إحكام توصيل سلك الـ (CPU_FAN) ومن دوران المروحة.<br>2. **المعجون الحراري:** افحص حالة المعجون واستبدله في حال جفافه التام.<br>3. **التثبيت:** تحقق من توازن مشتت الحرارة على سطح المعالج.")
        elif "Power" in component:
            st.markdown("1. **الكابلات الرئيسية:** افحص كابل الطاقة وتأكد من تثبيت موصل الـ 24-pin والـ 8-pin بإحكام.<br>2. **الأسلاك الأمامية:** تأكد من سلامة توصيلات الـ Front Panel (زر الباور).<br>3. **المصدر الكهربائي:** تأكد من سلامة الفيوز ومزود الطاقة.")
        else:
            st.markdown("1. **إعادة ضبط الـ BIOS:** أزل بطارية الـ CMOS لدقائق معدودة ثم أعد تركيبها.<br>2. **الالتماسات:** افحص خلو البورد من أي أتربة أو تلامسات معدنية خاطئة.<br>3. **المكونات:** تأكد من سلامة المكثفات والدوائر الظاهرة.")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.balloons()

# --- التبويب الثالث: الأمان ESD ---
with tab3:
    st.header("⚡ بروتوكولات الأمان والتفريغ الكهروستاتيكي (ESD)")
    st.markdown("""
    <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; padding: 20px; border-radius: 12px; color: #fca5a5;">
    <h3>⚠️ تحذير هندي هامة لحماية العتاد:</h3>
    <ol>
        <li><b>التفريغ الأرضي:</b> المس جسماً معدنياً غير مفصول لتفريغ الشحنات الساكنة من جسمك قبل لمس البورد.</li>
        <li><b>فصل الطاقة:</b> انزع كابل الكهرباء الرئيسي تماماً من الحائط قبل إجراء أي صيانة داخلية.</li>
        <li><b>الأدوات المعزولة:</b> استخدم دائماً مفكات وأدوات معزولة وتجنب العمل على أسطح قماشية تولد شحنات.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
