import streamlit as st
from openai import OpenAI

# إعداد الصفحة
st.set_page_config(
    page_title="PC TechAssist - AI Cyber Workshop",
    page_icon="💻",
    layout="wide"
)

# تصميم وتنسيق الثيم السيبراني الداكن
st.markdown("""
<style>
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stSidebar {
        background-color: #161b22;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
</style>
""", unsafe_allow_html=True)

st.title("💻 PC TechAssist | نظام إدارة الورش والذكاء الاصطناعي")
st.caption("منصة هندسية متكاملة لتشخيص أعطال الحواسيب، إدارة تذاكر الورش، ودعم الذكاء الاصطناعي للهاكاثون.")

# الشريط الجانبي لإعدادات الذكاء الاصطناعي
with st.sidebar:
    st.subheader("⚙️ إعدادات الذكاء الاصطناعي")
    key_input = st.text_input("أدخل مفتاح OpenAI API", type="password", placeholder="sk-...")
    
    # محاولة جلب المفتاح من الـ Secrets إذا لم يتم إدخاله يدوياً
    api_key = key_input
    if not api_key:
        try:
            api_key = st.secrets["OPENAI_API_KEY"]
        except Exception:
            api_key = None
            
    model = st.selectbox("اختر نموذج الذكاء الاصطناعي", ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"])
    st.markdown("---")
    st.info("💡 المشروع مجهز للمشاركة في هاكاثون فيريتاس للذكاء الاصطناعي.")

# تقسيم التطبيق إلى تبويبات منظمة
tab1, tab2, tab3, tab4 = st.tabs(["🏠 لوحة التحكم", "🛠️ التشخيص الهندسي", "🎫 تذاكر الورشة", "🤖 مساعد الذكاء الاصطناعي (AI)"])

with tab1:
    st.subheader("مرحباً بك يا منتظر في لوحة التحكم المركزية")
    st.write("هذه الأداة مصممة لمساعدة فنيي ومبتدئي صيانة الحواسيب في تشخيص المشاكل وإدارة قطع الغيار بكفاءة عالية.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("التذاكر النشطة", "4", "+1 اليوم")
    with col2:
        st.metric("كفاءة التشخيص", "94%", "+2.5%")
    with col3:
        st.metric("حالة النظام", "متصل بالذكاء الاصطناعي", "جاهز")

with tab2:
    st.subheader("🛠️ التشخيص السريع لأعطال العتاد")
    component = st.selectbox("اختر القطعة التي تعاني من مشكلة:", ["المعالج (CPU)", "الذاكرة العشوائية (RAM)", "مزود الطاقة (Power Supply)", "اللوحة الأم (Motherboard)"])
    
    if component == "المعالج (CPU)":
        st.write("**الأعراض الشائعة:** ارتفاع درجات الحرارة، توقف مفاجئ (Blue Screen).")
        st.info("التوصية: تحقق من معجون التبريد وحالة مروحة التبريد (Heatsink).")
    elif component == "الذاكرة العشوائية (RAM)":
        st.write("**الأعراض الشائعة:** عدم الإقلاع، صدور أصوات صفير من اللوحة الأم.")
        st.info("التوصية: قم بتنظيف أطراف الرام بإحكام أو تغيير الشق (Slot).")
    else:
        st.write("**الأعراض الشائعة:** عدم وصول طاقة للوحه، انطفاء مفاجئ.")
        st.info("التوصية: افحص الفولتية باستخدام الأوميتر والتأكد من سلامة الكابلات.")

with tab3:
    st.subheader("🎫 إدارة تذاكر الورشة وصيانة العتاد")
    ticket_name = st.text_input("اسم العميل أو الجهاز:")
    issue_desc = st.text_area("وصف العطل بالتفصيل:")
    if st.button("حفظ التذكرة هندسياً"):
        if ticket_name and issue_desc:
            st.success(f"تم حفظ تذكرة الصيانة بنجاح للجهاز: {ticket_name}")
        else:
            st.warning("الرجاء ملء كافة الحقول المطلوبة.")

with tab4:
    st.subheader("🤖 نافذة محادثة الذكاء الاصطناعي لتشخيص الأعطال")
    st.write("اسأل المساعد الذكي عن أي مشكلة في الهاردوير أو الأكواد وسيجيبك فوراً.")
    
    if not api_key:
        st.warning("⚠️الرجاء إدخال مفتاح OpenAI API في الشريط الجانبي لكي تعمل محادثة الذكاء الاصطناعي.")
    else:
        client = OpenAI(api_key=api_key)
        
        # إدارة حالة الشات في الذاكرة المؤقتة
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                {"role": "assistant", "content": "أهلاً بك! أنا مساعدك الذكي لتشخيص أعطال الحواسيب. كيف يمكنني مساعدتك في مشروع الهاكاثون اليوم؟"}
            ]
        
        # عرض رسائل السابقة
        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                
        # إدخال رسالة جديدة
        user_prompt = st.chat_input("اكتب سؤالك الهندسي هنا...")
        if user_prompt:
            st.session_state["messages"].append({"role": "user", "content": user_prompt})
            with st.chat_message("user"):
                st.markdown(user_prompt)
                
            with st.chat_message("assistant"):
                with st.spinner("جاري التحليل الهندسي عبر الذكاء الاصطناعي..."):
                    try:
                        response = client.chat.completions.create(
                            model=model,
                            messages=st.session_state["messages"],
                            temperature=0.7
                        )
                        answer = response.choices[0].message.content
                        st.markdown(answer)
                        st.session_state["messages"].append({"role": "assistant", "content": answer})
                    except Exception as e:
                        st.error(f"حدث خطأ في الاتصال: {e}")
                
