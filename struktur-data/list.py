
buah = ["mangga", "melon", "anggur", "jeruk"]

#untuk mengaksesnya menggunakan indeks
#indeks dimulai dari 0

#print(buah[0])

#menambah list dengan append()

#buah.append("semangka")

#print(buah)

#mengubah list dengan index yang mau di ubah = nilaibaru

#buah[1] = "duku"

#print(buah)

#menghapus list dengan del

#del buah[1]

#print(buah)

#mengambil data akhir yang sekaligus menghapus => pop()

#print(buah.pop())

#mengetahui jumlah data => len()

#print(len(buah))

#menyisipkan data sesuai index yang diinginkan
#buah.insert(1, "duku")
#print(buah)

#mengambil seluruh data menggunakan perulangan for

for i in  buah:
    #["mangga", "melon", "anggur", "jeruk"]
    #aksi apa yang akan dilakukan
    print("buah", i)