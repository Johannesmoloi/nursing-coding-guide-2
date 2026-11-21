# database.py - Simple Nursing Database
import sqlite3

conn = sqlite3.connect("nursing.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    test_name TEXT,
    loinc_code TEXT,
    snomed_code TEXT,
    result TEXT
)
""")

# Example patient
cursor.execute("""
INSERT INTO patients (name, test_name, loinc_code, snomed_code, result)
VALUES ('Test Patient', 'Haemoglobin', '718-7', '24863005', '13.5 g/dL')
""")

conn.commit()
print("Database created! Patient saved.")

for row in cursor.execute("SELECT * FROM patients"):
    print(row)

conn.close()
