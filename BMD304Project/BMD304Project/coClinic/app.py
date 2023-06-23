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
    page_title="Get Well",
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

selected = option_menu(
    menu_title=None,
    options=[
        "Diagnosis",
        "Patient",
        "Delete",
    ],
    icons=["person-check-fill", "clipboard", ""],
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
        get_dob = patient_data[3]
        get_present_history = patient_data[4]
        get_past_history = patient_data[5]
        get_family_history = patient_data[6]
        get_medical_history = patient_data[7]
        get_lab_history = patient_data[8]
        age = Functions.calculate_age(get_dob)
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


            with right_column:
                patient_last = st.text_input(
                    "Last patient:", placeholder="Patient name ", max_chars=20
                )
                dob = st.date_input("Age:")

            patient_gender = st.selectbox(
                label="Patient gender:", options=("Male", "Female")
            )


        st.write("---")

        st.subheader("Patient data")


        symptoms = st.multiselect("patient symptoms",
                            ["Abdominal pain",
                            "Abdominal swelling, distension or bloating",
                            "Bloody stool (blood may be red, black, or tarry in texture)",
                            "Constipation",
                            "Diarrhea",
                            "Fatigue",
                            "Fever and chills",
                            "Gas",
                            "Inability to defecate or pass gas",
                            "Nausea with or without vomiting"])
        diseases = st.multiselect("patient diseases", 
                                   ["Colonic polyps",
                                    "Ulcerative colitis",
                                    "Diverticulitis",
                                    "Irritable bowel syndrome",
                                    "Colorectal cancer"])
        disorder = st.multiselect("patient disorder",
                                  ["Appendicitis",
                                    "Chronic diarrhea",
                                    "Colon (colorectal) cancer",
                                    "Colonic dismotility",
                                    "Crohn’s disease (Inflammatory bowel disease)",
                                    "Diverticulitis",
                                    "Fecal incontinence — accidental stool leaks/pelvic floor disorders",
                                    "Intestinal ischemia",
                                    "Intestinal obstructions",
                                    "Irritable bowel syndrome",
                                    "Polyps",
                                    "Rectal prolapse",
                                    "Ulcerative colitis",
                                    "C difficile infection (Clostridium)"])
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
                dob=dob,
                present_history=present_history,
                past_history=past_history,
                family_history=family_history,
                medical_history=medical_history,
                lab_history=lab_history,
            )

elif selected == "Delete":
    st.header("Patient")
    patient = st.selectbox("Select patient:", Functions.get_all_patient())
    btn_delete = st.button("Delete patient")
    if btn_delete:
            sqDb.delete_patient(patient)
