# Biểu thuc if, if else, if elif, else
a = 4
if a > 3:
    pass
    print("next")
elif a == "Today":
    print("Today")
else:
    print("Tomorrow")

# Bieu thuc match case
b = "Tuesday"
match b:
    case "Monday":
        print("Today is Monday")
    case "Tuesday": print("Today is Tuesday") #rut gon khoi lenh tren cung 1 dong
    case _: print("invalid day")

# Toan tu 3 ngoi Dung de gan da tri dua vao bien khac
x = 5
number = "Even" if x % 2 == 0 else "Odd"
# Bieu thuc if long nhau
x = 6
if x % 2 == 0:
    if x % 3 == 0:
        print('x is divisible by 6')
    else:
        print('x is not divisible by 2 but not by 3')
else :
    if x % 3 == 0:
        print('x is divisible by 3 not by 2')
    else:
        print('x is not divisible by 3 but not by 2')
