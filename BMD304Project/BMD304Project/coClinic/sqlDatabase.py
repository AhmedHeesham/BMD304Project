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
    CREATE TABLE IF NOT EXISTS coPatient (
        patient_number INT PRIMARY KEY,
        patient_name VARCHAR(255),
        patient_gender VARCHAR(10),
        dob DATE,
        present_history TEXT,
        past_history TEXT,
        family_history TEXT,
        medical_history TEXT,
        lab_history TEXT
    )
"""
)

conn.commit()


def insert_Patient_data(
      patient_number , #0
        patient_name,#1
        patient_gender,#2
        dob, #3
        present_history,#4
        past_history,#5
        family_history,#6
        medical_history,#7
        lab_history,#8
):
    # Insert patient data into the table
    cursor.execute(
        """
        INSERT INTO coPatient (
      patient_number ,
        patient_name,
        patient_gender,
        dob,
        present_history,
        past_history,
        family_history,
        medical_history,
        lab_history

        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
        (
            patient_number,
            patient_name,
            patient_gender,
            dob,
            present_history,
            past_history,
            family_history,
            medical_history,
            lab_history,

        ),
    )
    conn.commit()






def fetch_all_patients():
    cursor.execute("SELECT * FROM coPatient")
    res = cursor.fetchall()
    return res


def get_patient(patient_number):
    cursor.execute(
        "SELECT * FROM coPatient WHERE patient_number = %s", (patient_number,)
    )
    res = cursor.fetchone()
    return res


def delete_patient(patient_number):
    # Delete a patient from the table
    cursor.execute("DELETE FROM coPatient WHERE patient_number = %s", (patient_number,))
    conn.commit()


# Close the database connection
