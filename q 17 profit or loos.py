actual_cost=int(input("enter cost"))
sale_cost=int(input("enter sell cost"))
if actual_cost<sale_cost:
    print("profit")
elif actual_cost>sale_cost:
    print("loss")
else:
    print("no profit no loss")
