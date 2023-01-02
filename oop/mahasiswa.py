class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def __init__(self , nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    def lulus(self, nilai):
     if(nilai > 90):
        print("lulus")
     else:
        print("tidak lulus")

mhs1 = Mahasiswa("0110222096", "Nasywa Kalailah Fathin", "TI13")
#mhs1.nama= "Nasywa"
#mhs1.nim= "0110222096"
#mhs1.rombel= "TI13"

print("Nama mahasiswa",mhs1.nama)
print("NIM",mhs1.nim)
print("Rombel",mhs1.rombel)
mhs1.lulus(91)