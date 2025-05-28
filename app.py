import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Dynamic Chatbot",
    page_icon="💬",
    layout="wide"
)

# Initialize messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for better UI
st.markdown("""
<style>
.stTextInput>div>div>input {
    background-color: #f0f2f6;
}
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
}
.user-message {
    background-color: #e3f2fd;
    align-self: flex-end;
}
.bot-message {
    background-color: #f5f5f5;
    align-self: flex-start;
}
</style>
""", unsafe_allow_html=True)

# Main title
st.title("💬 Dynamic Chatbot")
st.markdown("---")

def get_bot_response(user_input):
    """Get response from bot based on user input"""
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm doing great, thank you for asking! How can I assist you?",
        "what is python": "Python is a high-level, interpreted programming language known for its simplicity and readability. It's great for beginners and powerful enough for experts!",
        "bye": "Goodbye! Have a great day!",
    }
    
    user_input_lower = user_input.lower().strip()
    
    # Check for matching responses
    for key in responses:
        if key in user_input_lower:
            return responses[key]
    
    return f"I understand you said: '{user_input}'. How can I help you with that?"

# Display chat messages
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">👤 You: {message["content"]}</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message">🤖 Bot: {message["content"]}</div>', 
                       unsafe_allow_html=True)

# Chat form
with st.form(key="chat_form"):
    # Chat input
    user_input = st.text_input("Your message:", placeholder="Type your message here...")
    
    # Buttons
    col1, col2 = st.columns([4, 1])
    with col1:
        submit_button = st.form_submit_button("Send")
    with col2:
        clear_button = st.form_submit_button("Clear Chat")

    if submit_button and user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Get and add bot response
        bot_response = get_bot_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
    if clear_button:
        st.session_state.messages = [] 
