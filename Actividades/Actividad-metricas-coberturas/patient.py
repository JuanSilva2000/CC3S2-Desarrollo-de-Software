class Patient:
    def __init__(self, patient_id, name, dob):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.medical_history = []

    def update_info(self,name,dob):
        if not name:
            raise ValueError("El nombre no puede ser vacío")
        
        if not dob:
            raise ValueError("La fecha de nacimiento no puede estar vacia")
        
        self.name = name
        self.dob = dob

    def add_medical_history(self, entrance):
        if not entrance:
            raise ValueError("La entrada del historial médico no puede ser vacía")
        self.medical_history.append(entrance)

    def summary(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "dob": self.dob,
            "medical_history": self.medical_history,
        }
