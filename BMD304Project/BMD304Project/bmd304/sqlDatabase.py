import mysql.connector

# Connect to the database (create a new database if it doesn't exist)
conn = mysql.connector.connect(
    host="sql8.freesqldatabase.com",
    database="sql8627351",
    user="sql8627351",
    password="45EizTWfxb",
    port="3306",
)
cursor = conn.cursor()

# Create a table to store patient data
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS patients (
        patient_number INT PRIMARY KEY,
        patient_name VARCHAR(255),
        patient_gender VARCHAR(10),
        Weight FLOAT,
        Height FLOAT,
        dob DATE,
        present_history TEXT,
        goal TEXT,
        past_history TEXT,
        family_history TEXT,
        medical_history TEXT,
        lab_history TEXT,
        start_activity_level TEXT

    )
"""
)
conn.commit()


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
    # Insert patient data into the table
    cursor.execute(
        """
        INSERT INTO patients (
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
            start_activity_level
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
        (
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
        ),
    )
    conn.commit()


def fetch_all_patients():
    cursor.execute("""
                    SELECT patient_number, patient_name, patient_gender, Weight, Height, dob, present_history, goal, past_history, family_history, medical_history, lab_history, start_activity_level
                    FROM patients
                    UNION
                    SELECT patient_number, patient_name, patient_gender, NULL, NULL, dob, present_history, NULL, past_history, family_history, medical_history, lab_history, NULL
                    FROM coPatient;

                   """)
    res = cursor.fetchall()
    return res


def get_patient(patient_number):
    cursor.execute(
        """SELECT patient_number, patient_name, patient_gender, Weight, Height, dob, present_history, goal, past_history, family_history, medical_history, lab_history, start_activity_level
            FROM patients
            WHERE patient_number = %s
        UNION
        SELECT patient_number, patient_name, patient_gender, NULL, NULL, dob, present_history, NULL, past_history, family_history, medical_history, lab_history, NULL
        FROM coPatient
        WHERE patient_number = %s""",
        (patient_number,patient_number),
    )
    res = cursor.fetchone()
    return res



def delete_patient(patient_number):
    # Delete a patient from the table
    cursor.execute("DELETE FROM patients WHERE patient_number = %s", (patient_number,))
    conn.commit()


# Close the database connection
