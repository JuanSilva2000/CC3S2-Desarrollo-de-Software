class Doctor:
    def __init__(self, doctor_id, name, specialization, available_slots):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.available_slots= available_slots

    def add_available_slot(self, slot):
        self.available_slots.append(slot)

    def remove_available_slot(self, slot):
        self.available_slots.remove(slot)

    def summary(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization,
            "available_slots": self.available_slots,
        }