import pytest
from hospital_management.patient import Patient
from hospital_management.doctor import Doctor
from hospital_management.appointment import Appointment
from hospital_management.treatment import Treatment
from hospital_management.hospital_management import HospitalManagement

@pytest.fixture
def setup(scope="function", autouse=True):
    hospital_management = HospitalManagement()
    patient = Patient("1", "John Doe", "1990-01-01")
    doctor = Doctor("1", "Dr. Smith", "Cardiology")
    doctor.add_available_slot("2024-11-05 10:00")
    hospital_management.manage_patients(patient)
    hospital_management.manage_doctors(doctor)

    return hospital_management, patient, doctor

def test_patient_creation():
    assert patient.patient_id == "1"
    assert patient.name == "John Doe"
