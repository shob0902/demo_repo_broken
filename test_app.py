import pytest

from app import app, users


@pytest.fixture
def client():
    users.clear()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_signup_accepts_valid_email(client):
    resp = client.post("/signup", json={"email": "person@example.com", "password": "hunter2"})
    assert resp.status_code == 201


def test_signup_rejects_invalid_email(client):
    resp = client.post("/signup", json={"email": "not-an-email", "password": "hunter2"})
    assert resp.status_code == 400


def test_signup_rejects_missing_password(client):
    resp = client.post("/signup", json={"email": "person@example.com"})
    assert resp.status_code == 400
