from deta import Deta

DETA_KEY = "a0yr4brn1np_C1skqW5Ht18a5puSjNypgjCE5SVJew5H"

deta = Deta(DETA_KEY)

db = deta.Base("NCproject")


def insert_Patient_data(
    patient_number,
    patient_name,
    patient_gender,
    Weight,
    Height,
    dob,
    present_history,
    goal,
    past_history,
    family_history,
    medical_history,
    lab_history,
    start_activity_level,
):
    return db.put(
        {
            "key": patient_number,
            "patient_name": patient_name,
            "patient_gender": patient_gender,
            "Weight": Weight,
            "Height": Height,
            "dob": dob,
            "present_history": present_history,
            "goal": goal,
            "past_history": past_history,
            "family_history": family_history,
            "medical_history": medical_history,
            "lab_history": lab_history,
            "start_activity_level": start_activity_level,
        }
    )


def fetch_all_periods():
    res = db.fetch()
    return res.items


def get_patient(patient_number):
    return db.get(patient_number)
