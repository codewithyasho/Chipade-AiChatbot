from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import json
from datetime import datetime


# Initialize LLM

llm = ChatOllama(model="llama3:8b", temperature=0.7,
                 verbose=False, num_thread=10)

# Initialize conversation with system message (ONCE, outside loop)
conversation = [
    SystemMessage(content="You are an Adaptive and Intelligent AI assistant capable of helping with diverse topics including technology, education, business, creative writing, problem-solving, and everyday tasks. Adjust your response style based on context—be technical when needed, simple for beginners, creative for brainstorming, and professional for work-related queries. When needed, ask clarifying questions to better understand the user's needs. Always prioritize clarity and usefulness. Your name is Chipade."),

]

print("AI Assistant Chipade is ready! (Type 'exit', 'quit', or 'bye' to end)\n")

while True:
    human_msg = input("\nUser: ")

    if human_msg.lower() in ['exit', 'quit', 'bye']:
        print("\nChipade: Take care, Goodbye!")
        break

    # Add user message to conversation history
    conversation.append(HumanMessage(content=human_msg))

    # Stream the response word by word
    print("\nChipade: ", end="", flush=True)

    full_response = ""

    for chunk in llm.stream(conversation):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content

    # Add AI response to conversation history
    conversation.append(AIMessage(content=full_response))

    print()

# Save conversation to JSON file
history = []
for message in conversation:
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

# Create JSON object with metadata
conversation_data = {
    "session_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "messages": history
}

with open("ollama-chat-history.json", "w", encoding="utf-8") as f:
    json.dump(conversation_data, f, indent=4, ensure_ascii=False)

print("\nConversation history saved to ollama-chat-history.json")
