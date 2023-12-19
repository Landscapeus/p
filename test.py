def sortowanie_babelkowe(lista):

    n = len(lista)
    
    while n > 1:

        zamien = False
        for l in range(0, n-1):

            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1
        print(lista)
        if zamien == False: break
        
    return lista
print("test.exe")
man=[]       
markEplier=int(input("Please insert a number of how many numbers thee want to have in thy list: "))
for e in range(markEplier):
    man.append(int(input("Please insert a number: ")))

sortowanie_babelkowe(man)