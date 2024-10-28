import streamlit as st
from streamlit_chat import message
import random
import time

BPJS_HEALTHKATHON_LOGO = "images/bpjshealthkathon.png"
BPJS_LOGO = "images/bpjs.png"
HEALTHKATHON_LOGO = "images/healthkathon.png"

# TANYAPERMENKU_LOGO = "images/tanyapermenku.png"
# HORIZONTAL_TANYAPERMENKU_LOGO = "images/horizontal_tanyapermenku.png"

st.logo(BPJS_HEALTHKATHON_LOGO, icon_image=BPJS_HEALTHKATHON_LOGO, size="large")
st.sidebar.markdown("Riwayat Chat")

st.title("tanyaPermenKu")
st.markdown("##### Virtual Assistant untuk Permenkes dengan Retrieval Augmented Generation (RAG)") 

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: Arial, sans-serif;
        z-index: 9999; /* Ensures footer stays on top */
    }
    .footer p {
        margin: 0;
        padding-right: 10px;
    }
    .footer img {
        height: 30px;
        vertical-align: middle;
    }
    </style>
    <div class="footer">
        <p>Made with ❤️ by MiloZhegar for Healthkathon 2024</p>
        <img src="https://github.com/user-attachments/assets/90875f00-2f11-4228-b5e9-430ab74738ed" alt="Healthkathon 2024 logo">
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Tanyakan Seputar Peraturan yang Berlaku"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    st.session_state.messages.append({"role": "assistant", "content": response})
    
