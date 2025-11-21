# Example of using SQLite3 in Python

import sqlite3

# Connect to the database (creates file if not exists)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")

# Insert data
cursor.execute("INSERT INTO students VALUES ('Alice', 20)")
cursor.execute("INSERT INTO students VALUES ('Bob', 22)")

# Save changes
conn.commit()

# Fetch and display data
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

