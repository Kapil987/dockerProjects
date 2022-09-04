import psycopg2

# Connect to an existing databse
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="192.168.1.105",
    port=5432
)

# Open cursor to perform database operations
cur = conn.cursor()

# Insert data
cur.execute("INSERT INTO student (name, age) VALUES ('Kumar', 50)")

# Query the databse
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close communication with databse
cur.close()
conn.close()

