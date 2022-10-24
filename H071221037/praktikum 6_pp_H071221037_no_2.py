#1. masukkan inputan untuk nama file 
nama = input('nama file : ')
#2. masukkan input untuk nama file hasil salinan 
nama2 = input('nama file hasil salinan : ')

#3. buat file dengan nama file sebagai judulnya 
with open (f"{nama}.txt","w") as file :
# 4.1 membuat variabel untuk setiap baris yang diinginkan agar dapat ditambahkan format rata kanan     
    a =  input('masukkan inputan baris pertama : ')
    b =  input('masukkan inputan baris kedua   : ')
    c =  input('masukkan inputan baris ketiga  : ')
#4. menulis file sesuai dengan isi yang diminta    
    file.write(f"{a}\n{b}\n{c}\n") 
# cari len terpanjang 
if len(a) > len(b) and len(a) > len (c):
    terpanjang = len(a)
elif len (b) > len (a) and len (b) > len (c):
    terpanjang = len(b)
else : 
    terpanjang = len(c)
#5. buat perkondisian  agar dapat menghasilkan kondisi berhasil atau gagal
if nama != nama2   :
#6. menulis file salinan dengan isi yang ada di file pertama 
    with open(f"{nama}.txt", "r") as file :
        with open(f"{nama2}.txt", "w") as file_salinan:
#7. memberikan format rata kanan pada isi file salinan             
         file_salinan.write(f"{a.rjust(terpanjang)}\n")
         file_salinan.write(f"{b.rjust(terpanjang)}\n")
         file_salinan.write(f"{c.rjust(terpanjang)}\n")
#8. menghasilkan berhasil bila kondisi diatas berhasil diselesaikan         
    print('berhasil')
#9. menghasilkan gagal bila kondisi diatas tidak dijalankan /diselesaikan     
else : 
    print('gagal')

# nama = 'alim'
# print(f'nama saya adalah{nama}\n')    

# # file_salinan.write(f"{a.rjust(len(a))}")
