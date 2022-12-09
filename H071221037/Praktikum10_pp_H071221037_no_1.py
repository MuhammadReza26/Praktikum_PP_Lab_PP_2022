import re
 
def menu():    
    print('=' * 50)
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print('=' * 50)
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data Pada File')
    print('4. Save Data Pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')
    print('=' * 50)

menu()
opsi = input('Pilih Opsi Anda : ')
while opsi != '6':
    
    if opsi == '5':
        nama = input('Masukkan Nama : ')
        a = True
        while a == True :
                email = input('Email : ')
                syarat_email = '^[a-z0-9]*@student.unhas.ac.id$'
                cocok_email = re.search(syarat_email,email)
                if cocok_email:
                    a = False
                else:
                    print('=' * 50)
                    print('Email yang Anda Masukkan Salah')
                    print('=' * 50)   
    
        while a == False:
            password = input('Masukkan Password : ')
            if len(password) >= 8 and len(password) <= 20:
                syarat_password = "[A-Z]+[a-z]+[0-9]+"
                cocok_password = re.search(syarat_password,password)
                if cocok_password:
                    a = True
                else:
                    print('Gunakan minimal 1 Huruf Kapital,Huruf Kecil,dan Angka')    
            else:
                print('=' * 50)
                print("Password harus memiliki panjang 8 - 20 karakter")
                print('=' * 50)

    elif opsi == '1':
        try:
            if nama == None and email == None and password == None:
                print('=' * 50)
                print('Data saat ini kosong') 
            else:
                print('Data Anda Adalah')
                print('=' * 50)
                print(f'Nama : {nama}\nEmail : {email}\nPassword : {password}')
        except:
            print('=' * 50)
            print('Data saat ini kosong')

    elif opsi == '2':
        try:
            if nama == None and email == None and password == None:
                print('=' * 50)
                print('Data saat ini kosong')
            else:
                nama = input('Masukkan Nama Yang Baru : ')         
        except:
            print('=' * 50)
            print('Data saat ini kosong')
    
    elif opsi == '3':
        try:
            nama_file = input('Masukkan Nama File : ')
            file = open(f'{nama_file}.txt','r')
            jumlah = file.read()
            syarat_file = 'Nama'
            cocok_file =re.findall(syarat_file,jumlah)
            print('Jumlah Data pada File : ',len(cocok_file)) 
        except:
            print('=' * 50)
            print(f'Tidak Terdapat File Dengan Nama {nama_file}.txt')      
    
    elif opsi == '4':
        try: 
            if nama == None and email == None and password == None:
                print('=' * 50)
                print('Data saat ini kosong')
            else:
                nama_file = input('Masukkan Nama File : ')
                # pakai a+ untuk membuat file baru
                file = open(f'{nama_file}.txt','a+')
                file.close()
                file = open(f'{nama_file}.txt','r+')
                file.write("+" + "="*47 +'\n')
                file.write("|" + " Data yang Tersimpan" + " "*42 +"\n")
                file.write("+" + "="*47 + '\n')
                file.close()
                file = open(f'{nama_file}.txt','a+')
                file.write("|" + " " + 'Nama' + " "*10 + ":"+nama+'\n'+"| " + "Email" + " "*9+ ":"+email+'\n' +"| " +'Password' + " "*6 + ":" +password+ "\n"+"+" + "="*47+'\n')
                file.close()
                nama = None
                email= None
                password = None
                print('=' * 50)
                print('Berhasil')
        except:
            print('=' * 50)
            print('Data saat ini kosong')
    menu()
    opsi = input('Pilih Opsi Anda : ')
    

print('=' * 50)
print('Sampai Jumpa Lagi')
print('=' * 50)                    


