# Chipade AI Chatbot - Streamlit App

An interactive AI chatbot built with Streamlit, LangChain, and Groq's LLaMA 3.3 model.

## Features

- 🤖 **Intelligent Conversations**: Context-aware AI assistant powered by Groq LLaMA 3.3
- 💬 **Real-time Streaming**: See responses appear word by word
- 🗑️ **Clear Chat**: Reset conversation history with one click
- 📥 **PDF Export**: Download entire chat history as a formatted PDF
- 🎨 **Modern UI**: Clean and intuitive interface with Streamlit

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project directory and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Running the App

To run the Streamlit app, use the following command:

```bash
streamlit run streamlit_chatbot.py
```

The app will open in your default web browser at `http://localhost:8501`

## Usage

1. **Chat**: Type your message in the chat input box at the bottom
2. **Clear Chat**: Click the "🗑️ Clear Chat" button in the sidebar to reset the conversation
3. **Download PDF**: Click the "📥 Download Chat as PDF" button to export your chat history

## Features in Detail

### Chat Interface
- Messages are displayed in a clean chat format
- User messages appear with a 👤 avatar
- AI responses appear with a 🤖 avatar
- Responses stream in real-time for a natural feel

### Sidebar Controls
- **Clear Chat**: Removes all messages and starts fresh
- **Download as PDF**: Exports the entire conversation as a professionally formatted PDF
- **Chat Statistics**: Shows current model and message count
- **About Section**: Information about Chipade and its capabilities

## Project Structure

```
project1/
├── streamlit_chatbot.py    # Main Streamlit app
├── Simple-Chatbot.py        # Original CLI chatbot
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
└── README.md               # This file
```

## Technologies Used

- **Streamlit**: Web interface framework
- **LangChain**: LLM orchestration
- **Groq**: LLaMA 3.3 model provider
- **ReportLab**: PDF generation
- **Python-dotenv**: Environment variable management

## Notes

- Make sure you have a valid Groq API key
- The chat history is stored in session state and resets when you refresh the page
- PDF downloads include timestamps and formatted messages
