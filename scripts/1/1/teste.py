import os

path = "C:\\Users\\Host02\\Documents\\analise2\\archives\\ms"

arr = os.scandir(path)

for file in arr:
    a = open(file.path, "r")
    b = a.read()
    print(b)
    a.close()


    
