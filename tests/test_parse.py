from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_parse_sentence():
    response = client.post("/parse", json={"sentence": "去聚餐用了100元"})
    assert response.status_code == 200
    assert response.json()["金额"] == 100.0
    assert response.json()["类别"] == "聚餐"
    assert response.json()["备注"] == "聚餐花了100元"
