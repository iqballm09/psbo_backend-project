class Histori():
	def __init__(self, id , jam, tanggal):
		self.id = id
		self.jam = jam
		self.tanggal = tanggal
	def getId(self):
		return self.id 
	def getJam(self):
        return self.jam
    def setJam(self, jam):
        self.jam = jam
    def getTanggal(self):
        return self.tanggal
    def setTanggal(self, tanggal):
        self.tanggal = tanggal