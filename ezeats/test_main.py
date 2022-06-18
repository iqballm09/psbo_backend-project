from fastapi.testclient import TestClient
from ezeats import main

client = TestClient(main.app)

def test_create_user():
    response = client.post(
        "/user/",
        json={  "email": "testing2@mail.com",
                "nama": "Test User2",
                "deskripsi_singkat": "Testing User2",
                "password": "tes2",
                "no_telp": "091311112222",
                "alamat": "Jalan Testing2",
                "gambar": "testing2.png",
                "cover": "covertesting2.png"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "email": "testing2@mail.com",
        "nama": "Test User2",
        "deskripsi_singkat": "Testing User2",
        "no_telp": "091311112222",
        "alamat": "Jalan Testing2",
        "gambar": "testing2.png",
        "cover": "covertesting2.png",
    }

def test_read_user():
    response = client.get("/user/")
    assert response.status_code == 200
    assert response.json() == [{
        "email": "testing2@mail.com",
        "nama": "Test User2",
        "deskripsi_singkat": "Testing User2",
        "no_telp": "091311112222",
        "alamat": "Jalan Testing2",
        "gambar": "testing2.png",
        "cover": "covertesting2.png"
    }]

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

def test_create_resto():
    response = client.post(
        "/resto/",
        json={
            "nama": "Testing",
            "kategori": "Testing",
            "harga": 10,
            "jam_buka": "0900",
            "jam_tutup": "1500",
            "fasilitas": "Testing",
            "deskripsi": "Testing",
            "jalan": "Testing",
            "kecamatan": "Testing",
            "kotakab": "Testing",
            "nama_kabkota": "Testing",
            "provinsi": "Testing",
            "web": "Testing",
            "foto_menu": "Testingmenu.png",
            "foto_cover": "Testingcover.png",
            "foto_resto": "Testingresto.png",
            "no_telp": "081311112222",
            "upvotes": 0,
            "downvotes": 0,
            },
    )
    assert response.status_code == 201
    assert response.json() == "Resto berhasil ditambahkan"

def test_read_resto():
    response = client.get("/resto/")
    assert response.status_code == 200
    assert response.json() == [{
            "nama": "Testing",
            "kategori": "Testing",
            "harga": 10,
            "jam_buka": "0900",
            "jam_tutup": "1500",
            "fasilitas": "Testing",
            "deskripsi": "Testing",
            "jalan": "Testing",
            "kecamatan": "Testing",
            "kotakab": "Testing",
            "nama_kabkota": "Testing",
            "provinsi": "Testing",
            "web": "Testing",
            "foto_menu": "Testingmenu.png",
            "foto_cover": "Testingcover.png",
            "foto_resto": "Testingresto.png",
            "no_telp": "081311112222",
            "upvotes": None,
            "downvotes": None,
            "id":1,
            "user_id":None
    }]

def test_read_resto_id():
    response = client.get("/resto/1/")
    assert response.status_code == 200
    assert response.json() == {
            "nama": "Testing",
            "kategori": "Testing",
            "harga": 10,
            "jam_buka": "0900",
            "jam_tutup": "1500",
            "fasilitas": "Testing",
            "deskripsi": "Testing",
            "jalan": "Testing",
            "kecamatan": "Testing",
            "kotakab": "Testing",
            "nama_kabkota": "Testing",
            "provinsi": "Testing",
            "web": "Testing",
            "foto_menu": "Testingmenu.png",
            "foto_cover": "Testingcover.png",
            "foto_resto": "Testingresto.png",
            "no_telp": "081311112222",
            "upvotes": None,
            "downvotes": None,
            "id":1,
            "user_id":None
    }

def test_create_review():
    response = client.post(
        "/review/",
        json={      "judul": "Testing",
                    "ulasan": "Testing",
                    "gambar": "Testing",
                    "rekomendasi": "Testing",
                    "jam": "Testing",
                    "tanggal": "Testing",
                    "upvotes": 0,
                    "downvotes": 0},
    )
    assert response.status_code == 201
    assert response.json() == "Review sudah ditambahkan"


def test_read_review():
    response = client.get("/review/")
    assert response.status_code == 200
    assert response.json() == [{
                    "judul": "Testing",
                    "ulasan": "Testing",
                    "gambar": "Testing",
                    "rekomendasi": "Testing",
                    "jam": "Testing",
                    "tanggal": "Testing",
                    "upvotes": 0,
                    "downvotes": 0,
                    "id":1,
                    "resto_id":1,
                    "user_id":1
    }]

def test_read_review_id():
    response = client.get("/review/1/")
    assert response.status_code == 200
    assert response.json() == {
                    "judul": "Testing",
                    "ulasan": "Testing",
                    "gambar": "Testing",
                    "rekomendasi": "Testing",
                    "jam": "Testing",
                    "tanggal": "Testing",
                    "upvotes": 0,
                    "downvotes": 0,
                    "id":1,
                    "resto_id":1,
                    "user_id":1
    }







