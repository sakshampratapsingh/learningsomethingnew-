TEMP=int(input('enter the temperature in degree celsius: '))
if TEMP<0:
    print("freezing cold")
elif TEMP>=0 and TEMP<=10:
    print("very cold")
elif TEMP>=10 and TEMP<=20:
    print("cold")
elif TEMP>=20 and TEMP<=30:
    print("pleasant")
elif TEMP>=30 and TEMP<=40: 
    print("hot")
else:
    print("very hot")