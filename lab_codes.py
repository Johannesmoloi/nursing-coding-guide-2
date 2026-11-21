# Nursing Coding Guide - Lab & Investigation Codes
# LOINC = Lab test code | SNOMED CT = Clinical finding / procedure

LAB_INVESTIGATIONS = [
    # BLOOD TESTS
    {"test": "Full Blood Count (FBC)", "loinc": "58410-2", "snomed": "26604007", "category": "Blood Test", "unit": "x10^9/L"},
    {"test": "Haemoglobin (Hb)", "loinc": "718-7", "snomed": "271026005", "category": "Blood Test", "unit": "g/dL"},
    {"test": "Blood Glucose - Fasting", "loinc": "1558-6", "snomed": "271062006", "category": "Blood Test", "unit": "mmol/L"},
    {"test": "Blood Glucose - Random", "loinc": "2345-7", "snomed": "271061005", "category": "Blood Test", "unit": "mmol/L"},
    {"test": "HIV Test", "loinc": "25842-4", "snomed": "165815009", "category": "Blood Test", "unit": "Reactive/Non-Reactive"},
    {"test": "Urea & Electrolytes (U&E)", "loinc": "30938-2", "snomed": "275810003", "category": "Blood Test", "unit": "mmol/L"},
    # URINE TEST
    {"test": "Urine Dipstick - Protein", "loinc": "20454-6", "snomed": "167253007", "category": "Urine Test", "unit": "mg/dL"},
    {"test": "Urine Dipstick - Glucose", "loinc": "20448-8", "snomed": "167255009", "category": "Urine Test", "unit": "mg/dL"},
    {"test": "Urine Pregnancy Test (HCG)", "loinc": "2118-8", "snomed": "167252002", "category": "Urine Test", "unit": "Positive/Negative"},
    {"test": "Urine Microscopy - WBC", "loinc": "33051-8", "snomed": "167254008", "category": "Urine Test", "unit": "cells/uL"},
    # X-RAY
    {"test": "Chest X-Ray", "loinc": "24648-8", "snomed": "399208008", "category": "X-Ray", "unit": "Report"},
    {"test": "Abdominal X-Ray", "loinc": "24528-2", "snomed": "399198005", "category": "X-Ray", "unit": "Report"},
    {"test": "Limb X-Ray - Fracture Check", "loinc": "24531-6", "snomed": "399178006", "category": "X-Ray", "unit": "Report"},
    # ECG
    {"test": "ECG - 12 Lead", "loinc": "11524-6", "snomed": "29303009", "category": "ECG", "unit": "Report"},
    {"test": "ECG - Heart Rate", "loinc": "8867-4", "snomed": "364075005", "category": "ECG", "unit": "bpm"},
]

def show_codes(category=None):
    for lab in LAB_INVESTIGATIONS:
        if category is None or lab["category"] == category:
            print(f"{lab['test']} | LOINC: {lab['loinc']} | SNOMED: {lab['snomed']} | {lab['category']}")

if __name__ == "__main__":
    show_codes()
    print("\n--- Blood Tests Only ---")
    show_codes("Blood Test")
