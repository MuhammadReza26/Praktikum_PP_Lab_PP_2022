index0 = int(input('masukkan nilai matriks pertama index 1,1 : '))
index1 = int(input('masukkan nilai matriks pertama index 1,2 : '))
index2 = int(input('masukkan nilai matriks pertama index 2,1 : '))
index3 = int(input('masukkan nilai matriks pertama index 2,2 : '))
index4 = int(input('masukkan nilai matriks kedua index 1,1 : '))
index5 = int(input('masukkan nilai matriks kedua index 1,2 : '))
index6 = int(input('masukkan nilai matriks kedua index 2,1 : '))
index7 = int(input('masukkan nilai matriks kedua index 2,2 : '))

matriks1 = [
    [index0,index1],
    [index2,index3]]

matriks2 = [
    [index4,index5],
    [index6,index7]]

a0 = (index0 * index4) + (index1 * index6 )
a1 = (index0 * index5) + (index1 * index7 )
b0 = (index2 * index4) + (index3 * index6)
b1 = (index2 * index5) + (index3 * index7)

hasil = [
    [a0,a1],
    [b0,b1]]

print(hasil)





