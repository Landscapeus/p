print("This is some sort of sorting program idk man.")# I have no idea what I'm doing
brejncancar=[]
lungcancar=0
while lungcancar==0:
    eent=int(input("Please insert number of characters you want to sort. "))
    for pee in range(eent):
        brejncancar.append(int(input("Please insert a number. ")))
    print("This is the list before sorting, right? ",brejncancar)
    lungcancar=int(input("If you want to change your list, write 0. If not, write any other number. "))
skincancar=int(input("If you want your list to be sorted from smallest to largest, write anything but 1. If you want it inverted, write 1. "))
if skincancar==1:
    brejncancar
    print("This is your reversed and sorted list: ",brejncancar)
else:
    brejncancar
    print("This is a sorted list... but not sure if made as intended. Idk man, i have no idea what im doing. ",brejncancar)