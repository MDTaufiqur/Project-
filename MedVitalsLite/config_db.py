import sqlite3

def initialize_database():
    
    conn = sqlite3.connect('medvitals.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vital_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        heart_rate INTEGER NOT NULL,
        blood_pressure TEXT NOT NULL
    )
    ''')

   
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        doctor_name TEXT NOT NULL,
        notes TEXT NOT NULL
    )
    ''')

   
    
    try:
        cursor.execute("INSERT INTO users VALUES ('karim', 'pass123', 'Patient')")
        cursor.execute("INSERT INTO users VALUES ('dr_taufiq', 'doctor123', 'Doctor')")
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    

    conn.close()
    print("[SUCCESS] medvitals.db এবং টেবিলসমূহ সফলভাবে তৈরি হয়েছে!")

if __name__ == "__main__":
    initialize_database()
