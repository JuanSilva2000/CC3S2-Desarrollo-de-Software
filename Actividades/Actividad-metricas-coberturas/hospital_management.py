class HospitalManagement:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.treatments = {}

    def manage_patients(self, patient):
        self.patients[patient.patient_id] = patient

    def manage_doctors(self,doctor):
        self.doctors[doctor.doctor_id] = doctor

    def manage_appointments(self, appointment):
        self.appointments[appointment.appointment_id] = appointment

    def manage_treatments(self, treatment):
        self.treatments[treatment.treatment_id] = treatment

        