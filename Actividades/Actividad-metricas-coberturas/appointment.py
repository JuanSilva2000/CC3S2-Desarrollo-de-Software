class Appointment:
    def __init__(self,appointment_id, patient, doctor, datetime, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = datetime
        self.status = status

    def schedule(self):
        if self.datetime_slot not in self.doctor.available_slots:
            raise ValueError("La cita no esta en un horario disponible del medico")
        self.doctor.remove_available_slot(self.datetime_slot)

    def cancel(self):
        self.status = "canceled"
        self.doctor.add_available_slot(self.datetime_slot)

    def summary(self):
        return {
            "appointment_id": self.appointment_id,
            "patient": self.patient,
            "datetime": self.datetime,
            "status": self.status
        }