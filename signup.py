import sqlite3

# Connect to the database
conn = sqlite3.connect('campus.db')

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL,
                   role TEXT NOT NULL,
                   department TEXT NOT NULL,
                   campus_id TEXT NOT NULL)''')

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their email address
email = input("What is your email address? ")

# Ask the user for their password
password = input("What is your password? ")

# Ask the user for their role
role = input("What is your role? (Student, Faculty/Staff, Visitor) ")

# Ask the user for their department
department = input("What is your department? ")

# Ask the user for their campus ID
campus_id = input("What is your campus ID? ")

# Insert the user data into the users table
cursor.execute("INSERT INTO users (name, email, password, role, department, campus_id) VALUES (?,?,?,?,?,?)", (name, email, password, role, department, campus_id))

# Commit the changes to the database
conn.commit()

# Print a confirmation message
print(f"Welcome, {name}! Your account has been created with the email {email} and password {password}. You are a {role} in the {department} department with campus ID {campus_id}.")

# Close the connection to the database
conn.close()