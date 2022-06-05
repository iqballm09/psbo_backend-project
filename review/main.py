class review():
    def __init__(self, id, judul, ulasan, gambar, rekomendasi, jam, tanggal, upvotes, downvotes):
        self.id = id
        self.judul = judul
        self.ulasan = ulasan
        self.gambar = gambar
        self.rekomendasi = rekomendasi
        self.jam = jam
        self.tanggal = tanggal
        self.upvotes = upvotes
        self.downvotes = downvotes

    def getId(self) :
        return self.id
    def getJudul(self):
        return self.judul
    def getUlasan(self):
        return self.ulasan
    def getGambar(self):
        return self.gambar
    def getRekomendasi(self):
        return self.rekomendasi
    def getJam(self):
        return self.jam
    def getTanggal(self):
        return self.tanggal
    def getUpvotes(self):
        return self.upvotes
    def getDownvotes(self):
        return self.downvotes
