
import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture
def movie_payload():
    return {
        "movie_name": "Test Movie",
        "language": "English",
        "duration": "2h 10m",
        "price": 200
    }

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie(movie_payload):
    response = requests.post(f"{BASE_URL}/api/movies", json=movie_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["movie_name"] == "Test Movie"


def test_book_ticket():
    movies_response = requests.get(f"{BASE_URL}/api/movies")
    movie_id = movies_response.json()[0]["id"]

    booking_payload = {
        "movie_id": movie_id,
        "tickets": 2
    }

    response = requests.post(f"{BASE_URL}/api/bookings", json=booking_payload)

    assert response.status_code == 201
    assert response.json()["message"] == "Booking successfull"
