import database as db
import streamlit as st
from streamlit_lottie import st_lottie
import Functions

st.header("Patient")
with st.form("saved_patient"):
    patient = st.selectbox("Select patient:", Functions.get_all_patient())
    submitted = st.form_submit_button("Show patient")
    if submitted:
        patient_data = db.get_patient(patient)
        get_dob = patient_data.get("dob")
        get_number = patient_data.get("patient_number")
        get_diagnosis = patient_data.get("diagnosis")
        get_weight = patient_data.get("Weight")
        get_height = patient_data.get("Height")
        get_patient_gender = patient_data.get("patient_gender")
        get_goal = patient_data.get("goal")
        if get_patient_gender == "Male":
            BMR = 10 * get_weight + 6.25 * get_height - 5 * get_dob + 5
        else:
            BMR = 10 * get_weight + 6.25 * get_height - 5 * get_dob - 161

        BMI = get_weight / get_height

        # Create input fields for patient information
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(
                    "## <font color=#444741>BMI:</font> "
                    f" <font color=#444741>{BMI}</font>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    "## <font color=#444741>BMR:</font> "
                    f" <font color=#444741>{BMR}</font>",
                    unsafe_allow_html=True,
                )

        st.markdown(
            "## <font color=#444741>Diagnosis:</font> \n### "
            f"<font color=#444741>{get_diagnosis}</font>",
            unsafe_allow_html=True,
        )
