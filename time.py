time=float(input("enter time"))
if time>=9.00 and time<=13.00 :
    print("1st coding class")
elif time>13.00 and time<14.00:
    print("lunch")
elif time>=14.00 and time<=17.00:
    print("2nd coding class")
elif time>17.00 and time<18.00:
    print("snacks")
elif time>18.00 and time<22.00:
    print("3rd coding class")
else:
    print("no more class")


