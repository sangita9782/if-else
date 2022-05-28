basic_salary=int(input("enter"))
if basic_salary<=10000:
    HRA=basic_salary//100*20
    DA=basic_salary//100*80
    gross_salary=basic_salary+HRA+DA
    print(gross_salary)
elif basic_salary<=20000:
    HRA=basic_salary//100*25
    DA=basic_salary//100*90
    gross_salary=basic_salary+HRA+DA
    print(gross_salary)
elif basic_salary>=20000:
    HRA=basic_salary//100*30
    DA=basic_salary//100*95
    gross_salary=basic_salary+HRA+DA
    print(gross_salary)
else:
    print("none")