class Patient:
    def __init__(self, name, phone_number, address, occupation):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.occupation = occupation
        self.doctors = []
        self.discharged = False
        self.discharge_time = None

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def discharge(self, discharge_time):
        self.discharged = True
        self.discharge_time = discharge_time

class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patient_details(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                print("Patient Details:")
                print(f"Name: {patient.name}")
                print(f"Phone Number: {patient.phone_number}")
                print(f"Address: {patient.address}")
                print(f"Occupation: {patient.occupation}")
                print("Doctors:")
                for doctor in patient.doctors:
                    print(f"  {doctor.name} ({doctor.department})")
                if patient.discharged:
                    print(f"Discharged at: {patient.discharge_time}")
                else:
                    print("Still in treatment")
                return
        print("Patient not found")

    def discharge_patient(self, patient_name, discharge_time):
        for patient in self.patients:
            if patient.name == patient_name:
                patient.discharge(discharge_time)
                print(f"Patient {patient_name} discharged at {discharge_time}")
                return
        print("Patient not found")


hospital = Hospital()


patient1 = Patient("John Doe", "1234567890", "New York", "Software Engineer")
patient2 = Patient("Jane Smith", "9876543210", "California", "Doctor")


doctor1 = Doctor("Dr. Smith", "Cardiology")
doctor2 = Doctor("Dr. Johnson", "Neurology")


patient1.add_doctor(doctor1)
patient2.add_doctor(doctor2)


hospital.add_patient(patient1)
hospital.add_patient(patient2)


hospital.display_patient_details("John Doe")


hospital.discharge_patient("John Doe", "2023-02-20 10:00:00")


hospital.display_patient_details("John Doe")