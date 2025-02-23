from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import logging

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# MySQL configuration from environment variables
db_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', ''),
    'database': os.environ.get('MYSQL_DATABASE', 'employeedb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    app.logger.info("Database initialized.")

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    app.logger.info("Fetched employee list.")
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        emp_id = request.form['id']
        emp_name = request.form['name']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee (id, name) VALUES (%s, %s)", (emp_id, emp_name))
        conn.commit()
        cursor.close()
        conn.close()
        app.logger.info(f"Added employee {emp_name} with id {emp_id}.")
        return redirect(url_for('index'))
    return render_template('add_employee.html')

@app.route('/delete/<int:emp_id>')
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE id = %s", (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()
    app.logger.info(f"Deleted employee with id {emp_id}.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
