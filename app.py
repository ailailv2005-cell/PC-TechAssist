# --- تبويب المقترحات والإبلاغ المباشر (مرتبط بإيميلك) ---
with tab3:
    st.header("💡 الإبلاغ عن مشكلة أو إرسال مقترح تطويري")
    st.write("اكتب مقترحك أو العطل الجديد، وسيتم إرساله مباشرة إلى بريدك الإلكتروني (`ailailv2005@gmail.com`):")

    st.markdown("""
    <form action="https://formsubmit.co/ailailv2005@gmail.com" method="POST">
        <input type="hidden" name="_subject" value="رسالة جديدة من تطبيق PC TechAssist!">
        <input type="hidden" name="_captcha" value="false">
        
        <label style="color: #f3f4f6; font-weight: bold;">👤 اسمك الكريم:</label><br>
        <input type="text" name="name" required style="width: 100%; padding: 10px; margin: 8px 0; border-radius: 8px; border: 1px solid #374151; background: #1f2937; color: white;"><br><br>
        
        <label style="color: #f3f4f6; font-weight: bold;">📧 بريدك الإلكتروني:</label><br>
        <input type="email" name="email" required style="width: 100%; padding: 10px; margin: 8px 0; border-radius: 8px; border: 1px solid #374151; background: #1f2937; color: white;"><br><br>
        
        <label style="color: #f3f4f6; font-weight: bold;">✍️ تفاصيل المقترح أو المشكلة:</label><br>
        <textarea name="message" required rows="4" style="width: 100%; padding: 10px; margin: 8px 0; border-radius: 8px; border: 1px solid #374151; background: #1f2937; color: white;" placeholder="اكتب تفاصيل مقترحك هنا..."></textarea><br><br>
        
        <button type="submit" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; font-weight: bold; padding: 12px 24px; border: none; border-radius: 10px; cursor: pointer;">📤 إرسال إلى بريد المطور</button>
    </form>
    """, unsafe_allow_html=True)
    
