# 🤖 Chipade AI Chatbot Collection

A comprehensive collection of AI chatbots built with different technologies including LangChain, Ollama, Groq, and Hugging Face. Features both CLI and beautiful Streamlit web interfaces.

## 🌟 Project Overview

This repository contains multiple AI chatbot implementations:

1. **Ollama Chatbot** - Fully local AI assistant using Ollama (Llama 3)
2. **Streamlit Ollama Chatbot** - Stunning web UI for Ollama chatbot
3. **Groq Chatbot** - Cloud-based chatbot using Groq's LLaMA models
4. **Hugging Face Chatbot** - Integration with Hugging Face models
5. **Simple CLI Chatbot** - Basic command-line chatbot



### Ollama Chatbot (Local & Private)
- 🔒 **100% Private**: Runs completely on your local machine
- 💬 **Context-Aware**: Maintains conversation history
- ⚡ **Real-time Streaming**: See responses appear word by word
- � **Auto-Save**: Conversations saved to JSON files
- 🎯 **Adaptive AI**: Adjusts response style based on context


## 🚀 Installation

### Prerequisites
- Python 3.8+
- Ollama installed locally (for Ollama chatbots)
- API keys (for Groq/Hugging Face)

### Step 1: Clone the Repository
```bash
git clone https://github.com/codewithyasho/Chipade-AiChatbot.git
cd Chipade-AiChatbot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Ollama (for Local Chatbot)
1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the Llama model:
```bash
ollama pull llama3.2:3b
```

### Step 4: Configure API Keys (Optional)
Create a `.env` file for cloud-based chatbots:
```env
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_KEY=your_hf_api_key_here
```

## 🎯 Usage

### Ollama Chatbot (CLI)
Run the command-line version:
```bash
python Ollama-chatbot.py
```

Features:
- Type your messages and get instant AI responses
- Conversation history maintained throughout session
- Type `exit`, `quit`, or `bye` to end
- Chat history auto-saved to `ollama-chat-history.json`

### Streamlit Ollama Chatbot (Web UI) ⭐ **RECOMMENDED**
Launch the beautiful web interface:
```bash
streamlit run streamlit_ollama_chatbot.py
```

Then open your browser at `http://localhost:8501`

**Web UI Features:**
- 🎨 Stunning gradient purple design
- 🌡️ Temperature slider (0.0 - 1.0) to control creativity
- 📊 Real-time message statistics
- 💾 Save conversations with timestamps
- 🗑️ Quick clear chat button
- 🤖 Smooth message streaming animations

### Groq Chatbot
```bash
python app.py
# or
streamlit run streamlit_chatbot.py
```

### Simple CLI Chatbot
```bash
python Simple-Chatbot.py
```

## 📁 Project Structure

```
project1/
├── streamlit_ollama_chatbot.py  # ⭐ Main Streamlit web UI (Ollama)
├── Ollama-chatbot.py            # CLI Ollama chatbot
├── app.py                       # Groq chatbot app
├── Simple-Chatbot.py            # Basic CLI chatbot
├── ollama.ipynb                 # Ollama experiments notebook
├── langchain-groq.ipynb         # Groq integration notebook
├── huggingface.ipynb            # Hugging Face notebook
├── requirements.txt             # Python dependencies
├── .env                         # API keys (create this)
└── README.md                    # This file
```

## 🛠️ Technologies Used

### Core Technologies
- **Python 3.8+**: Primary language
- **LangChain**: LLM orchestration and conversation management
- **Streamlit**: Modern web UI framework

### AI Models & Platforms
- **Ollama**: Local LLM runtime (Llama 3.2:3b)
- **Groq**: Cloud-based LLM API (LLaMA 3.3)
- **Hugging Face**: Model hub integration

### Additional Libraries
- **langchain-ollama**: Ollama integration for LangChain
- **langchain-groq**: Groq integration for LangChain
- **langchain-core**: Core LangChain components
- **python-dotenv**: Environment variable management
- **reportlab**: PDF generation for chat exports


## 🔒 Privacy & Security

**Ollama Chatbot Benefits:**
- ✅ Runs 100% locally on your machine
- ✅ No data sent to external servers
- ✅ Complete privacy and control
- ✅ Works offline (after model download)
- ✅ No API costs or rate limits

## 📝 Configuration

### Adjusting Model Settings

In the code, you can modify:

```python
llm = ChatOllama(
    model="llama3.2:3b",      # Change model
    temperature=0.7,           # Creativity (0.0-1.0)
    verbose=False,             # Debug output
    num_thread=10              # CPU threads
)
```

### Available Ollama Models
- `llama3.2:3b` - Fast, efficient (recommended)
- `llama3:8b` - More capable, slower
- `llama3:70b` - Most capable (requires powerful hardware)

Pull models with: `ollama pull <model-name>`

## 🐛 Troubleshooting

### Ollama Connection Error
**Problem**: "Error: Ollama connection failed"
**Solution**: 
1. Make sure Ollama is running: `ollama serve`
2. Verify model is downloaded: `ollama list`
3. Pull model if needed: `ollama pull llama3.2:3b`

### Import Errors
**Problem**: "ModuleNotFoundError"
**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Streamlit Not Found
**Problem**: "streamlit: command not found"
**Solution**: 
```bash
pip install streamlit
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**Yasho Chipade** ([@codewithyasho](https://github.com/codewithyasho))

## 🙏 Acknowledgments

- **Ollama** - For making local LLMs accessible
- **LangChain** - For excellent LLM orchestration tools
- **Streamlit** - For the amazing web framework
- **Meta AI** - For the Llama models

---

<div align="center">

**Made with ❤️ using Streamlit & Ollama**

🔒 **100% Private & Local** | ⚡ **Fast & Efficient** | 🎨 **Beautiful UI**

[Report Bug](https://github.com/codewithyasho/Chipade-AiChatbot/issues) · [Request Feature](https://github.com/codewithyasho/Chipade-AiChatbot/issues)

</div>
