# database.py

# Name      : Tanishka Sahu
# Roll No   : 25BCE10056
# Database connection file for Hospital Project
# This file is for connecting to database


import sqlite3
#  this is needed for database

def connect():   # this function makes tables if not there
    print("Connecting to hospital database...")
    conn = sqlite3.connect("hospital.db")
    c = conn.cursor()
    
    # creating patients table
    c.execute('''CREATE TABLE IF NOT EXISTS patients
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               gender TEXT,
               disease TEXT)''')
    
    # doctors table
    c.execute("""CREATE TABLE IF NOT EXISTS doctors (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 specialization TEXT)""")
    
    # appointments table
    c.execute('''CREATE TABLE IF NOT EXISTS appointments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  patient_id INTEGER,
                  doctor_id INTEGER,
                  date TEXT)''')
    
    conn.commit()
    print("All tables ready!")
    conn.close()

# this function only opens connection 
def get_connection():
    return sqlite3.connect("hospital.db")

# testing part (i run this to check)
if __name__ == "__main__":
    connect()
    print("Database created successfully!")