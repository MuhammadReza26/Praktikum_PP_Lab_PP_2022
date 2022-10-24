#1 buat variabel untuk input nama file
nama = input('nama file : ')
#2 buat variabel untuk input nama file hasil salinan
nama2 = input('nama file salinan : ')

#3. membuat file dengan nama sebagai judul 
with open (f"{nama}.txt","w") as file :
#4. menulis file yang sudah ada sesuai dengan soal     
    file.write("baris pertama \nbaris kedua \nseterusnya \n") 
#5. membuat perkondisian untuk menghasilkan berhasil atau gagal
if nama != nama2   :
    #6. membaca file yang telah dibuat 
     with open(f"{nama}.txt", "r") as file :
        #7. menulis file hasil salinan dengan isi yang ada pada file yang pertama 
      with open(f"{nama2}.txt", "w") as file_salinan:
        file_salinan.write(file.read())
     print('berhasil')
else :
    print('gagal')


