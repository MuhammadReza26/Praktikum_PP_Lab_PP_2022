# Tugas Tambahan Mengecek kevalidan password

# Minimal 8 karakter
# Harus memenuhi syarat dibawah : 
# huruf besar: A-Z
# huruf kecil: a-z
# angka: 0-9
# salah satu karakter khusus: @#$%^&+=
import re
pola = "^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("password: ")
hasil = re.findall(pola, password)
if (hasil):
    print ("Valid password")
else:
    print ("Password not valid")
