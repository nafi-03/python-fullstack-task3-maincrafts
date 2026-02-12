# python-fullstack-task3-maincrafts

Overview
This project extends a basic Flask authentication system into a complete admin-style CRUD module for managing students.
Only authenticated users can create, view, update, and delete student records, making it a good starting point for dashboards, admin panels, and internal tools.

Features
User registration and login with password hashing

Session‑based authentication and logout

Create, Read, Update, Delete operations for students

SQLite database for persistent storage

Protected routes – CRUD pages accessible only after login

Simple, clean UI built with HTML and CSS

Modular and extensible structure suitable for other entities (employees, products, etc.)

Tech Stack
Language: Python 3.x

Framework: Flask

Database: SQLite

Templating: Jinja2 (Flask templates)

Styling: HTML, CSS

Security: Werkzeug password hashing, Flask sessions

Project Structure
text
project-root/
│
├── app.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── addstudent.html
│   ├── students.html
│   └── editstudent.html
│
└── static/
    └── style.css
app.py – Main application entry point, routes, and database logic

database.db – SQLite database file

templates/ – All HTML templates

static/style.css – Global styles

Database Schema
users
Used for authentication.

id – INTEGER, PRIMARY KEY

username – TEXT, UNIQUE

password – TEXT, hashed

students
Used for CRUD operations.

id – INTEGER, PRIMARY KEY AUTOINCREMENT

name – TEXT

email – TEXT

course – TEXT

Example SQL for the students table:

sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
);
Setup & Installation
Clone the repository

bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create and activate a virtual environment (optional but recommended)

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
If you do not have a requirements.txt, you can start with:

bash
pip install flask
Initialize the database

Ensure database.db exists.

Create the users table (from your Task‑2/auth module).

Create the students table using the SQL snippet above.

Running the Application
Set the Flask app (optional depending on your environment):

bash
set FLASK_APP=app.py        # Windows
export FLASK_APP=app.py     # Linux / macOS
Run the development server:

bash
flask run
or

bash
python app.py
Open your browser and visit:

text
http://127.0.0.1:5000/
Register a new user, log in, and navigate to the dashboard to access the Student Management pages.

CRUD Flow
1. Create – Add Student
Route: /add-student

Methods: GET, POST

Behavior:

GET: Display a form to enter name, email, and course.

POST: Insert new student into the students table and redirect to the students list.

2. Read – View Students
Route: /students

Method: GET

Behavior:

Fetch all students from the database.

Render students.html with a table listing all records.

3. Update – Edit Student
Route: /edit/<int:id>

Methods: GET, POST

Behavior:

GET: Retrieve the student by id and pre‑fill the edit form.

POST: Update the record with the new name, email, and course, then redirect back to /students.

4. Delete – Remove Student
Route: /delete/<int:id>

Method: GET (or POST if you use a form)

Behavior:

Delete the student with the given id from the database.

Redirect to the students list.

