from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


def test_predict_endpoint():
    with TestClient(app) as client:
        payload = {
            "SqFtTotLiving": 2200.0,
            "SqFtLot": 7500.0,
            "Bedrooms": 3,
            "Bathrooms": 2.5,
            "BldgGrade": 8,
            "YrBuilt": 1995,
            "NewConstruction": 0,
            "TrafficNoise": 0.0,
        }

        response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "predicted_price_usd" in data
    assert isinstance(data["predicted_price_usd"], float)
    assert data["predicted_price_usd"] > 0