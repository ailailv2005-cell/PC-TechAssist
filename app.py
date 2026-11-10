
import streamlit as st

st.title("💻 PC TechAssist")
st.subheader("مساعد تشخيص أعطال الحاسوب - نسخة الهاكاثون")
st.write("مرحباً بك! هذا التطبيق مصمم لمساعدة المبتدئين في صيانة وتشخيص قطع الحواسيب.")

issue = st.selectbox("اختر نوع المشكلة:", ["مشكلة إقلاع (Boot)", "ارتفاع حرارة", "مشكلة شبكة"])
details = st.text_area("اكتب تفاصيل المشكلة هنا:")

if st.button("تشخيص"):
    st.success("تم استلام الطلب بنجاح!")
    if "إقلاع" in issue:
        st.info("تحقق من تركيب ذواكر الرام (RAM) وإعادة توصيلها.")
    else:
        st.warning("تحقق من تنظيف المراوح ونظام التبريد.")
        
