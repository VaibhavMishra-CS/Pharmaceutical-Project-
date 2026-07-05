import streamlit as st 
import csv 
import os 

st.title("Pharmacy Medication Reminder System")
with st.form("patient_form"):
    patient_name = st.text_input("Enter Patient Name")
    medicine = st.text_input("Enter Medicine Name")
    scheduled_time = st.time_input("Enter Scheduled Time")
    phone_number = st.text_input("Enter Patient Phone Number")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Save the data to a CSV file
        with open("patient_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([patient_name, medicine, scheduled_time, phone_number])
        st.success("Patient Enrolled successfully!")