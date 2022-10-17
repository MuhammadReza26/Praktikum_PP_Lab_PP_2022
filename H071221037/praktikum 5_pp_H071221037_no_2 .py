print('Selamat datang untuk memulai silahkan input data anda')
nama = input('input nama : ')
umur = input('input umur : ')
alamat = input('input alamat : ')

while True : 
 print('========================================')
 print(f'selamat datang {nama} silahkan pilih opsi')
 print('1. Detail anda\t')
 print('2. ubah nama ')
 print('3. ubah umur')
 print('4. ubah alamat')
 print('5. keluar')
 print('========================================')
 opsi = input('input opsi : ')
 print('========================================')

 if opsi == '1' :
    print('Data anda adalah  ')
    detail_diri = {
        'nama'      : nama,
        'umur'      : umur,
        'alamat'    : alamat
    }
    print(detail_diri)
    print('===================================')


 if opsi == '2' :
    nama2 = input('input nama baru : ')
    detail_diri = {
        'nama'      : nama2,
        'umur'      : umur,
        'alamat'    : alamat
        }
    print(detail_diri)
    print('data anda selesai di perbarui ')
    print('===================================')

 elif opsi == '3' :
    umur2 = input('masukkan umur baru : ')
    detail_diri = {
        'nama'      : nama2,
        'umur'      : umur2,
        'alamat'    : alamat
        }
    print(detail_diri)
    print('data anda selesai di perbarui ')
    print('===================================')

 elif opsi == '4' :
    alamat2 = input('masukkan alamat baru : ')
    detail_diri = {
        'nama'      : nama2,
        'umur'      : umur2,
        'alamat'    : alamat2
        }    
    print(detail_diri)  
    print('data anda selesai di perbarui ')
    print('===================================')

 elif opsi == '5' : 
    print('selamat tinggal', nama2 )
    print('===================================')
    break




