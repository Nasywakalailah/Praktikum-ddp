#membuat dictionari menggunakan {}
#data_diri = {"nama" : "Nasywa "}

#print(data_diri["nama"])

#untuk mengakses valuenya saja, menggunakan function values()
nilai = {"firda" : 89, "inaya":78, "fawwaz": 90, "rahmah": 75}

#for i in nilai.values():
  #  print(i)

#mengakses keynya saja
for i in nilai.keys():
    print(i)

#mencetak key dan value menggunakan items()

for nama,skor in nilai.items():
    print(nama,":",skor)
