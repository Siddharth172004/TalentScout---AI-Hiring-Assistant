# 🤖 TalentScout – AI Hiring Assistant  
A smart conversational AI assistant that automates **initial candidate screening** — built using **LangChain**, **Mistral LLM**, and a clean **Streamlit UI** for a smooth hiring experience.

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/AI-LangChain-0A66C2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployment-Streamlit%20Cloud-00C853?style=for-the-badge" />
</p>

---

## 📌 **Overview**
**TalentScout** is an AI-powered hiring assistant designed to automate the **first round of candidate interaction**.  
It converses with applicants in a structured and professional manner to collect essential information such as:
- Basic personal details  
- Technical & soft skills  
- Role preferences  

This significantly reduces manual effort for recruiters and speeds up the hiring pipeline.

---

## 🎯 **Problem Statement**
Traditional hiring workflows require recruiters to repeatedly ask the same screening questions, making the process:
- ⏳ Time-consuming  
- 🔁 Repetitive  
- 📉 Inefficient at scale  

TalentScout solves this by providing an **automated, scalable, and conversational screening solution** while maintaining a professional candidate experience.

---

## 📂 **Project Structure**
```
📁 TalentScout---AI-Hiring-Assistant
├── venv # Virtual Environment (not committed)
├── UI.py # Streamlit frontend
├── main.py # Backend logic + LangChain workflow
├── .env # API keys (ignored in git)
├── requirements.txt # Dependencies
├── README.md
└── .gitignore
```

---

## ✨ **Key Features**
- 💬 Conversational AI-based hiring assistant  
- 🧠 Context-aware follow-up questions  
- 🔄 Memory-enabled interaction using LangChain  
- 🧑‍💼 Structured & professional candidate flow  
- 📊 Basic logging to track chatbot activity  
- ⚠️ Exception handling for runtime error management  
- 💻 Simple and intuitive Streamlit UI    

---

## 🛠 **Technologies Used**
- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **AI Framework:** LangChain, LangChain-core, Langchain-openAI
- **Large Language Model:** mistralai/mistral-7b-instruct (via OpenRouter)  
- **Deployment:** Streamlit Cloud  

---

## ⚙️ **Workflow Overview**

### 1️⃣ User Interaction  
Candidate interacts with the Streamlit-based UI.

### 2️⃣ Prompt & Memory Handling  
LangChain structures prompts and maintains conversation memory.

### 3️⃣ Response Generation  
LLM generates context-aware, professional responses.

### 4️⃣ Logging & Error Handling
The application implements basic logging and exception handling to improve debugging and system reliability.

- Logging level used: **INFO**  
- Logs are stored in **app.log**  
- Errors are captured and handled gracefully to prevent application crashes  

### 5️⃣ UI Rendering  
Responses are displayed back to the user in real time.

*(A workflow diagram is included in the project documentation.)*

---

## 🚀 **Setup Instructions**

### 1️⃣ Clone the repository
```
git clone https://github.com/Siddharth172004/TalentScout---AI-Hiring-Assistant
cd TalentScout---AI-Hiring-Assistant
```
### 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv  
```
Activate the environment:

Windows:  
venv\Scripts\activate  

Linux / macOS:  
source venv/bin/activate  
---

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt  
```
---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root and add:
```
OPENROUTER_API_KEY=your_api_key_here  
```
---

### 5️⃣ Run the Application
```
streamlit run UI.py  
```
---

## ⚠️ Limitations

- Response quality depends on user input  
- Free-tier LLM may introduce latency  
- This project does not currently support uploading resumes or automatically reading resume data.  

---

## 🔮 Future Enhancements

- 📄 Resume upload and parsing  
- 🎯 Skill matching with job descriptions  
- 🗄️ Database integration for candidate data  
- 📊 Recruiter analytics dashboard  
- 🚀 Support for advanced LLM models  

---

## ✅ Conclusion

 *TalentScout is a fictional AI hiring assistant created for learning and demonstration purposes.*

- LLM integration  
- Prompt engineering  
- Conversation memory handling  
- End-to-end deployment  

This project reflects strong practical skills relevant to **AI/ML Intern** roles.

---

## 📚 References

- LangChain Documentation  
- OpenRouter Platform    
- Streamlit Documentation  

---

## 👨‍💻 Developed By

Siddharth Dhole
