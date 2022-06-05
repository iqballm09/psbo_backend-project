class KoleksiSaya():
    def __init__(self, id, status, jam, tanggal):
        self.id = id
        self.status = status
        self.jam = jam
        self.tanggal = tanggal
    def getId(self):
        return self.id
    def getStatus(self):
        return self.status
    def setStatus(self, status):
        self.status = status
    def getJam(self):
        return self.jam
    def setJam(self, jam):
        self.jam = jam
    def getTanggal(self):
        return self.tanggal
    def setTanggal(self, tanggal):
        self.tanggal = tanggal
    def getAll(self):
        return { 'id': self.id, 'status': self.status, 'jam': self.jam, 'tanggal':self.tanggal }