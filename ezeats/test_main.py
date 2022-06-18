from fastapi.testclient import TestClient
from ezeats import main

client = TestClient(main.app)

def test_create_user():
    response = client.post(
        "/user/",
        json={  "email": "testing@mail.com",
                "nama": "Test User",
                "deskripsi_singkat": "Testing User",
                "password": "tes",
                "no_telp": "081311112222",
                "alamat": "Jalan Testing",
                "gambar": "testing.png",
                "cover": "covertesting.png"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "email": "testing@mail.com",
        "nama": "Test User",
        "deskripsi_singkat": "Testing User",
        "no_telp": "081311112222",
        "alamat": "Jalan Testing",
        "gambar": "testing.png",
        "cover": "covertesting.png",
    }

def test_read_user_id():
    response = client.get("/user/1/")
    assert response.status_code == 200
    assert response.json() == {
        "email": "testing2@mail.com",
        "nama": "Test User2",
        "deskripsi_singkat": "Testing User2",
        "no_telp": "091311112222",
        "alamat": "Jalan Testing2",
        "gambar": "testing2.png",
        "cover": "covertesting2.png"
    }

