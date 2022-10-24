 #1. masukkan nama file 
namafile = input('masukkan nama file : ') + ".txt"
 #2. masukkan jumlah asisten yang ingin diinput
jumlah_asisten = int(input("input perulangan : "))
 #3. membuat variabel untuk membuka file dengan operasi baca dan tulis 
buka_file = open(namafile, "w+")

# 4. menggunakan operasi try except untuk menjalankan program
try:
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    buka_file.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
#5. membuat perulangan untuk menginput berapa data yang dimasukkan sesuai jumlah asisten yang diinput
    for i in range(jumlah_asisten):
        nama = input().replace(" ","_")
        if len(nama) > 20:
            raise TypeError    #menggunakan raise agar apabila lebih dari 20 nama maka program dipaksa error 
        nim = input('input nim : ')
        angkatan = input('input angkatan : ')
#6. menulis file sesuai dengan inputan dari perulangan  di atas 
        buka_file.write("|"+ nama + " "*(22 - (len(nama))) + "| " + nim +" "*(10-(len(nim)))+ " | " + angkatan + " "*(9-len(angkatan)) + "|" + "\n")
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
#7. print berhasil apabila program di atas berhasil    
    print("Berhasil")
#8. print gagal apabila program di atas gagal sesuai dengan program try except    
except:
    print("Gagal")
#9. menutup file yang telah di isi     
buka_file.close()
 
