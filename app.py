import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية للأداء السريع
st.set_page_config(
    page_title="PC TechAssist - Cyber Pro",
    page_icon="⚡",
    layout="wide"
)

# تصميم وتغيير الألوان (بنفسجي، أزرق فاتح، وذهبي فاخر)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d061f 0%, #1a103c 100%);
        color: #f3f4f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: rgba(26, 16, 60, 0.8);
        padding: 10px;
        border-radius: 12px;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f1438;
        border-radius: 8px;
        padding: 12px 24px;
        color: #c084fc;
        font-weight: 700;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2e1d54;
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7c3aed 0%, #4c1d95 100%) !important;
        color: #fbbf24 !important;
        border: 1px solid #fbbf24 !important;
        box-shadow: 0 4px 15px rgba(251, 191, 11, 0.3);
    }
    .cyber-card {
        background: linear-gradient(145deg, #1b1236 0%, #110a24 100%);
        border: 1px solid #fbbf24;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(251, 191, 11, 0.15);
        margin-bottom: 25px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
        color: #0d061f;
        font-weight: 900;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 15px rgba(251, 191, 11, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(251, 191, 11, 0.6);
        background: linear-gradient(135deg, #fcd34d 0%, #b45309 100%);
    }
    [data-testid="stSidebar"] {
        background-color: #0b0517;
        border-right: 1px solid #2e1d54;
    }
    </style>
""", unsafe_allow_html=True)

# شريط التنبيه الذهبي
st.markdown("""
    <div style="background-color: rgba(251, 191, 11, 0.1); border-left: 5px solid #fbbf24; padding: 12px; border-radius: 8px; margin-bottom: 20px; color: #fde68a; font-weight: bold;">
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
    st.caption("الإصدار: 5.0 (Royal Cyber Gold)")

# التعريف الصحيح للتبويبات الأربعة
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 الواجهة الرئيسية", 
    "🛠️ نظام التشخيص الذكي", 
    "💡 المقترحات والإبلاغ",
    "⚡ بروتوكولات الأمان (ESD)"
])

# --- التبويب الأول: الواجهة الرئيسية ---
with tab1:
    st.title("⚡ منصة PC TechAssist Cyber")
    st.subheader("النظام الهندسي المطور لتشخيص وصيانة عتاد الحواسيب")
    
    st.markdown("""
    <div class="cyber-card">
        <h3 style="color: #60a5fa; margin-bottom: 10px;">🚀 تطوير وهندسة البرمجيات بواسطة</h3>
        <h1 style="color: #fbbf24; text-shadow: 0 0 15px rgba(251, 191, 11, 0.4); margin: 10px 0;">Montazer Thamer Yousif</h1>
        <p style="color: #c084fc; font-size: 1.1em;"><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("✨ المنصة جاهزة بالكامل بألوانها الملكية الجديدة ومزودة بنظام تواصل فعال!")

# --- التبويب الثاني: التشخيص الموسع ---
with tab2:
    st.header("🛠️ محطة التشخيص الهندسي المباشر (الموسعة)")
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
            <div style="background: rgba(124, 58, 237, 0.15); border: 1px solid #fbbf24; padding: 20px; border-radius: 12px; margin-top: 15px;">
            <h3 style="color: #fbbf24; margin-top: 0;">✅ نتائج الفحص الميداني لـ ({component} - العطل: {symptom}):</h3>
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

# --- تبويب الثالث: الإرسال الفعلي الحقيقي ---
with tab3:
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
                color: #fbbf24;
                font-size: 14px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #7c3aed;
                background: #1b1236;
                color: white;
                box-sizing: border-box;
                font-size: 14px;
            }
            input:focus, textarea:focus {
                border-color: #fbbf24;
                outline: none;
            }
            button {
                background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
                color: #0d061f;
                font-weight: 900;
                padding: 12px 24px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                width: 100%;
                font-size: 15px;
                box-shadow: 0 4px 15px rgba(251, 191, 11, 0.4);
            }
            button:hover {
                opacity: 0.95;
            }
        </style>
    </head>
    <body>
        <form action="https://formsubmit.co/ailailv2005@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="رسالة جديدة من تطبيق PC TechAssist!">
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

# --- تبويب الرابع: الأمان ESD ---
with tab4:
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
    
