# Nursing Coding Guide - LOINC / SNOMED CT
# South Africa - NHLS Compatible

LAB_CODES = {
    # BLOOD TESTS
    "Full Blood Count": {"LOINC": "58410-2", "SNOMED": "26604007"},
    "Haemoglobin": {"LOINC": "718-7", "SNOMED": "24863005"},
    "Glucose Blood": {"LOINC": "2345-7", "SNOMED": "33747003"},
    "HIV Test": {"LOINC": "75622-1", "SNOMED": "165815009"},
    "Creatinine": {"LOINC": "2160-0", "SNOMED": "113075003"},

    # URINE TESTS
    "Urine Dipstick": {"LOINC": "5803-2", "SNOMED": "167261000"},
    "Urine Protein": {"LOINC": "5804-0", "SNOMED": "167284007"},

    # INVESTIGATIONS
    "Chest X-Ray": {"LOINC": "24627-2", "SNOMED": "399208008"},
    "ECG": {"LOINC": "11524-6", "SNOMED": "29303009"},
    "Blood Pressure": {"LOINC": "85354-9", "SNOMED": "75367002"},
}

for name, codes in LAB_CODES.items():
    print(f"{name} - LOINC: {codes['LOINC']} | SNOMED: {codes['SNOMED']}")
