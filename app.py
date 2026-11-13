import streamlit as st
from openai import OpenAI

# إعداد الصفحة
st.set_page_config(
    page_title="PC TechAssist - AI",
    page_icon="💻",
    layout="centered"
)

# تصميم الثيم الداكن
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

st.title("💻 PC TechAssist")
st.caption("منصة هندسية ذكية لتشخيص أعطال الحواسيب والعتاد مدعومة بالذكاء الاصطناعي.")

# القائمة الجانبية للتنقل بسهولة على الموبايل
menu = st.sidebar.radio("📌 القائمة الرئيسية:", [
    "🏠 الرئيسية والتعريف", 
    "🛠️ التشخيص الهندسي", 
    "🤖 محادثة الذكاء الاصطناعي"
])

# مفتاح الـ API الافتراضي
api_key = "sk-..." 
try:
    if "OPENAI_API_KEY" in st.secrets:
        api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

if menu == "🏠 الرئيسية والتعريف":
    st.subheader("مرحباً بك يا منتظر في لوحة التحكم المركزية")
    st.write("هذه الأداة مصممة لمساعدة فنيي ومبتدئي صيانة الحواسيب في تشخيص المشاكل وتحديد الأعطال بدقة وسرعة عالية.")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("كفاءة التشخيص", "94%", "+2.5%")
    with col2:
        st.metric("حالة النظام", "متصل بالذكاء الاصطناعي", "جاهز")
        
    st.info("💡 استخدم القائمة الجانبية للانتقال بين التشخيص الهندسي السريع أو المحادثة المباشرة مع الذكاء الاصطناعي.")

elif menu == "🛠️ التشخيص الهندسي":
    st.subheader("🛠️ التشخيص السريع لأعطال العتاد")
    component = st.selectbox("اختر القطعة التي تعاني من مشكلة:", [
        "المعالج (CPU)", 
        "الذاكرة العشوائية (RAM)", 
        "مزود الطاقة (Power Supply)", 
        "اللوحة الأم (Motherboard)"
    ])
    
    if component == "المعالج (CPU)":
        st.write("**الأعراض الشائعة:** ارتفاع درجات الحرارة، توقف مفاجئ (Blue Screen).")
        st.info("التوصية: تحقق من معجون التبريد وحالة مروحة المشتت (Heatsink).")
    elif component == "الذاكرة العشوائية (RAM)":
        st.write("**الأعراض الشائعة:** عدم الإقلاع، صدور أصوات صفير من اللوحة الأم.")
        st.info("التوصية: قم بتنظيف أطراف الرام بإحكام أو تغيير الشق (Slot).")
    elif component == "مزود الطاقة (Power Supply)":
        st.write("**الأعراض الشائعة:** انطفاء الجهاز تماماً وعدم استجابة الباور.")
        st.info("التوصية: افحص كابلات الفولتية والتوصيلات الكهربائية.")
    else:
        st.write("**الأعراض الشائعة:** عدم ظهور بيانات على الشاشة رغم عمل المراوح.")
        st.info("التوصية: افحص بطارية الـ CMOS وشريحة البايوس.")

elif menu == "🤖 محادثة الذكاء الاصطناعي":
    st.subheader("🤖 نافذة محادثة الذكاء الاصطناعي")
    st.write("اسأل المساعد الذكي عن أي مشكلة في الهاردوير أو الصيانة وسيُجيبك فوراً.")
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "أهلاً بك يا منتظر! أنا جاهز للإجابة على أي استفسار هندسي أو صيانة حواسيب."}
        ]
    
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    user_prompt = st.chat_input("اكتب مشكلتك هنا...")
    if user_prompt:
        st.session_state["messages"].append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)
            
        with st.chat_message("assistant"):
            with st.spinner("جاري التحليل..."):
                try:
                    client = OpenAI(api_key=api_key)
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=st.session_state["messages"],
                        temperature=0.7
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state["messages"].append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error("الرجاء التأكد من صحة مفتاح OpenAI API لكي يعمل الشات.")
                    
