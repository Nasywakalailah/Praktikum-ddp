#list makanan dengan 2 dimensi
list_makanan = [
    ["bakwan", "tempe", "tahu"],                #index - 0
    ["nasi uduk", "nasi pecel", "sate padang"]  #index - 1
]

#print nasi pecel

print(list_makanan[1][1])


#print tahu
print(list_makanan[0][2])

#print semua makanan

for makanan in list_makanan:
    #aksi buat for pertama
    for detail_makanan in makanan :
        #aksi for kedua 
        print(detail_makanan)
    