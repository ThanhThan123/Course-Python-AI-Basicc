"""
    Nhập vào 2 số:
    - 1 số đa diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý : Năm nhuân là năm thoả mãn 1 trong 2 điều kiện sau:
    -   Năm đó chia hết cho 4 nhưng không chia heets cho 100
    -   Năm đó chia hết cho 400
"""

# year = int(input("Nhập vào số năm  đó: "))
# month = int(input("Nhập vào số tháng của năm đó "))
# if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
#     if month == 2:
#         print(29)
#     elif month in [1,3,5,7,8,10,12]:
#         print(31)
#     else:
#         print(30)
# else :
#     if month == 2:
#         print(28)
#     elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10  or month == 12:
#         print(31)
#     else:
#         print(30)

""" Bai 2  
        Yeu cau nguoi dung nhap vao 3 so a,b,c
        Tim nghiem cua phuong trinh bac 2 
        ax^2 +bx + c = 0
    """
# a=float(input("Enter a:"))
# b= float(input("Enter b:"))
# c=float(input("Enter c:"))
#
# if a == 0:
#     if b == 0 and c == 0:
#         print("infinity many solution")
#     elif b == 0 and c != 0:
#         print('No solution')
#     else: # b != 0
#         print("x =", -c/b)
# else:
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("No solution")
#     if delta == 0:
#         print("x = ", float(-b / (2 * a)))
#     else:
#         x1 = (-b + delta ** 0.5) /(2 * a)
#         x2 = (-b - delta ** 0.5) / (2 * a)
#         print("x1 and x2", x1, x2)

"""
     Cau3.Yeu cau nguoi dung nhap vao 3 so nguyen duong
     1. Kiem tra xem day co phai so do 3 canh cua 1 tam giac khong
     2. Neu co thi kiem tra tiep xem day la tam giac can, tam giac deu,
     tam giac vuong, tam giac vuong can hay tam giac thuong
     3. Kiem tra xem tam giac co goc tu hay khong
     4. Tinh dien tich cua 1 tam giac
"""
from math import sqrt
a=int(input("Enter a:"))
b= int(input("Enter b:"))
c=int(input("Enter c:"))
if a > 0 and b > 0 and c > 0 and (a + b > c) or (a + c > b) or (b + c > a):
    if a == b and b == c:
        print('Day la tam giac deu')
    elif a == b or b == c or c == a:
        if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
            print('Day la tam giac vuong can')
        else:
            print('Day la tam giac vuong')
    elif (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
            print('Day la tam giac vuong')
    else:
        print('Day la tam giac vuong')

    p = (a + b + c) /2
    area = sqrt((p*(p-a)*(p-b)*(p-c)))
    print('area:', area)
else:
    print(" Day khong phai 3 canh cua 1 tam giac")