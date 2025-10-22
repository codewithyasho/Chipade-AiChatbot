import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT
import io

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Chipade AI Assistant | Democratize People by AI",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are an Adaptive and Intelligent AI assistant capable of helping with diverse topics including technology, education, business, creative writing, problem-solving, and everyday tasks. Adjust your response style based on context—be technical when needed, simple for beginners, creative for brainstorming, and professional for work-related queries. When needed, ask clarifying questions to better understand the user's needs. Always prioritize clarity and usefulness. Your name is Chipade.")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "llm" not in st.session_state:
    st.session_state.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)


def generate_pdf():
    """Generate PDF from chat history"""
    buffer = io.BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#2E86AB',
        spaceAfter=30,
        alignment=TA_LEFT
    )
    
    user_style = ParagraphStyle(
        'UserStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor='#1A535C',
        spaceAfter=10,
        leftIndent=20,
        fontName='Helvetica-Bold'
    )
    
    ai_style = ParagraphStyle(
        'AIStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor='#4ECDC4',
        spaceAfter=10,
        leftIndent=20,
        fontName='Helvetica-Bold'
    )
    
    content_style = ParagraphStyle(
        'ContentStyle',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=15,
        leftIndent=40,
        rightIndent=20
    )
    
    # Add title
    title = Paragraph("Chipade AI Assistant - Chat History", title_style)
    elements.append(title)
    
    # Add date
    date_text = Paragraph(
        f"<b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        styles['Normal']
    )
    elements.append(date_text)
    elements.append(Spacer(1, 0.3*inch))
    
    # Add chat messages
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            role_paragraph = Paragraph("👤 <b>User:</b>", user_style)
        else:
            role_paragraph = Paragraph("🤖 <b>Chipade:</b>", ai_style)
        
        elements.append(role_paragraph)
        
        # Escape special characters and format content
        content = msg["content"].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        content = content.replace('\n', '<br/>')
        
        content_paragraph = Paragraph(content, content_style)
        elements.append(content_paragraph)
        elements.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(elements)
    
    # Get PDF data
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data


def clear_chat():
    """Clear chat history"""
    st.session_state.messages = [
        SystemMessage(content="You are an Adaptive and Intelligent AI assistant capable of helping with diverse topics including technology, education, business, creative writing, problem-solving, and everyday tasks. Adjust your response style based on context—be technical when needed, simple for beginners, creative for brainstorming, and professional for work-related queries. When needed, ask clarifying questions to better understand the user's needs. Always prioritize clarity and usefulness. Your name is Chipade.")
    ]
    st.session_state.chat_history = []


# Sidebar
with st.sidebar:
    st.title("🤖 Chipade AI")
    st.markdown("---")
    
    st.markdown("### Chat Controls")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        clear_chat()
        st.rerun()
    
    # Download chat as PDF button
    if len(st.session_state.chat_history) > 0:
        pdf_data = generate_pdf()
        st.download_button(
            label="📥 Download Chat as PDF",
            data=pdf_data,
            file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.button("📥 Download Chat as PDF", disabled=True, use_container_width=True)
        st.caption("Start chatting to enable download")
    
    st.markdown("---")
    st.markdown("### About")
    st.info(
        "Chipade is an adaptive AI assistant powered by Groq LLaMA 3.3.\n\n"
        "**Features:**\n"
        "- Real-time streaming responses\n"
        "- Context-aware conversations\n"
        "- PDF chat export\n"
        "- Clear chat history"
    )
    
    st.markdown("---")
    st.markdown(f"**Model:** {st.session_state.llm.model_name}")
    st.markdown(f"**Messages:** {len(st.session_state.chat_history)}")


# Main chat interface
st.title("💬 Chat with Chipade")
st.markdown(
    "<h2 style='text-align: center; color: #667eea; font-weight: 600; margin: 1rem 0; "
    "text-shadow: 0 2px 4px rgba(0,0,0,0.1);'>Democratize People by AI</h2>",
    unsafe_allow_html=True
)
st.markdown("Ask me anything! I'm here to help with technology, education, creative writing, and more.")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Display assistant response with streaming
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        for chunk in st.session_state.llm.stream(st.session_state.messages):
            full_response += chunk.content
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant message to history
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
    st.session_state.messages.append(AIMessage(content=full_response))

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>"
    "Powered by Groq LLaMA 3.3 | Built with Streamlit & LangChain"
    "</div>",
    unsafe_allow_html=True
)
