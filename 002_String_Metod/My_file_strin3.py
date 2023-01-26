x=0
if x>0:
    print ("Х больше 0")
elif x<0:
    print("Х меньше 0")
else:
    print("Х = 0")
print('Tere tulemast')

idcode='38405230460'
if len(idcode)==11:
    print('Ид верный')
else:
    if len(idcode)>11:
        print('Код длинный')
    else:
        print('код короткий')