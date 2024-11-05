import pytest
from hospital_management import HospitalManagement
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from treatment import Treatment

@pytest.fixture
def hospital_management():
    return HospitalManagement()

def test_manage_patients_create(hospital_management):
    #aqui quiero probar la creacion de un paciente
    hospital_management.manage_patients("create", "001", "Juan Silva", "16-02-2000")
    assert "P001" in hospital_management.patients
