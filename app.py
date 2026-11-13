import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PC TechAssist - Workshop Pro",
    page_icon="⚡",
    layout="wide"
)

# تنسيقات التصميم الاحترافي للنسخة المتطورة
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: rgba(17, 24, 39, 0.9);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid rgba(55, 65, 81, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 8px 14px;
        color: #9ca3af;
        font-weight: 700;
        font-size: 13px;
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
    .cyber-card {
        background: linear-gradient(145deg, #161e2e 0%, #0f172a 100%);
        border: 1px solid #3b82f6;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .metric-card {
        background: rgba(31, 41, 55, 0.6);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
    }
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
    [data-testid="stSidebar"] {
        background-color: #0d1322;
        border-right: 1px solid #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

# شريط التنبيه الاحترافي
st.markdown("""
    <div style="background-color: rgba(59, 130, 246, 0.15); border-left: 5px solid #3b82f6; padding: 12px; border-radius: 8px; margin-bottom: 20px; color: #93c5fd; font-weight: bold;">
        🚀 منصة PC TechAssist Pro Workshop: نظام إدارة صيانة الأجهزة والتشخيص الهندسي الشامل.
    </div>
""", unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    st.info("إدارة الورشة والتشخيص الذكي.")
    st.markdown("---")
    st.markdown("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.markdown("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("📚 **المؤسسة:** إعدادية المثنى المهنية المسائية")
    st.markdown("---")
    st.caption("الإصدار: 8.0 (Workshop Pro)")

# تبويبات النظام الشامل الجديد (6 أقسام احترافية)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚀 لوحة القيادة", 
    "🛠️ التشخيص الهندسي", 
    "📋 إدارة أوامر الورشة", 
    "📦 مخزون قطع الغيار", 
    "💡 الإبلاغ والمقترحات",
    "⚡ أمان ESD"
])

# --- 1. لوحة القيادة وإحصائيات الورشة ---
with tab1:
    st.title("⚡ منصة PC TechAssist Pro")
    st.subheader("نظام إدارة ورش الصيانة والتشخيص الهندسي للعتاد")
    
    st.markdown("""
    <div class="cyber-card">
        <h3 style="color: #93c5fd; margin-bottom: 10px;">🚀 تطوير وهندسة البرمجيات بواسطة</h3>
        <h1 style="color: #60a5fa; text-shadow: 0 0 15px rgba(96, 165, 250, 0.5); margin: 10px 0;">Montazer Thamer Yousif</h1>
        <p style="color: #9ca3af; font-size: 1.1em;"><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 نظرة عامة على أداء الورشة (Live Stats)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h4 style="color:#60a5fa; margin:0;">الأجهزة قيد الصيانة</h4><h2 style="color:white; margin:10px 0 0 0;">8</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h4 style="color:#34d399; margin:0;">أوامر مكتملة</h4><h2 style="color:white; margin:10px 0 0 0;">42</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h4 style="color:#fbbf24; margin:0;">نسبة النجاح</h4><h2 style="color:white; margin:10px 0 0 0;">98.5%</h2></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h4 style="color:#f87171; margin:0;">قطع منخفضة المخزون</h4><h2 style="color:white; margin:10px 0 0 0;">2</h2></div>', unsafe_allow_html=True)

# --- 2. التشخيص الهندسي المباشر ---
with tab2:
    st.header("🛠️ محطة التشخيص الهندسي المتقدم")
    st.write("حدد القطعة المستهدفة والعطل الدقيق لاستخراج خطوات الصيانة الفورية:")
    
    col1, col2 = st.columns(2)
    with col1:
        component = st.selectbox(
            "اختر القطعة المستهدفة بالفحص:",
            [
                "الذاكرة العشوائية (RAM)",
                "المعالج (CPU) ومشتت الحرارة",
                "مزود الطاقة (Power Supply - PSU)",
                "كارت الشاشة (GPU)",
                "اللوحة الأم (Motherboard)",
                "هاردوير التخزين (HDD / SSD)",
                "البطارية وساعة النظام (CMOS / BIOS)"
            ]
        )
    with col2:
        symptom = st.selectbox(
            "طبيعة المشكلة الملاحظة:",
            [
                "عدم إقلاع الجهاز أو صفارات متقطعة",
                "انقطاع تام للطاقة وعدم اشتغال المراوح",
                "ارتفاع حرارة مفاجئ واطفاء تلقائي",
                "شاشة سوداء وعدم ظهور بيانات",
                "توقف نظام التشغيل عن التعرف على القرص الصلب",
                "إعادة تشغيل عشوائية متكررة (Random Reboots)",
                "ظهور شاشة الموت الزرقاء (BSOD) عند الإقلاع"
            ]
        )

    if st.button("🚀 تنفيذ التشخيص الهندسي الفوري"):
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 15px;">
            <h3 style="color: #34d399; margin-top: 0;">✅ نتائج الفحص الميداني لـ ({component} - العطل: {symptom}):</h3>
            """, unsafe_allow_html=True)
        
        if "RAM" in component:
            st.markdown("1. **إخراج شرائح الذاكرة:** افصل الطاقة تماماً وأخرج الرمات من أماكنها بحذر.<br>2. **تنظيف التلامسات:** نظف الأطراف الذهبية بممحاة ناعمة لإزالة طبقة الأكسدة.<br>3. **إعادة التثبيت:** جرب تركيبها في شقوق (Slots) بديلة وتأكد من إحكام القفل.")
        elif "CPU" in component:
            st.markdown("1. **مروحة المعالج:** تأكد من إحكام توصيل سلك الـ (CPU_FAN) ومن دوران المروحة.<br>2. **المعجون الحراري:** افحص حالة المعجون واستبدله في حال جفافه التام.<br>3. **التثبيت:** تحقق من توازن مشتت الحرارة على سطح المعالج.")
        elif "Power" in component:
            st.markdown("1. **الكابلات الرئيسية:** افحص كابل الطاقة وتأكد من تثبيت موصل الـ 24-pin والـ 8-pin بإحكام.<br>2. **الأسلاك الأمامية:** تأكد من سلامة توصيلات الـ Front Panel (زر الباور).<br>3. **المصدر الكهربائي:** تأكد من سلامة الفيوز ومزود الطاقة.")
        elif "HDD" in component or "SSD" in component:
            st.markdown("1. **كابلات التوصيل:** تأكد من إحكام ربط كابل الـ SATA وطاقة الطاقة (أو فحص تركيب NVMe M.2 في مكانه).<br>2. **التعرف في الـ BIOS:** أعد تشغيل الجهاز وادخل إلى الـ BIOS للتأكد من أن اللوحة الأم تقرأ القرص.<br>3. **فحص القطاعات التالفة:** استخدم برامج الفحص الخارجية للتأكد من خلو الهارد من Bad Sectors.")
        elif "CMOS" in component or "BIOS" in component:
            st.markdown("1. **فحص البطارية:** قيس فولتية بطارية الـ CMOS (CR2032) ويجب أن تكون حوالي 3V.<br>2. **إعادة الضبط:** انزع البطارية أو استخدم جامبر الـ CLR_CMOS لتفريغ إعدادات الـ BIOS الفاسدة.<br>3. **تحديث الـ BIOS:** تأكد من استقرار نسخة البيوس في حال واجهت مشاكل توافقية.")
        else:
            st.markdown("1. **الفحص الشامل:** افحص كابلات الشاشة وتاكد من سلامة كارت الشاشة الخارجي أو الداخلي.<br>2. **فحص درجات الحرارة:** راقب حرارة القطع لتجنب الـ Thermal Throttling.<br>3. **الالتماسات:** تأكد من عدم وجود تلامس بين اللوحة الأم وصندوق الحاسوب (Case).")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.balloons()

# --- 3. إدارة أوامر الورشة ---
with tab3:
    st.header("📋 سجل أوامر العمل والصيانة (Workshop Tickets)")
    st.write("إدارة الأجهزة المستلمة وحالات الصيانة الحالية في الورشة:")
    
    st.markdown("""
    | رقم الطلب | اسم الزبوون | نوع الجهاز | العطل المبلغ عنه | الحالة الحالية | الفني المسؤول |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | **#WRK-101** | أحمد علي | HP ProBook Laptop | انقطاع طاقة وعدم إقلاع | 🔄 قيد الفحص | منتظر ثامر |
    | **#WRK-102** | كرار محمد | Custom PC Desktop | شاشة سوداء وصفارات | ⏳ بانتظار القطع | فني الورشة |
    | **#WRK-103** | مصطفى حسن | Dell OptiPlex | إعادة تشغيل عشوائي | ✅ تم الإصلاح | منتظر ثامر |
    """, unsafe_allow_html=True)

# --- 4. مخزون قطع الغيار ---
with tab4:
    st.header("📦 إدارة مخزون قطع الغيار (Spare Parts Inventory)")
    st.write("متابعة توفر القطع والكميات المتاحة في الورشة:")
    
    st.markdown("""
    | قطعت الغيار / المكون | الفئة | الكمية المتوفرة | حد الانخفاض | الحالة |
    | :--- | :--- | :--- | :--- | :--- |
    | **معجون حراري Arctic MX-4** | مواد استهلاكية | 15 | 5 | 🟢 متوفر |
    | **شرائح RAM 8GB DDR4** | عتاد داخلي | 6 | 2 | 🟢 متوفر |
    | **مزود طاقة PSU 500W** | طاقة | 2 | 3 | ⚠️ منخفض |
    | **بطارية CMOS CR2032** | صيانة عامة | 25 | 10 | 🟢 متوفر |
    """, unsafe_allow_html=True)

# --- 5. الإرسال الفعلي الحقيقي للمقترحات ---
with tab5:
    st.header("💡 الإبلاغ عن مشكلة أو إرسال مقترح تطويري")
    st.write("اكتب مقترحك أو العطل الجديد، وسيتم إرساله مباشرة إلى فريق التطوير:")

    components.html("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                background-color: transparent;
                color: #f3f4f6;
                font-family: Tahoma, sans-serif;
                margin: 0;
                padding: 5px;
            }
            .form-group {
                margin-bottom: 12px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #f3f4f6;
                font-size: 14px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #374151;
                background: #1f2937;
                color: white;
                box-sizing: border-box;
                font-size: 14px;
            }
            button {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                font-weight: bold;
                padding: 12px 24px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                width: 100%;
                font-size: 15px;
                box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            }
            button:hover {
                opacity: 0.95;
            }
        </style>
    </head>
    <body>
        <form action="https://formsubmit.co/ailailv2005@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="رسالة جديدة من منصة PC TechAssist Pro Workshop!">
            <input type="hidden" name="_captcha" value="false">
            
            <div class="form-group">
                <label>👤 اسمك الكريم:</label>
                <input type="text" name="name" required placeholder="اكتب اسمك هنا...">
            </div>
            
            <div class="form-group">
                <label>📧 بريدك الإلكتروني:</label>
                <input type="email" name="email" required placeholder="example@gmail.com">
            </div>
            
            <div class="form-group">
                <label>✍️ تفاصيل المقترح أو المشكلة:</label>
                <textarea name="message" required rows="3" placeholder="اكتب تفاصيل مقترحك أو العطل هنا..."></textarea>
            </div>
            
            <button type="submit">📤 إرسال إلى المطور</button>
        </form>
    </body>
    </html>
    """, height=340)

# --- 6. الأمان ESD ---
with tab6:
    st.header("⚡ بروتوكولات الأمان والتفريغ الكهروستاتيكي (ESD)")
    st.markdown("""
    <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; padding: 20px; border-radius: 12px; color: #fca5a5;">
    <h3>⚠️ تحذيرات هندسية هامة لحماية العتاد:</h3>
    <ol>
        <li><b>التفريغ الأرضي:</b> المس جسماً معدنياً غير مفصول لتفريغ الشحنات الساكنة من جسمك قبل لمس البورد.</li>
        <li><b>فصل الطاقة:</b> انزع كابل الكهرباء الرئيسي تماماً من الحائط قبل إجراء أي صيانة داخلية.</li>
        <li><b>الأدوات المعزولة:</b> استخدم دائماً مفكات وأدوات معزولة وتجنب العمل على أسطح قماشية تولد شحنات.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
                    
