import streamlit as st
from google import genai

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="PC TechAssist - AI Pro",
    page_icon="🤖",
    layout="wide"
)

# تصميم الألوان والعِبارات
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
st.warning("⚠️ **تنبيه:** هذه النسخة تجريبية ومدعومة بمحرك الذكاء الاصطناعي وقابلة للتطوير المستمر ضمن مشاريع الصيانة التعليمية.")

# الشريط الجانبي لإدخال المفتاح بسلامة وبدون أخطاء
with st.sidebar:
    st.header("⚙️ لوحة التحكم الذكية")
    st.info("مساعد ذكي متقدم لتشخيص أعطال عتاد الحواسيب.")
    
    # حقل آمن لإدخال المفتاح إذا لم يكن مخزناً في سحابة ستريمليت
    api_key_input = st.text_input("🔑 مفتاح Google Gemini API:", type="password", placeholder="أدخل مفتاحك هنا...")
    
    st.markdown("---")
    st.write("👨‍💻 **المطور:** Montazer Thamer Yousif")
    st.write("🏫 **التخصص:** تجميع وصيانة الحاسوب")
    st.markdown("---")
    st.caption("الإصدار: 3.1 (AI Pro)")

# التبويبات الرئيسية
tab1, tab2, tab3 = st.tabs([
    "👋 الترحيب", 
    "🤖 مساعد الذكاء الاصطناعي (حوار مباشر)", 
    "⚡ إرشادات الأمان (ESD)"
])

# --- التبويب الأول: الترحيب ---
with tab1:
    st.title("💻 مرحباً بك في منصة PC TechAssist الذكية")
    st.subheader("المساعد الأول المدعوم بالذكاء الاصطناعي لتشخيص وصيانة الحواسيب")
    
    st.markdown("""
    <div class="developer-card">
        <h3>🚀 تطوير البرمجة بواسطة المطور</h3>
        <h2 style="color: #58a6ff;">Montazer Thamer Yousif</h2>
        <p><b>التخصص:</b> تجميع وصيانة الحاسوب | إعدادية المثنى المهنية المسائية</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("أداة ذكية متكاملة مصممة خصيصاً لتتحدث معك وتحاورك كخبير صيانة محترف لمساعدتك في حل وتشخيص مشاكل الهاردوير بدقة فائقة.")

# --- التبويب الثاني: محادثة الذكاء الاصطناعي الحية ---
with tab2:
    st.header("🤖 المحاور الذكي لصيانة الحواسيب")
    st.write("اسألني عن أي عطل، مشكلة في الإقلاع، حرارة معالج، أو قطع هاردوير، وسأجيبك فوراً بخطوات دقيقة:")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "أهلاً بك يا بطل! أنا مساعدك الذكي لصيانة الحواسيب. تفضل، ما هي المشكلة أو العطل الذي تواجهه في الجهاز لكي أساعدك في حله؟"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اكتب سؤالك أو صف المشكلة هنا..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("جاري التفكير وصياغة الحل الهندسي..."):
                try:
                    # استخدام المفتاح المدخل من الشريط الجانبي أو من إعدادات البيئة
                    import os
                    key_to_use = api_key_input if api_key_input else os.getenv("GEMINI_API_KEY")
                    
                    if not key_to_use:
                        reply_text = "⚠️ تنبيه: يرجى إدخال مفتاح الـ API (`GEMINI_API_KEY`) في الشريط الجانبي (Sidebar) من القائمة الجانبية لكي يتمكن الذكاء الاصطناعي من الرد عليك!"
                    else:
                        client = genai.Client(api_key=key_to_use)
                        full_prompt = f"""
                        أنت خبير صيانة حواسيب محترف ومساعد ذكي ودود وداعم (تتحدث باللهجة العربية الواضحة والمبسطة وتساعد الطلاب والفنيين).
                        سؤال المستخدم أو المشكلة هي: {prompt}
                        أعطه إجابة دقيقة، احترافية، ومرتبة بخطوات واضحة لحل المشكلة.
                        """
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=full_prompt
                        )
                        reply_text = response.text
                        
                    st.markdown(reply_text)
                    st.session_state.messages.append({"role": "assistant", "content": reply_text})
                except Exception as e:
                    error_msg = f"عذراً، حدث خطأ: {e}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

# --- التبويب الثالث: الأمان ESD ---
with tab3:
    st.header("⚡ إرشادات السلامة والتفريغ الكهروستاتيكي (ESD)")
    st.warning("⚠️ تنبيه: الشحنات الساكنة قد تدمر اللوحات والقطع الدقيقة فور لمسها!")
    st.markdown("""
    1. **التفريغ الأرضي:** المس جسماً معدنياً غير مفصول لتفريغ الشحنات الساكنة من جسمك.
    2. **فصل الطاقة:** انزع كابل الكهرباء الرئيسي من الحائط قبل التعامل مع اللوحة الأم.
    3. **الأدوات:** استخدم مفكات معزولة وتجنب العمل على أسطح قماشية تولد كهرباء استاتيكية.
    """)
    
