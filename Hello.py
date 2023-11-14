import random
import math
import time

#print("Hello wrlod");

#donotforgetdis
'''
use
les
sss
'''
'''
czo=2137;
gopro=21.37;

print(czo);
print('%.20f'%gopro);

print("wartosc zmiennej czo wynosi:", czo);
print("wartosc zmiennej czo wynosi: " +str(czo));


imie=input("Jak brzmi twe imie? ");
wiek=int(input("Ile masz lat?"));

print("Czesc, ", imie);

print("masz ", wiek," lat.");
los=random.randint(0, 222);
print(los)
potega=math.pow(44, 2)
print(potega)
suma=2100+37
roznica=999-333
iloczyn=99*0
iloraz=33/11
potega2=99**2
modulo=6%2

liczba=int(input("Podaj liczbe: "))

if liczba>0:
    print("Liczba jest dodatnia.")
elif liczba==0:
    print("Liczba to zero.")
else:
    print("Liczba jest ujemna.") #if
#print("yadadada") if <insert warunek> else print("gluten tag") #worse if
'''
#for i in range(10):
#    print("Numer: ", i)#pentla for(theworthy)

#for e in range (1,111):
#    if e%2==0:
#       print(e)

#for reee in range (1,111,2):
#    print(reee)

#for pee in range (110,0,-1):
#    print(pee)

#for leetera in "Minos": #for but literowane und s=NO
#    if leetera=="s":
#        break
#    print(leetera)

#for reetera in "Sisyphus": #four but literowane und CONTINUE?
#    if reetera=="y":
#        continue
#    print(reetera)

#lolczba=int(input("Podaj pan(zer) liczbe: "))

#while lolczba<0:
#    liczba=int(input("Podaj innom liczbe: ")) # do NOT use print() (in case of moronism use ctrl+C)

#def powitanie():         #Na poczontku to dej
#    print("Guten tag")   #definiowanie 
#powitanie()              #uywanie

#def powitanie_imienne(imie):
#   print("Witaj", imie, " !") #def but complicated. a tad bit
#powitanie_imienne("WAAAALUIGI")

#def dzielenie(dzielna, dzielnik): # def but a tad tad bit complicated
#    if dzielnik==0:
#        return "STOP! You violated the law!"
#    else:
#        return dzielna/dzielnik

#print(dzielenie(0,5465))
#print(dzielenie(333333333333333333333333,0)) #print.exe
#iloraz=dzielenie(3321,3)
#print(iloraz)

#lista=[1,2,3,7,9,4,8,6,5] # lista liczb
#print(type(lista))
#print(lista)
#print(*lista)
#print(*lista, sep=";") #* sie zepsulo

#lista.sort() #sortowanie lol
#print(lista)

#lista.reverse() #atsil
#print(lista)

#lista.sort(reverse=True) # posortowana atsil
#print(lista)

#print(lista.count(3))

#lista.remove(3)
#print(lista)

#lista.append(1) # +1 do lista
#print(lista)

#print(lista[0])
#print(lista[8])

#print(len(lista)) #lista lenght

#for reeeeeeeee in lista
#   print(reeeeeeeee)

#krotka=(1,2,3) #lista but NO CHANGING
#print(krotka)

#krotka2=1,2,3.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001,"Sisyphus" #hehe no () 
#print(krotka2)

#dicktionary={} #słownik
#dicktionary["Stefano"]=332121370
#dicktionary["Józef"]=333666999
#dicktionary={
#    "Stefano":332121370,
#    "Józef":333666999,
#    "Mietek":222444888
#}
#print(dicktionary["Stefano"])
#for imie, numer in dicktionary.items(): #magia
#    print("%s ma numer %d" %(imie, numer))

#print(dicktionary.keys())
#print(dicktionary.values())

#del dicktionary["Józef"] #delet this thing

#start=time.time() #złołżoność liniowa
#lilsta=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] 
#for i in lilsta:
#    print(i)

#end=time.time()
#print(end-start)
start=time.time() #złooność kwadratowa
n=int(input("Podaj liczbę całkowitą: "))
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
end=time.time()
print(end-start)