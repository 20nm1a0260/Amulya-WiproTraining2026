
import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture
def patient_payload():
    return {
       "patient_name": "sai",
        "age": 32,
        "gender": "male",
        "contact": "9876543210",
        "disease": "cold",
        "doctor_assigned": "Dr. Sharat"
    }


def test_get_patients(base_url):
    response = requests.get(f"{base_url}/api/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_patient(patient_payload):
    response = requests.post(f"{BASE_URL}/api/patients", json=patient_payload)
    assert response.status_code == 201
    assert response.json()["patient_name"] == "sai"


@pytest.mark.skip(reason="Feature under development")
def test_skip_example():
    assert True

@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2


@pytest.mark.parametrize("invalid_id", [999, 500])
def test_invalid_patient(invalid_id):
    response = requests.get(f"{BASE_URL}/api/patients/{invalid_id}")
    assert response.status_code == 404
