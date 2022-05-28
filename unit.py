unit=int(input("enter number"))
if unit>=1 and unit<=100:
  print("no charge")
elif unit>=101 and unit<=201:
  bill=unit*5/100
  print("amount",bill)
elif unit>=200:
  bill=unit*10/100
  print("amount",bill)
else:
  print("no electric")



