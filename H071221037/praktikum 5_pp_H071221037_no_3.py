array1  = []
array2  = []
duplikat  = []

array1 = input('Input Array Pertama : ')
array2 = input('Input Array Kedua : ')

for i in array2:
    if i in array1:
        duplikat.append(i)
        duplikat.sort()
                
print(f'Terdapat {len(duplikat)} Duplikasi {duplikat}')

