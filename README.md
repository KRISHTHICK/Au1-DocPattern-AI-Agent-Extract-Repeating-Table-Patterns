# Au1-DocPattern-AI-Agent-Extract-Repeating-Table-Patterns
AI Agent

Project Title: “DocPattern AI Agent” – Extract Repeating Table Patterns from MS Word Documents
📌 Project Objective:
Build an AI agent system that extracts repeating or common table structures from uploaded .docx Word documents. It identifies pattern types such as headers, checkbox columns, and value formats (e.g., percentages, dates), and converts the tables into structured JSON output.

✅ Use Case Example:
You upload a .docx file with 5–10 tables (e.g., checklists, reports, data logs), and the system:

Detects repeating table formats

Classifies the table types

Extracts rows with associated labels (e.g., heading row, checkbox column)

Outputs a JSON pattern + extracted content

⚙️ Tech Stack:
Python

python-docx

Streamlit (for UI)

re (regex for value pattern detection)

json (output format)

🚀 How to Run
Install packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
