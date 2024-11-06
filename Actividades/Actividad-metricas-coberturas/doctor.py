import re

class Doctor:
    def __init__(self, doctor_id, name, specialization, available_slots):
        self.doctor_id = doctor_id
        self.name = self.validate_name_or_specialization(name)
        self.specialization = self.validate_name_or_specialization(specialization)
        self.available_slots = [self.validate_slot(slot) for slot in available_slots]

    def validate_name_or_specialization(self,value):
        if not re.match(r'^[A-Za-z\s]+$', value):
            raise ValueError("Nombre no valido")
        
        return value

    def validate_slot(self,slot):
        if not re.match(r'^\d{2}-\d{2}-\d{4}, \d{2}:\d{2}$', slot):
            raise ValueError("Slot no valido")
        
        return slot

    def add_available_slot(self, slot):
        slot_validated = self.validate_slot(slot)
        self.available_slots.append(slot_validated)

    def remove_available_slot(self, slot):
        if slot in self.available_slots:
            self.available_slots.remove(slot)
        else:
            print("El slot no existe. No hay nada que eliminar")

    def summary(self):
        return {
            "ID_DOCTOR": self.doctor_id,
            "Nombre": self.name,
            "Especialización": self.specialization,
            "Slots disponibles": self.available_slots
        }
