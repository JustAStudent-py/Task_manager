# 📝 Task Manager CLI (Python)

A simple and interactive **Command Line Interface (CLI) task manager** built with Python.  
This project allows users to **create, manage, and track tasks directly from the terminal** in a clean and straightforward way.

---

## 🚀 Features

- ✅ Add new tasks  
- 🗑️ Remove tasks  
- 🔄 Update task priority  
- ✔️ Mark tasks as completed  
- 📋 List all tasks  
- 🎯 Simple and intuitive CLI interface  

---

## 🧠 Concepts Practiced

This project was built to strengthen core Python fundamentals:

- 📦 Lists and Dictionaries  
- 🔧 Functions  
- 🔁 Loops (`while`, `for`)  
- 🔀 Conditional statements (`if/else`)  
- ⚠️ Error handling (`try/except`)  
- 💻 CLI interaction (`input`, `print`)  

---

## 📂 Project Structure
task_manager/
│
├── app/
│ ├── main.py       # Application entry logic
│ ├── handlers.py   # User interaction (input/output)
│ ├── logic.py      # Core business rules
│ ├── utils.py      # Helper functions
│── .gitignore       
├── run.py # Entry point to start the app
├── README.md

---

## ▶️ How to Run

Make sure you have Python installed (**Python 3+**).

Run the program:

```bash
python run.py

```

## 🖥️ Menu Options

1 - Add Task
2 - Remove Task
3 - Update Task Priority
4 - Show Tasks
5 - Complete Task
6 - Exit


## 📌 Example Output

[1] study python | Priority: 1 | ✖ Pending
[2] go to gym    | Priority: 3 | ✔ Done

## 💡 About this Project
This project was built as a hands-on exercise to practice Python backend fundamentals and simulate a real application architecture.

The main focus was not only functionality, but also code organization and separation of concerns, similar to production backend systems.

## 📈 Possible Improvements

💾 Save tasks to a JSON file (data persistence)
🔄 Load tasks when starting the application
📅 Add due dates for tasks
🔝 Sort tasks by priority
🔍 Add search functionality
🌐 Transform into a REST API using Flask or FastAPI

## 👨‍💻 Author
- Elias Souza