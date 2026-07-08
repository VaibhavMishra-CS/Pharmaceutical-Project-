from datetime import datetime, timedelta
import streamlit as st 
import csv 
import os 

st.set_page_config(layout="wide") #making website wider
st.title("Pharmacy Medication Reminder System")

#create two columns 
col1, col2 = st.columns([1, 1])

#intial session state to keep track of added medications 
if 'medications' not in st.session_state:
    st.session_state.medications = []

# Input section
with col1:
    with st.form("patient_form"):
        patient_name = st.text_input("Enter Patient Name")
        dosage = st.text_input("Enter Dosage (mg/ml)") 
        times_per_day = st.number_input("Enter Number of Times per Day", min_value=1, max_value=10, step=1)

        interval_hours = st.number_input("Enter Interval Between Doses (in hours)", min_value=1, max_value=24, step=1)

        medicine = st.text_input("Enter Medicine Name")
        scheduled_time = st.time_input("Enter Scheduled Time")
        phone_number = st.text_input("Enter Patient Phone Number")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
             start_dt = datetime.combine(datetime.today(), scheduled_time)
             for i in range(times_per_day):
                 #calculate the for each dose: 
                    dose_time = (start_dt + timedelta(hours=i * interval_hours))
             st.session_state.medications.append({
                 "patient_name": patient_name,
                 "dosage": dosage,
                 "times_per_day": times_per_day,
                 "medicine": medicine,
                 "scheduled_time": scheduled_time,
                "phone_number": phone_number
          })

# Display the list of added medications
with col2:
    st.subheader("Your Daily Schedule")
    for i, medicine in enumerate(st.session_state.medications):
        st.write(f"{i+1}. {medicine['medicine']} ({medicine['dosage']}mg/ml) at {medicine['scheduled_time']}")

#final submit
    if st.button("Save Full Schedule", key='save_button'):
        if st.session_state.medications:
        # Save the data to a CSV file
            with open("patient_data.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                for med in st.session_state.medications:
                    patient_name = med['patient_name']
                    medicine = med['medicine']
                    scheduled_time = med['scheduled_time']
                    phone_number = med['phone_number']
                    times_per_day = med['times_per_day']
                    writer.writerow([patient_name, medicine, scheduled_time, phone_number, times_per_day])

            #Assuming "patient name & contact" is constant for this session 
        st.success("Patient Enrolled successfully!")
        st.session_state.medications = [] #clear list
    else:
        st.warning("Your list is Empty!")