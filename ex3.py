# Vòng lặp trong python

"""
    Bài 1.Yêu cầu người dùng nhập vào 1 số tự nhiên
    1. Kiểm tra xem đó có phải số nguyên tố hay không
    2. In ra màn hình tất cả số nguyên tố nhỏ hơn n
"""

# n = int(input("Enter a number: "))
# if n<2:
#     print(n, 'is a composite number')
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print(n, 'is a composite number')
#             break
#     else:
#         print(n, 'is prime number')

"""
    Bài 2 Yêu cầu người dùng nhập vào 1 số tự nhiên khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""
# n = int(input("Enter a number: "))
#
# n0 = 1
# n1 = 1
# for _ in range(n):
#     print(n0)
#     n_new = n0 + n1
#     n0 = n1
#     n1 = n_new

"""
    Bài 3 Yêu cầu người dùng nhập vào 1 số tự nhiên khác 0
    In ra tất cả số Armstrong nhỏ hơn hoặc bằng n
    Định nghĩa số Armstrong: tổng các chữ số của số đó, với mỗi chu số được luỹ thừa với
    số mũ k bằng chính số đó, với k là chữ số của n
    Vi dụ: 153 là số Armstrong vì:
    153 có 3 chu số và 153 = 1^3 + 5^3 + 3^3
"""

# n = int(input("Enter a number: "))
# for number in range(1, n+1):
#     num_digits = len(str(number))
#     total = 0
#     for digit in str(number):
#         total += int(digit) ** num_digits
#     if number == total:
#         print(number, "is an Armstrong number")

# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10

"""
    Bài 4: Yêu cầu người dùng nhập vào 1 số nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương đương của số đó
"""

# n = int(input("Enter a binary number: "))
# sum = 0
# somu = 0
# while n != 0:
    # lay chu so cuoi
    # k = n % 10
    # bo chu so cuoi
    # n //= 10
    # Vi du bit o vi tri cuoi la 1, h = 0 => 1*2^0 = 1
#     sum += k * (2 ** somu)
#     somu += 1
# print(sum)

# cach 2
# n = input("Enter a binary number: ")
# num_digits = len(n)
# decimal_num = 0
# count = 1
# for digit in n:
#     decimal_num += int(digit) * 2**(num_digits-count)
#     count += 1
# print(decimal_num)

# cach 3 su dung enumerate
# n = input("Enter a binary number: ")
# num_digits = len(n)
# decimal_num = 0
# for index,digit in enumerate(n):
#     decimal_num += int(digit) * 2**(num_digits-index-1)
# print(decimal_num)

"""Bài 5:
    Tìm  số lớn nhất và nhỏ nhất trong dãy sau
"""
from math import inf
numbers = [2, 3, 1, 4, 5, -1, -2, -3, -4]

# print(max(numbers))
# print(min(numbers))

min_number = inf
max_number = -inf

for number in numbers:
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number
print(min_number, "min number")
print(max_number, "max number")