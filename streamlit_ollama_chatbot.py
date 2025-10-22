import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Chipade AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for stunning UI
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main App Styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e2e 0%, #2d2d44 100%);
        border-right: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    [data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }
    
    /* Sidebar header */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #fff !important;
        font-weight: 600;
    }
    
    /* Chat Messages Container */
    [data-testid="stChatMessageContainer"] {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
    }
    
    /* User Message */
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 18px;
        padding: 15px 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    [data-testid="stChatMessage"][data-testid*="user"] p {
        color: white !important;
        font-weight: 500;
    }
    
    /* Assistant Message */
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 18px;
        padding: 15px 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
    }
    
    [data-testid="stChatMessage"][data-testid*="assistant"] p {
        color: white !important;
        font-weight: 500;
    }
    
    /* Chat Input - Simple & Clean */
    [data-testid="stChatInput"] {
        background: white;
        border-radius: 12px;
        padding: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    [data-testid="stChatInput"] textarea {
        background: white !important;
        border: none !important;
        color: #333 !important;
        font-size: 15px !important;
        padding: 10px 15px !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    [data-testid="stChatInput"] textarea::placeholder {
        color: #999 !important;
    }
    
    [data-testid="stChatInput"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
    }
    
    [data-testid="stChatInput"] button:hover {
        opacity: 0.9 !important;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Metrics */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 700;
        color: #fff !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 14px;
        color: #e0e0e0 !important;
    }
    
    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background: rgba(255, 255, 255, 0.2);
    }
    
    .stSlider [role="slider"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.5);
    }
    
    /* Title styling */
    h1 {
        color: white !important;
        font-weight: 700;
        text-align: center;
        font-size: 3.5rem;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 0;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        margin: 2rem 0;
    }
    
    /* Success message */
    .stSuccess {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        border-radius: 12px;
        padding: 15px;
        border: none;
    }
    
    /* Chat container scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Avatar styling */
    [data-testid="chatAvatarIcon"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        margin-top: 3rem;
        padding: 20px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    /* Welcome message */
    .welcome-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px auto;
        max-width: 800px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        text-align: center;
    }
    
    .welcome-card h2 {
        color: #667eea !important;
        margin-bottom: 15px;
    }
    
    .welcome-card p {
        color: #555 !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Tagline styling */
    .tagline {
        text-align: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1rem 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        letter-spacing: 1px;
        background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    </style>
    """, unsafe_allow_html=True)


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are an Adaptive and Intelligent AI assistant capable of helping with diverse topics including technology, education, business, creative writing, problem-solving, and everyday tasks. Adjust your response style based on context—be technical when needed, simple for beginners, creative for brainstorming, and professional for work-related queries. When needed, ask clarifying questions to better understand the user's needs. Always prioritize clarity and usefulness. Your name is Chipade.")
    ]

if "llm" not in st.session_state:
    st.session_state.llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.7,
        verbose=False,
        num_thread=10
    )

# Header
st.markdown("<h1>🤖 Chipade AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>Democratize People by AI</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✨ Powered by Ollama (Llama3.2:3b) - Your Intelligent Conversation Partner</p>", unsafe_allow_html=True)

# Sidebar for settings and info
with st.sidebar:
    st.markdown("### ⚙️ Settings & Controls")
    st.markdown("---")
    
    # Model info card
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
        <h4 style='margin: 0; color: #fff;'>🔮 Active Model</h4>
        <p style='margin: 5px 0 0 0; color: #e0e0e0;'>Llama3.2:3b (Local)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Temperature slider
    st.markdown("##### 🌡️ Temperature")
    temperature = st.slider(
        "Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="🎨 Lower = More focused & precise\n🌟 Higher = More creative & diverse",
        label_visibility="collapsed"
    )
    
    # Temperature indicator
    if temperature < 0.3:
        temp_label = "❄️ Very Focused"
    elif temperature < 0.5:
        temp_label = "🎯 Balanced"
    elif temperature < 0.7:
        temp_label = "🌈 Creative"
    else:
        temp_label = "🔥 Very Creative"
    
    st.markdown(f"<p style='text-align: center; color: #fff; margin-top: -10px;'>{temp_label}</p>", unsafe_allow_html=True)
    
    # Update temperature if changed
    if temperature != st.session_state.llm.temperature:
        st.session_state.llm.temperature = temperature
    
    st.markdown("---")
    
    # Action buttons
    st.markdown("##### 🎮 Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Clear", use_container_width=True, help="Clear chat history"):
            st.session_state.messages = [
                SystemMessage(content="You are an Adaptive and Intelligent AI assistant capable of helping with diverse topics including technology, education, business, creative writing, problem-solving, and everyday tasks. Adjust your response style based on context—be technical when needed, simple for beginners, creative for brainstorming, and professional for work-related queries. When needed, ask clarifying questions to better understand the user's needs. Always prioritize clarity and usefulness. Your name is Chipade.")
            ]
            st.rerun()
    
    with col2:
        if st.button("💾 Save", use_container_width=True, help="Save conversation"):
            history = []
            for message in st.session_state.messages:
                if isinstance(message, HumanMessage):
                    role = "user"
                elif isinstance(message, AIMessage):
                    role = "assistant"
                else:
                    role = "system"
                
                history.append({
                    "role": role,
                    "content": message.content
                })
            
            conversation_data = {
                "session_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "messages": history
            }
            
            filename = f"chipade-chat-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(conversation_data, f, indent=4, ensure_ascii=False)
            
            st.success(f"✅ Saved!")
            st.toast(f"💾 {filename}", icon="✅")
    
    st.markdown("---")
    
    # Stats section
    st.markdown("### 📊 Session Stats")
    user_messages = sum(1 for msg in st.session_state.messages if isinstance(msg, HumanMessage))
    ai_messages = sum(1 for msg in st.session_state.messages if isinstance(msg, AIMessage))
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💬 Your Messages", user_messages)
    with col2:
        st.metric("🤖 AI Replies", ai_messages)
    
    # Total messages
    total_msgs = user_messages + ai_messages
    st.metric("📈 Total Exchanges", total_msgs)
    
    st.markdown("---")
    
    # Info section
    st.markdown("""
    <div style='background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; margin-top: 20px;'>
        <h4 style='margin: 0 0 10px 0; color: #fff;'>ℹ️ About Chipade</h4>
        <p style='font-size: 0.85rem; line-height: 1.5; color: #e0e0e0; margin: 0;'>
            Your intelligent AI assistant powered by locally running Ollama. 
            Completely private and secure! 🔒
        </p>
    </div>
    """, unsafe_allow_html=True)


# Welcome message for first-time users
if len(st.session_state.messages) == 1:  # Only system message exists
    st.markdown("""
    <div class='welcome-card'>
        <h2>👋 Welcome to Chipade AI!</h2>
        <p>I'm your intelligent AI assistant, ready to help you with anything you need.</p>
        <p><strong>💡 Try asking me about:</strong></p>
        <p>📚 Technology & Programming • ✍️ Creative Writing • 💼 Business & Productivity<br>
        🎓 Learning & Education • 🔧 Problem Solving • 💬 General Conversation</p>
        <p style='margin-top: 20px; font-size: 0.95rem; color: #888;'>Start by typing a message below! 👇</p>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages (excluding system message)
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user", avatar="👤"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message.content)

# Chat input
if prompt := st.chat_input("💭 Type your message here...", key="chat_input"):
    # Add user message to chat
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        try:
            for chunk in st.session_state.llm.stream(st.session_state.messages):
                full_response += chunk.content
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        except Exception as e:
            error_msg = f"⚠️ Error: {str(e)}\n\nPlease make sure Ollama is running and the model is available."
            message_placeholder.error(error_msg)
            full_response = error_msg
    
    # Add assistant response to chat history
    st.session_state.messages.append(AIMessage(content=full_response))
    st.rerun()

# Footer
st.markdown("<div class='footer'>Made with ❤️ using Streamlit & Ollama | 🔒 100% Private & Local</div>", unsafe_allow_html=True)
