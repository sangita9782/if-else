age=int(input("enter age"))
sex=input("enter sex")
wages=int(input("enter wages"))
if sex=="m":
    if age>=18 and age<30:
        a=wages*700
        print("total",a)
    if age>=30 and age<=40:
            b=wages*800
            print("total",b)
    else:
        print("aproprite")
elif sex=="f":
    if age>=18 and age<30:
        c=wages*750
        print("total",c)
    if age>=30 and age<=40:
           d=wages*850
           print("total",d)
    else:
         print("not aproprita")
else:
    print("error")