from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_github_skills_present():
    res = client.get("/activities")
    assert res.status_code == 200
    activities = res.json()
    assert "GitHub Skills" in activities


def test_signup_for_github_skills():
    email = "test_student@mergington.edu"
    # Ensure signup works
    res = client.post(f"/activities/GitHub Skills/signup?email={email}")
    assert res.status_code == 200
    assert "Signed up" in res.json()["message"]

    # Verify the participant was added
    res = client.get("/activities")
    activities = res.json()
    assert email in activities["GitHub Skills"]["participants"]
