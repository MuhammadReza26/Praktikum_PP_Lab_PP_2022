import re

try :
    inputan = input('masukkan inputan : ')
    match = re.search("[2468a-zA-Z]{40}[13579\s]{5}", inputan)
    if match :
        print("true")
    else :
        print("false")
except :
    print("false")