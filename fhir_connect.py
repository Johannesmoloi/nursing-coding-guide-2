# fhir_connect.py - Connect to FHIR Server
import requests

FHIR_BASE = "https://hapi.fhir.org/baseR4"

def get_patient_observations(patient_id):
    url = f"{FHIR_BASE}/Observation?patient={patient_id}&_count=20"
    res = requests.get(url)
    data = res.json()
    for entry in data.get("entry", []):
        obs = entry["resource"]
        code = obs.get("code", {}).get("coding", [{}])[0].get("code")
        display = obs.get("code", {}).get("text", "Lab Result")
        value = obs.get("valueQuantity", {}).get("value", "See report")
        print(f"LOINC: {code} | {display} = {value}")

if __name__ == "__main__":
    get_patient_observations("example")
