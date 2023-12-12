from langchain.memory import ConversationBufferMemory, RedisChatMessageHistory




history = ConversationBufferMemory(return_messages=True, memory_key="chat_history")
