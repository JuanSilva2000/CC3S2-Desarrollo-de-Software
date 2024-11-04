class Treatment:
    def __init__(self, treatment_id, patient, doctor, description, date):
        self.treatment_id = treatment_id
        self.patient = patient
        self.doctor = doctor
        self.description = description
        self.date = date

    def record_treatment(self, description, date):
        if not description:
            raise ValueError("La descripción del tratamiento no puede ser vacía.")
        self.description = description
        self.date = date

    def update_treatment(self, description):
        self.description = description

    def summary(self):
        return {
            "treatment_id": self.treatment_id,
            "patient": self.patient.summary(),
            "doctor": self.doctor.summary(),
            "description": self.description,
            "date": self.date,
        }
