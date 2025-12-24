import streamlit as st
from main import chatbot   


st.set_page_config(
    page_title="TalentScout - AI Hiring Assistant",
    layout="centered"
)

# sessions
if "session_id" not in st.session_state:
    st.session_state.session_id = "candidate_1"

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown("""
<div style="text-align:center; padding: 10px 0;">
    <h1 style="color: #2E86AB;">TalentScout - AI Hiring Assistant</h1>
    <p style="color: #555;">Practice or conduct technical interviews using smart AI prompts.</p>
</div>
<hr style="margin-top: -10px;">
""", unsafe_allow_html=True)


# form page
if not st.session_state.chat_started:

    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 30px 25px; border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05); margin-top: 20px;">
    """, unsafe_allow_html=True)

    st.markdown("### 👤 Candidate Information")

    with st.form("candidate_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email (Optional)")
            experience = st.number_input("Years of Experience", min_value=0, step=1)

        with col2:
            phone = st.text_input("Phone Number")
            location = st.text_input("Current Location")
            position = st.text_input("Desired Position")

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("### 💻 Tech Stack and Role")

        tech_stack = st.text_input("Your Tech Stack (e.g., Python, Django, OpenCV)")
        submit = st.form_submit_button("Start Interview")

        if submit:
            if name.strip() == "" or phone.strip() == "" or location.strip() == "":
                st.error("Required fields missing")
            else:
                # save candidate info
                st.session_state.user_data = {
                    "user_name": name,
                    "user_mail": email,
                    "user_experience": experience,
                    "user_phone": phone,
                    "user_location": location,
                    "user_desired_position": position,
                    "user_techstack": tech_stack
                }

                st.session_state.chat_started = True

                # FIRST BOT MESSAGE (memory-aware)
                first_message = chatbot(
                    user_input="Start interview",
                    data=st.session_state.user_data,
                    session_id=st.session_state.session_id
                )

                st.session_state.messages.append(
                    {"role": "assistant", "content": first_message}
                )

                st.rerun()

# =========================
# CHAT UI
# =========================
if st.session_state.chat_started:

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your answer...")

    if user_input:
        # show user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
        with st.chat_message("user"):
            st.markdown(user_input)

        # bot reply (MEMORY ENABLED)
        bot_reply = chatbot(           
            user_input=user_input,
            data=st.session_state.user_data,
            session_id=st.session_state.session_id

        )

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
