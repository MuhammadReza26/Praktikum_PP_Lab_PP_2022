def isprime(angka) :
  for i in range(2,angka) :
    if (angka % i == 0) :
      return False
  return True    

angka = int(input('masukkan angka : '))
prima = isprime(angka)
if prima == True :
   print('Ini bilangan prima')
else :
  print('Ini bukan bilangan prima')   


