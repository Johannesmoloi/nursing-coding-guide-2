# database.py - Connect to Full Database - SQLite (Easy) / PostgreSQL (Hospital)
import sqlite3
import os
from lab_codes import LAB_INVESTIGATIONS

# FOR SQLITE (For Learning / GitHub Demo):
DATABASE_URL = "nursing_lab.db"

# FOR POSTGRESQL (For Real Hospital - Uncomment this):
# DATABASE_URL = "postgresql://username:password@localhost:5432/nursing_db"
# pip install psycopg2-binary

def connect_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            age INTEGER,
            gender TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lab_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            test_name TEXT,
            loinc_code TEXT,
            snomed_code TEXT,
            category TEXT,
            result_value TEXT,
            unit TEXT,
            date_done TEXT,
            nurse_name TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    """)
    conn.commit()
    conn.close()
    print("Database created!")

def add_patient(patient_id, name, age, gender):
    conn = connect_db()
    conn.execute("INSERT OR REPLACE INTO patients VALUES (?,?,?,?)", (patient_id, name, age, gender))
    conn.commit()
    conn.close()

def add_lab_result(patient_id, test_name, result, date_done, nurse):
    lab = next((x for x in LAB_INVESTIGATIONS if x["test"] == test_name), None)
    if not lab:
        print("Test not found! Check lab_codes.py")
        return
    conn = connect_db()
    conn.execute("""
        INSERT INTO lab_results (patient_id, test_name, loinc_code, snomed_code, category, result_value, unit, date_done, nurse_name)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (patient_id, lab["test"], lab["loinc"], lab["snomed"], lab["category"], result, lab["unit"], date_done, nurse))
    conn.commit()
    conn.close()
    print(f"Saved: {test_name} = {result} {lab['unit']} | LOINC {lab['loinc']}")

def view_patient_results(patient_id):
    conn = connect_db()
    rows = conn.execute("SELECT * FROM lab_results WHERE patient_id=?", (patient_id,)).fetchall()
    for r in rows:
        print(dict(r))
    conn.close()

if __name__ == "__main__":
    create_tables()
    add_patient("P001", "Thabo Mokoena", 34, "Male")
    add_lab_result("P001", "Haemoglobin (Hb)", "13.5", "2026-11-21", "Nurse Dlamini")
    add_lab_result("P001", "ECG - 12 Lead", "Normal Sinus Rhythm", "2026-11-21", "Nurse Dlamini")
    add_lab_result("P001", "Chest X-Ray", "No abnormality", "2026-11-21", "Nurse Dlamini")
    print("\n--- Patient P001 Results ---")
    view_patient_results("P001")
