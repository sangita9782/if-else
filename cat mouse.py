cat1=int(input("enter number"))
mouse=int(input("enter number"))
cat2=int(input("enter number"))
if cat1<mouse and mouse<cat2:
    print("cat1")
elif cat1>mouse and mouse>cat2:
    print("cat2")
elif cat1<mouse and cat2<mouse:
    print("mouse")
else:
    print("none")
