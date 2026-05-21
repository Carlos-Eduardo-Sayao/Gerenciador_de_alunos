🇧🇷 **Versão em português:** [Clique aqui](https://github.com/Carlos-Eduardo-Sayao/Gerenciador_de_alunos/blob/main/README.md)

# Student Management System 🏫

A command-line interface (CLI) system developed in Python and MySQL to manage school information, including the registration and control of classes, students, and grades.

---

## 🚀 Features

The system offers an interactive menu with the following options:

* **Class Management:** Register, list, update data, and delete classes.
* **Student Management:** Register, list (by class), update data (enrollment/name), and delete students.
* **Grade Control:** Enter grades by subject/unit, update existing grades, and view the student's report card.

> ⚠️ **Attention:** The system uses cascade deletion (`ON DELETE CASCADE`) in the database. If you delete a class, all of its students will be automatically deleted. Likewise, deleting a student will remove all of their grades.

---

## 🗄️ Database Structure

The `sistema_gerenciador_aluno` database consists of three main tables:

1. **`turmas`**: Stores information about the classrooms (Grade, Letter, Year, and Education Level).
2. **`alunos`**: Linked to a class, it features a unique enrollment number of exactly 9 characters.
3. **`notas`**: Linked to a student, it stores the subject, the unit, and the score.

---

## 🛠️ Prerequisites

Before you begin, you will need to have installed on your machine:
* Python 3
* MySQL Server

---

## 🔧 Installation and Configuration

### 1. Clone the repository or extract the files
Navigate to the project root folder in your terminal:
```bash
cd Gerenciador_de_alunos-main
```

### 2. Configure the Database
Open your MySQL client (via terminal or tools like Workbench/DBeaver) and execute the SQL script contained in `database/schema.sql` to create the table structure.

```bash
# Example via command line:
mysql -u seu_usuario -p < database/schema.sql
```

### 3. Adjust access credentials
Open the `database/conexao.py` file and change the `user` and `password` fields with your local MySQL credentials:

```python
def conectar():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "SEU_USUARIO",       # Change here 
        password = "SUA_PASSWORD",   # Change here 
        database = "sistema_gerenciador_aluno" 
    )
    return conn 
```

### 4. Install dependencies
It is recommended to create a virtual environment (`venv`) before installing the packages:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

---

## 💻 How to Run the System

With the database configured and active, simply run the main file:

```bash
python main.py
```

You will see the interactive menu in the terminal. Just type the number corresponding to the action you want to perform and follow the instructions on the screen.

---

## 📂 Folder Structure

```text
├── database/
│   ├── conexao.py  # Manages the connection with MySQL 
│   └── schema.sql  # Structural dump of the database 
├── models/
│   ├── aluno.py    # Aluno Class 
│   ├── nota.py     # Nota Class 
│   └── turma.py    # Turma Class 
├── main.py         # CLI Interface and menu loop 
├── services.py     # CRUD functions and database queries 
├── requirements.txt# Project dependencies 
└── .gitignore      # Files ignored by Git 
```
