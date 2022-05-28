exp_date=int(input("enter date"))
exp_month=int(input("enter month"))
exp_year=int(input("enter month"))
return_date=int(input("enter return date"))
return_month=int(input("enter return month"))
return_year=int(input("enter return year"))
if return_month==exp_month and return_year==exp_year:
    if return_date<exp_date:
        print("no fine")
    elif return_date>exp_date:
        fine=15*6
        print(fine)
    else:
        print("no fine")
elif return_month>=exp_month and return_year==exp_year:
    if return_date>=exp_date:
        fine=500*30
        print(fine)
    else:
        print("find charge")
elif return_month<=exp_month and return_year!=exp_year:
    if return_date<exp_date:
        fixed_fine=10000
        print(fixed_fine)
else:
    print("no fixed fine")
