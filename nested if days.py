day=input("enter day")
time=input("enter time")
if day=="monday":
    if time=="breakfast":
        print("poori sabzi")
    elif time=="lunch":
        print("sambhar rice")
    elif time=="dinner":
        print("chicken rice")
    else:
        print("chowmin")
elif day=="tuesday":
    if time=="breakfast":
        print("poha")
    elif time=="lunch":
        print("rajma rice")
    elif time=="dinner":
        print("roti sabzi")
    else:
        print("milk")
else:
    print("wednesday")
