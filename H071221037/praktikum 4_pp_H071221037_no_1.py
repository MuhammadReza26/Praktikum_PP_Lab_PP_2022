list = []
x = int(input('berapa banyak angka yang dimasukkan : '))
def sortiran() :
    for i in range(x) :
        y = int(input('masukkan angka :'))
        list.append(y)
    print(list)
    for i in range(x) :
     for j in range(i+1,x) :
      if list[j] < list[i] :
        angka = list[i]
        list[i] = list [j]
        list[j] = angka
    print(list)        

sortiran() 



                         





    


        






