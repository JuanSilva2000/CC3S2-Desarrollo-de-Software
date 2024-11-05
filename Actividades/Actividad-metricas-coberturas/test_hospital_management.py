import pytest
from patient import Patient
# import patient

@pytest.fixture(scope="function",autouse=True)
def setup():
    patient = Patient("1", "Juan Silva", "16-02-2000")
    
def test_patient_creation():
    assert patient.patient_id == "1"
    assert patient.name == "Juan Silva"
