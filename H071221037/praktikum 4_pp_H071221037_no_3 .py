def faktorial (nilai) :
    if nilai == 0 : 
        return 1
    else :
       return nilai * faktorial (nilai-1)

nilai = int(input('masukkan angka : '))
faktor = faktorial(nilai)
print(faktor)            







       
    
