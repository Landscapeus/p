import math
x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
forgotname=str(input("Podaj znak dzialania, ktore chcesz wykonac: "))
if forgotname=='+':
    suma=(x+y)
    print("Suma liczb wynosi ",suma)
elif forgotname=='-':
    something=(x-y)
    print("Roznica liczb wynosi ",something)
elif forgotname=='*':
    lioczyn=(x*y)
    print("Iloczyn liczb wynosi ",lioczyn)
elif forgotname=='/':
    if y==0:
        print("STOP! YOU VIOLATED THE LAW! You can't divide by zero.")
    else:
        lioraz=(x/y)
        print("Iloraz liczb wynosi ",lioraz)
elif forgotname=="**":
    power=(x**y)
    print("Potenga liczby x do y wynosi ",power)
elif forgotname=='%':
    if y==0:
        print("STOP! YOU VIOLATED THE LAW! You can't divide by zero.")
    else:
        moderator=(x%y)
        print("Reszta z dzielenia x przez y wynosi ",moderator)
else:
    print("To nie jest znak działania")