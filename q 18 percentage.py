physics=int(input("enter pysics"))
chemistry=int(input("enter chemistry"))
biology=int(input("enter biology"))
mathe=int(input("enter mathe"))
computer=int(input("enter computer"))
total=physics+chemistry+biology+mathe+computer
percentage=total/500*100
if percentage>=90:
    percentage("grade A")
elif percentage>=80:
    percentage("grade B")
elif percentage>=70:
    percentage("grade C")
elif percentage>=60:
    print("grade D")
elif percentage>=40:
    print("grade E")
else:
    print("f")