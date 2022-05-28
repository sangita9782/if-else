age=int(input("enter"))
age1=int(input("enter"))
age2=int(input("enter"))
if age>age1 and age>age2:
    print(" age is oldest")
elif age1>age and age1>age2:
    print("age1 is oldest")
elif age2>age and age2>age1:
    print("afe2 is oldest")
elif age<age1 and age<age2:
    print("age is youngeest")
elif age1<age and age1<age2:
    print("age1 is youngest")
elif age2<age and age2<age1:
    print("age2 is youngest")
else:
    print("none")