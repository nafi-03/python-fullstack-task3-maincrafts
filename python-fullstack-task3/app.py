import sqlite3
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_key' 

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

with app.app_context():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, course TEXT)')
    db.commit()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'])
        db = get_db()
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (request.form['username'], hashed_pw))
            db.commit()
            return redirect('/login')
        except:
            return "Username already exists!"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (request.form['username'],)).fetchone()
        if user and check_password_hash(user['password'], request.form['password']):
            session['user'] = user['username']
            return redirect('/students')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/students')
def students():
    if 'user' not in session: return redirect('/login') 
    db = get_db()
    data = db.execute("SELECT * FROM students").fetchall() 
    return render_template('students.html', students=data)

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session: return redirect('/login')
    if request.method == 'POST': 
        db = get_db()
        db.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                   (request.form['name'], request.form['email'], request.form['course']))
        db.commit()
        return redirect('/students')
    return render_template('add_student.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session: return redirect('/login')
    db = get_db()
    student = db.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()
    if request.method == 'POST': 
        db.execute("UPDATE students SET name=?, email=?, course=? WHERE id=?",
                   (request.form['name'], request.form['email'], request.form['course'], id))
        db.commit()
        return redirect('/students')
    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    if 'user' not in session: return redirect('/login') 
    db = get_db()
    db.execute("DELETE FROM students WHERE id=?", (id,)) 
    db.commit()
    return redirect('/students')

if __name__ == '__main__':
    app.run(debug=True)