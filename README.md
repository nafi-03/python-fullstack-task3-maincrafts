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

