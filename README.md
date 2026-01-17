# AI-Powered CSV Agent

An end-to-end beginner-friendly project to build an **AI-powered CSV Agent** using Python and VS Code.
This agent allows you to ask natural language questions about a CSV file, and an AI model converts them
into pandas operations to give you answers.

---

## 📌 What This Project Does

- Loads a CSV file using pandas
- Accepts natural language questions from the user
- Uses an AI model to convert questions into pandas code
- Executes the generated code and shows results
- Runs completely in VS Code using a virtual environment

---

## 🧠 Example Questions You Can Ask

- What is the average age?
- Show all rows where city is Pune
- How many records are there?
- What is the maximum age?
- Show the first 5 rows

---

## 🛠️ Tech Stack

- Python 3.10+
- pandas
- OpenAI / Google GenAI (LLM)
- python-dotenv
- VS Code
- Virtual Environment (.venv)

---

## 📂 Project Structure

CSV_Agents/
│
├── .venv/               # Python virtual environment
├── csv_agent_ai.py      # Main AI CSV Agent code
├── data.csv             # Your CSV file
├── .env                 # API key (not shared)
└── README.md            # Project documentation

---

## ⚙️ Step-by-Step Setup (Beginner Friendly)

### 1️⃣ Open Project in VS Code

- Open VS Code
- Click **File → Open Folder**
- Select the `CSV_Agents` folder

---

### 2️⃣ Create & Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

You should see:
(.venv) in your terminal

---

### 3️⃣ Install Required Libraries

```powershell
python -m pip install pandas openai python-dotenv
```

---

### 4️⃣ Add API Key

Create a file named `.env` in the project root.

For OpenAI:
```env
OPENAI_API_KEY=your_api_key_here
```

For Google GenAI:
```env
GOOGLE_API_KEY=your_api_key_here
```

⚠️ Never upload this file to GitHub.

---

### 5️⃣ Add Sample CSV File

Create `data.csv`:

```csv
name,age,city
Nayan,22,Bhopal
Amit,25,Indore
Sara,23,Pune
Ravi,30,Pune
```

---

### 6️⃣ Run the AI CSV Agent

```powershell
python csv_agent_ai.py
```

Type your questions and see the results.
Type `exit` to quit.

---

## 🚨 Important Notes

- This project uses `exec()` to run AI-generated code.
- This is OK for learning but NOT safe for production.
- Do not run untrusted inputs.

---

## 🌱 Learning Outcomes

By completing this project, you will understand:
- pandas data analysis
- AI-to-code translation
- Virtual environments
- API key management
- Real-world AI agent workflow

---

## 🔮 Future Improvements

- Web UI using Streamlit
- CSV upload support
- Multi-file reasoning
- Secure execution sandbox
- Resume-ready project polish

---

## 👨‍💻 Author

Nayan Suhane  
AI & Python Beginner Project  

## 📸 Application Screenshot

![CSV Agent UI](Screenshot 2026-01-18 004743.png
)



