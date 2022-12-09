class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = 0
        self.massaJenis = 0
    
    def setLebar(self, lebar):
        self.lebar = lebar
    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def setPanjang(self, panjang):
        self.panjang = panjang
    def setMassa(self, massa):
        self.massa = massa
    def getVolume(self):
        volume = self.lebar * self.tinggi * self.panjang
        return volume
    def getMassaJenis(self):
        self.massaJenis = (self.massa)/(self.getVolume())
        return self.massaJenis

lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))
panjang = float(input("Masukkan panjang: "))
massa = float(input("Masukkan massa: "))

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())