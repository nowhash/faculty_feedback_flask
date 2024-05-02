from flask import Flask, render_template,request, url_for, redirect
from cs50 import SQL
app = Flask(__name__)

db = SQL("sqlite:///facultyFeedback.db")

@app.route('/')
def index():
    db_data = db.execute("SELECT * FROM faculty_info LIMIT 10")
    return render_template('index.html', data=db_data)

@app.route('/fed_form/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        fid = request.form['fid']
        fname = request.form['fname']
        comment = request.form['comment']
        db.execute("INSERT INTO faculty_info (fid, fname, comment) VALUES (?, ?, ?)", fid, fname, comment)
        return redirect(url_for('index'))

    return render_template('fed_form.html')
