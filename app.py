import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password=""
        )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM expenses;')
    expenses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        type = request.form['type']
        value = request.form['value']
        category = request.form['category']
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO expenses (type, value, category)'
                    'VALUES (%s, %s, %s)',
                    (type, value, category))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('create.html')