![Nursing Coding Guide](nursing-cover.png)

# 🩺 Nursing Coding Guide 2 - Lab & Investigation Codes

Guide for nurses to code Lab & Investigation data using **LOINC** and **SNOMED CT**.

## What is in this project?

| File | What it does |
| :--- | :--- |
| `lab_codes.py` | List of Lab tests with LOINC + SNOMED codes - Blood, Urine, X-Ray, ECG |
| `database.py` | Saves patient + lab results to Database (SQLite / PostgreSQL) |
| `fhir_connect.py` | Connects to FHIR Server to get patient Observations |
| `requirements.txt` | Libraries needed |

## Codes Explained

- **LOINC** = Code for the TEST / QUESTION. Example: Haemoglobin = `718-7`
- **SNOMED CT** = Code for the FINDING / PROCEDURE. Example: Chest X-Ray = `399208008`

## Categories Covered
- ✅ Blood Tests - FBC, Hb, Glucose, HIV, U&E
- ✅ Urine Tests - Protein, Glucose, Pregnancy, Microscopy
- ✅ X-Ray - Chest, Abdomen, Limb Fracture
- ✅ ECG - 12 Lead, Heart Rate

## How to Run

```bash
pip install -r requirements.txt
python lab_codes.py
python database.py
python fhir_connect.py
