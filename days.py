days=int(input("enter days"))
if  days<=5:
    print(days*2)
elif days>=6 and days<=10:
    print(days*3)
elif days>=10 and days<=15:
    print(days*4)
elif days>15:
    print(days*5)
else:
    print("no day")