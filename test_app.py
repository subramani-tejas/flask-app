from app import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'<h3> Scaler DevOps Bootcamp - Day 1 </h3>'
    assert response.status_code == 200

print("Passed.")
