import streamlit as st
from openai import OpenAI

def get_api_key(key_input=None):
    if key_input:
        return key_input
    try:
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        return None

def create_client(api_key):
    return OpenAI(api_key=api_key)

def ask_openai(client, model, messages, mode="chat"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}"

def render_chat_history(history_key_suffix):
    history_key = f"pc_techassist_{history_key_suffix}"
    if history_key not in st.session_state:
        st.session_state[history_key] = [
            {"role": "assistant", "content": "أهلاً بك! أنا مساعدك الذكي لتشخيص أعطال الحواسيب وإدارة الورش. كيف يمكنني مساعدتك اليوم؟"}
        ]
    
    for message in st.session_state[history_key]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def reset_chat(history_key_suffix):
    history_key = f"pc_techassist_{history_key_suffix}"
    st.session_state[history_key] = [
        {"role": "assistant", "content": "تم مسح المحادثة. كيف يمكنني مساعدتك الآن؟"}
    ]
  
