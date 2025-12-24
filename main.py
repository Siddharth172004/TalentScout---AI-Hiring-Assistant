from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()

parser = StrOutputParser()

memory = {}
def history(session_id: str):
    if session_id not in memory:
        memory[session_id] = InMemoryChatMessageHistory()
    return memory[session_id]

def chatbot(user_input: str, data: str, session_id: str):

    model = ChatOpenAI(
        model = "mistralai/mistral-7b-instruct:free",
        openai_api_key = os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature= 0.7
    )
    

    system_prompt = (f"""You are a professional Hiring Assistant chatbot.

IMPORTANT INSTRUCTIONS:
- Do NOT show your thinking, reasoning, planning, or analysis.
- Do NOT explain what you are going to do.
- ONLY output the final message that the candidate should see.

Candidate details:
- Name: {data["user_name"]}
- Experience: {data["user_experience"]}
- Tech Stack: {data["user_techstack"]}

Conversation rules:
1. Always greet and ask the candidate "hows his day Going" using their name - {data["user_name"]}.
2. First message:
   - Greet politely
   - Ask how their day is going (friendly tone)
3. After the user replies:
   - Respond positively using their name
   - Acknowledge their response (e.g., “That’s great to hear”)
4. Then ask HR-style questions one by one.
5. The FIRST interview question must ALWAYS be:
   "Can I know a bit about yourself?"
6. Ask only ONE question at a time.
7. Keep tone professional, polite, and conversational.
8. Do not mention AI, LLM, system, prompts, or internal logic.
9. Use simple English suitable for interviews.
10. Continue the conversation naturally based on the candidate’s responses.

Start the conversation now.""")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | model | parser

    chat_with_memory = RunnableWithMessageHistory(
        chain,
        history,
        input_messages_key="input",
        history_messages_key="history"
    )

    result = chat_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
    )

    return result