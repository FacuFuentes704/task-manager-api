def test_register_user(client):
    response = client.post("/users/register", json={
        "name": "Test User",
        "email": "test@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"

def test_email(client):
     client.post("/users/register", json={
        "name": "Test User",
        "email": "test@test.com",
        "password": "mipass123"
        })
     response = client.post("/users/register", json={
          "name": "TestClient",
          "email": "test@test.com",
          "password": "mipass123"
     })
     assert response.status_code == 400
     assert response.json()["detail"] == "Email duplicado"


def test_login(client):
     client.post("/users/register", json={
          "name": "TestClient",
          "email": "test@test.com",
          "password": "mipass123"
          })
     response = client.post("/auth/login", json={
          "email": "test@test.com",
          "password": "mipass123"
     })
     assert response.status_code == 200
     assert response.json()["access_token"]
     assert response.json()["token_type"] == "bearer"

def test_wrong_password(client):
     client.post("/users/register", json={
          "name": "TestClient",
          "email": "test@test.com",
          "password": "mipass123"
     })
     response = client.post("/auth/login", json={
          "email": "test@test.com",
          "password": "contraseña_incorrecta"
     })
     assert response.status_code == 401
     assert response.json()["detail"] == "Credenciales incorrectas"