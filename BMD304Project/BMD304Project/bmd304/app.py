from ast import If
from asyncio.windows_events import NULL
import streamlit as st
from PIL import Image
import database as db
from docx import Document
import requests
import Functions
from streamlit_option_menu import option_menu
import numpy as np
from streamlit_lottie import st_lottie

import sqlDatabase as sqDb

st.set_page_config(
    page_title="Hello Fit",
    page_icon="👩‍⚕️",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# 'Log In', 'Upload report',
# 'box-arrow-in-right', 'file-earmark ',
correct_username = "Ahmed"
correct_password = "123"
selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Diagnosis",
        "Patient",
        "Delete",
    ],
    icons=["house", "person-check-fill", "clipboard", ""],
    orientation="horizontal",
)

if selected == "Home":
    st.header(":mailbox: Get In Touch With Hello Fit!")

    contact_form = """
    <form action="https://formsubmit.co/a7medh474279@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit" style="background-color: #356e0a;" >Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(r"C:\Users\20100\Desktop\pythonstreamlit\style\style.css")

if selected == "Patient":
    st.header("Patient")
    patient = st.selectbox("Select patient:", Functions.get_all_patient())
    submitted = st.button("Show patient")
    if submitted:
        patient_data = sqDb.get_patient(patient)
        get_number = patient_data[0]
        get_name = patient_data[1]
        get_patient_gender = patient_data[2]
        get_weight = patient_data[3]
        get_height = patient_data[4]
        get_dob = patient_data[5]
        get_present_history = patient_data[6]
        get_goal = patient_data[7]
        get_past_history = patient_data[8]
        get_family_history = patient_data[9]
        get_medical_history = patient_data[10]
        get_lab_history = patient_data[11]
        get_activity_level = patient_data[12]

        age = Functions.calculate_age(get_dob)
        if (get_weight and get_height) == NULL:
                get_weight = 1
                get_height = 1
        else:
            if get_patient_gender == "Male":
                BMR = 10 * get_weight + 6.25 * get_height - 5 * age + 5
            else:
                BMR = 10 * get_weight + 6.25 * get_height - 5 * age - 161

        BMI = get_weight / (get_height / 100) ** 2
        BMI = format(BMI, ".1f")

        # Create input fields for patient information
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(
                    "## <font color=#444741>patient name:</font> "
                    f"<font color=#444741>{get_name}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Patient gender:</font>"
                    f"<font color=#444741>{get_patient_gender}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Age:</font> "
                    f" <font color=#444741>{age}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Weight:</font> "
                    f"<font color=#444741>{get_weight}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Height:</font> "
                    f"<font color=#444741>{get_height}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Goal:</font>"
                    f"<font color=#444741>{get_goal}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Past history:</font>"
                    f"<font color=#444741>{get_past_history}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Medical history:</font>"
                    f"<font color=#444741>{get_medical_history}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>Lab history:</font>"
                    f"<font color=#444741>{get_lab_history}</font>",
                    unsafe_allow_html=True,
                )

                st.markdown(
                    "## <font color=#444741>BMI:</font> "
                    f" <font color=#444741>{BMI}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>BMR:</font> "
                    f" <font color=#444741>{BMR} cal/day</font>",
                    unsafe_allow_html=True,
                )

            protein_ratio = 0.3
            protein_per_gram = 4
            protein_requirement = 0

            if get_activity_level == "Sedentary: little or no exercise":
                protein_requirement = (BMR * 1.2 * protein_ratio) / protein_per_gram

            elif get_activity_level == "Moderate: exercise 4-5 times/week":
                protein_requirement = (BMR * 1.5 * protein_ratio) / protein_per_gram

            elif get_activity_level == "Very Active: intense exercise 6-7 times/week":
                protein_requirement = (BMR * 1.7 * protein_ratio) / protein_per_gram
            protein_requirement = format(protein_requirement, ".0f")
        st.markdown(
            "## <font color=#444741>Needed protein:</font> "
            f" <font color=#444741>{protein_requirement} gram/day</font>",
            unsafe_allow_html=True,
        )
        with right_column:
            st_lottie(
                Functions.load_lottieurl(
                    "https://assets9.lottiefiles.com/packages/lf20_nq22pa14.json"
                ),
                height=400,
                width=400,
                quality="high",
                key="fit",
            )


if selected == "Diagnosis":
    st.subheader("Patient Data")
    with st.form(
        "entry_form",
        clear_on_submit=True,
    ):
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                global patient_number
                patient_name = st.text_input(
                    "First patient:", placeholder="Patient name ", max_chars=20
                )

                patient_number = st.text_input(
                    "Patient phone number: ",
                    placeholder="Patient phone number",
                    max_chars=11,
                )

                Height = st.number_input("Patient height:", value=180)

            with right_column:
                patient_last = st.text_input(
                    "Last patient:", placeholder="Patient name ", max_chars=20
                )
                dob = st.date_input("Age:")
                Weight = st.number_input(
                    "Patient weight:", value=70, min_value=1, max_value=110
                )
            patient_gender = st.selectbox(
                label="Patient gender:", options=("Male", "Female")
            )
            start_activity_level = st.selectbox(
                "Select patient actively level",
                (
                    "Sedentary: little or no exercise",
                    "Moderate: exercise 4-5 times/week",
                    "Very Active: intense exercise 6-7 times/week",
                ),
            )
        st.write("---")

        st.subheader("Patient data")

        # Create input fields for patient information
        # Create text boxes for specimen information
        goal = st.selectbox(
            label="Patient goal:",
            options=(
                "Lose weight",
                "Gain weight",
                "Lose weight and gain muscle",
                "Gain weight and muscles",
            ),
        )

        present_history = st.text_area("Present history:")
        past_history = st.text_area("Past history:")
        family_history = st.text_area("Family history:")
        medical_history = st.text_area("Medical history:")
        lab_history = st.text_area("Lab history:")
        add_data = st.form_submit_button("Save")

        if add_data:
            sqDb.insert_Patient_data(
                patient_number=patient_number,
                patient_name=patient_name,
                patient_gender=patient_gender,
                Weight=Weight,
                Height=Height,
                dob=dob,
                present_history=present_history,
                goal=goal,
                past_history=past_history,
                family_history=family_history,
                medical_history=medical_history,
                lab_history=lab_history,
                start_activity_level=start_activity_level,
            )
            output = "hello chatgpt you are a certified nutritionist\n"
            output += f"Here is a {patient_gender} named {patient_name}. "
            output += f"{patient_name} is {dob} years old, he is {Weight} kg and {Height} cm and his activity level is {start_activity_level}"
            output += f"{patient_name} wants to {goal}. "
            output += f"His medical history is {medical_history} and his past history is {past_history}. "
            output += f"His family history is {family_history} and his lab history is {lab_history}. "
            output += "Please make a diet plan with the situation in view of all these previous things."
            output += "and  please write the number of calories, protine, fats and carb  before every meal name and please write the number of grams of every thing inside the meal and please write the diet in English then arabic"

            # chatgptReplay = Functions.send_message(output)
            # document = Document()
            # document.add_paragraph(chatgptReplay)
            # document.save(f"{patient_number}, {patient_name} diet plan.docx")
            # # Append the data to the dataframe

            # data = {'Patient Name': patient_number, 'Transferred From': transferred_from, 'Date of Birth': dob,
            #         'Number of Visits': num_visits, 'Nature of Specimen': nature_of_specimen, 'Gross': gross,
            #         'Microscopy': microscopy, 'Diagnosis': diagnosis}


elif selected == "Delete":
    st.header("Patient")
    patient = st.selectbox("Select patient:", Functions.get_all_patient())
    btn_delete = st.button("Delete patient")
    if btn_delete:
            sqDb.delete_patient(patient)
