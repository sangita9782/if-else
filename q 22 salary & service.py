salary=int(input("enter"))
service=int(input("enter"))
if service>5:
    bonus=salary+salary*5/100
    print("salary",bonus)
else:
    print("none")
    