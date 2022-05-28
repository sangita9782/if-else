quantity=int(input("enter"))
total_cost=quantity*100
if total_cost>1000:
    unit=total_cost*10/100
    cost=total_cost-unit
    print("totalcostof 10%:",cost)
else:
    print("total cost")