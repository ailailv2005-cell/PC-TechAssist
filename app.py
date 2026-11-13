import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية للأداء السريع
st.set_page_config(
    page_title="PC TechAssist - Pro Platform",
    page_icon="⚡",
    layout="wide"
)

# تصميم الواجهة والتنسيقات (Modern Cyber UI)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(17, 24, 39, 0.8);
        padding: 10px;
        border-radius: 12px;
        border: 1px solid rgba(55, 65, 81, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 10px 16px;
        color: #9ca3af;
        font-weight: 700;
        font-size: 14px;
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
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
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
        🚀 المنصة الهندسية المتكاملة لصيانة وتشخيص عتاد الحواسيب (الإصدار الاحترافي للهاكاثون).
    </div>
""", unsafe_allow_html=True)

# الشريط الجانبي
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    st.info("المنصة الشاملة لصيانة الحواسيب.")
    st.markdown("---")
    st.markdown("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.markdown("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("📚 **المؤسسة:** إعدادية المثنى المهنية المسائية")
    st.markdown("---")
    st.caption("الإصدار: 7.0 (Ultimate Pro Platform)")

# التبويبات المتكاملة للمنصة الجديدة
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚀 الرئيسية", 
    "🛠️ التشخيص الفوري", 
    "🔔 دليل صفارات البايوس", 
    "🔌 فحص التوافقية (PC Builder)", 
    "💡 المقترحات",
    "⚡ أمان ESD"
])

# --- 1. التبويب الأول: الواجهة الرئيسية ---
with tab1:
    st.title("⚡ منصة PC TechAssist Pro")
    st.subheader("النظام الهندسي المطور لتشخيص وصيانة عتاد الحواسيب")
    
    st.markdown("""
    <div class="cyber-card">
        <h3 style="color: #93c5fd; margin-bottom: 10px;">🚀 تطوير وهندسة البرمجيات بواسطة</h3>
        <h1 style="color: #60a5fa; text-shadow: 0 0 15px rgba(96, 165, 250, 0.5); margin: 10px 0;">Montazer Thamer Yousif</h1>
        <p style="color: #9ca3af; font-size: 1.1em;"><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🛠️ **تشخيص متقدم**\n\nفحص دقيق لمشاكل الهاردوير والقطع.")
    with col2:
        st.success("🔔 **رموز البايوس**\n\nتحليل صفارات اللوحة الأم واكتشاف الأعطال.")
    with col3:
        st.warning("🔌 **توافقية القطع**\n\nدليل بناء التجميعات واختيار الباور سبلاي.")

# --- 2. التبويب الثاني: التشخيص الفوري المعتاد ---
with tab2:
    st.header("🛠️ محطة التشخيص الهندسي المباشر")
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

# --- 3. التبويب الثالث: دليل صفارات البايوس (ميزة جديدة مضافة) ---
with tab3:
    st.header("🔔 دليل صفارات اللوحة الأم (BIOS Beep Codes)")
    st.write("تعرف على دلالة الأصوات الصادرة من سماعة اللوحة الأم عند التشغيل لاكتشاف العطل فوراً:")
    
    beep_choice = st.selectbox(
        "اختر نمط الصفارات المسموع:",
        [
            "صفارة واحدة قصيرة (1 Short Beep)",
            "صفارتان قصيرتان (2 Short Beeps)",
            "صفارة طويلة تليها قصيرة (1 Long, 1 Short)",
            "صفارة طويلة تليها صفارتان قصيرتان (1 Long, 2 Short)",
            "صفارات متقطعة ومستمرة (Continuous Beeps)"
        ]
    )
    
    if st.button("🔍 تحليل نمط الصفارات"):
        st.markdown("<div style='background: rgba(59, 130, 246, 0.1); border: 1px solid #3b82f6; padding: 20px; border-radius: 12px; margin-top: 15px;'>", unsafe_allow_html=True)
        if "1 Short" in beep_choice:
            st.success("🟢 **الحالة سليمة:** النظام يعمل بشكل طبيعي ولا توجد أي مشاكل في العتاد الأساسي (POST Successful).")
        elif "2 Short" in beep_choice:
            st.error("🔴 **خطأ في إعدادات الـ CMOS:** فشل اختبار الذاكرة الأساسي، أعد ضبط إعدادات البيوس أو افحص الرمات.")
        elif "1 Long, 1 Short" in beep_choice:
            st.error("🔴 **مشكلة في اللوحة الأم أو الـ PSU:** حدث خطأ عام في اللوحة الرئيسية أو في تزويد الطاقة.")
        elif "1 Long, 2 Short" in beep_choice:
            st.error("🔴 **خطأ في كارت الشاشة (GPU):** اللوحة الأم لا تستطيع التعرف على كارت الشاشة أو الذاكرة الرسومية.")
        else:
            st.error("🔴 **مشكلة حرجة في الطاقة أو الرمات:** إما أن مزود الطاقة معطل أو أن شرائح الذاكرة غير مثبتة نهائياً.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 4. التبويب الرابع: فحص التوافقية وبناء التجميعات (ميزة جديدة مضافة) ---
with tab4:
    st.header("🔌 دليل فحص توافقية القطع وحساب الطاقة (PC Builder)")
    st.write("احسب استهلاك الطاقة التقريبي لتجهيزك وتأكد من توافق المقابس:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        cpu_type = st.selectbox("نوع المعالج (CPU):", ["Intel Core i3 / i5 (فئة اقتصادية)", "Intel Core i7 / i9 (فئة عليا)", "AMD Ryzen 3 / 5", "AMD Ryzen 7 / 9"])
        gpu_type = st.selectbox("كارت الشاشة (GPU):", ["بدون كارت خارجي (معالج رسومي مدمج)", "فئة اقتصادية (GTX 1650 / RTX 3050)", "فئة متوسطة (RTX 4060 / RX 7600)", "فئة عليا (RTX 4080 / 4090)"])
    with col_b:
        ram_sticks = st.selectbox("عدد شرائح الرمات (RAM):", ["شريحة واحدة (8GB / 16GB)", "شريحتان Dual Channel (16GB / 32GB)"])
        storage_count = st.selectbox("عدد أقراص التخزين:", ["قرص واحد (SSD M.2)", "قرصان (SSD + HDD)"])

    if st.button("⚡ حساب القدرة المطلوبة للـ PSU"):
        # حساب تقديري بسيط للواط
        base_power = 150
        if "i7" in cpu_type or "Ryzen 7" in cpu_type or "i9" in cpu_type or "9" in cpu_type:
            base_power += 80
        if "اقتصادية" in gpu_type:
            base_power += 150
        elif "متوسطة" in gpu_type:
            base_power += 220
        elif "عليا" in gpu_type:
            base_power += 450
            
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 15px;">
            <h3 style="color: #34d399; margin-top: 0;">💡 نتيجة الحساب الهندسي للتجميعة:</h3>
            <p><b>القدرة الدنيا المطلوبة لمزود الطاقة (PSU):</b> <span style="color: #fbbf24; font-size: 1.2em;">{base_power + 100} Watt</span> (مع أخذ مساحة أمان 20% للحمل الزائد).</p>
            <p><b>التوصية:</b> ينصح بشراء مزود طاقة بشهادة <b>80 Plus Bronze</b> أو أعلى لضمان استقرار الفولتية وحماية القطع.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 5. التبويب الخامس: الإرسال الفعلي الحقيقي ---
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
            <input type="hidden" name="_subject" value="رسالة جديدة من منصة PC TechAssist Pro!">
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

# --- 6. التبويب السادس: الأمان ESD ---
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
    
