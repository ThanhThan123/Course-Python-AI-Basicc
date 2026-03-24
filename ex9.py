# Tìm hiểu sự khác nhau giữa hàm và phương thức
    # Hàm
        # Nằm bên ngoài và không liên quan đến class
        # Có thể gọi độc lập không phụ thuộc và lớp hoặc đối tượng cụ thể nào
    # Phương thức
        # Nằm bên trong lớp
        # Là 1 thành phần của đối tượng
        # Chỉ có thể được gọi thông qua lớp hoặc đối tượng

"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 chuỗi ký tự bất kỳ,
    hàm trả về danh sách bao gồm các ký tự xuất hiện ở cả
    2 chuỗi
"""

# First approach
# def common_chars(str1, str2):
#     char_count = [] # contain letter  appearing in both string
#     str1 = str1.replace(" ","")
#     str2 = str2.replace(" ","")
#     for char in str1:
#         if char in str2:
#             if char not in char_count:
#                 char_count.append(char)
#     return char_count
# string1= "today is Sunday"
# string2 = "You look tired"
#
# print(common_chars(string1, string2))

# Second Approach
# def common_chars(str1, str2):
#     str1 = set(str1.replace(" ",""))
#     str2 = set(str2.replace(" ",""))
#     result = str1.intersection(str2)
#     return list(result)
# string1= "today is Sunday"
# string2 = "You look tired"
#
# print(common_chars(string1, string2))

"""
    Yêu cầu người dùng nhập vào 1 chuỗi ký tự bất kỳ 
    Kiểm tra xem chuỗi đó có phải là 1 palindrome hay không
    Định nghĩa palindrome: 1 palindrome là 1 từ hoặc số mà nếu từ
    hoặc số đó giữ nguyên giá trị bất kể đọc từ trái sang phải hay đọc từ phải sang trái
"""
#
# n = input('Enter a number or string:')
# if n == n[::-1]:
#     print(n, "is a palindrome")
# else:
#     print(n, "is not a palindrome")

# Tìm hiểu về lập trình hướng đối tượng
    #Class(Lớp) và Đối tượng(Object)
        #Class (Lớp)
            # Vd: Bản vẽ của xe Ô tô
            # Định nghĩa Lớp : Viết liền và chữ cái đầu viết Hoa
                # Oto, Motobike
            # Định nghĩa hàm khởi tạo:
                # __init__: Phương thức khởi tạo dùng để làm các công việc cần thiết khi một đt mới được tạo ra
                # self: Luôn là tham số đầu tiên của tất cả các phương thức của lớp
                # Thuộc tính (Attribute)
                    # Thuộc tính dùng để phân biệt đối tượng này với đối tượng kia
                        # Thuộc tính lớp : Đây là thuộc tính chung cho tất cả mọi đối tượng của lớp
                            # num_wheels = 4 # bất kỳ thay đổi nào đến thuộc tính lớp này sẽ có hiệu lực cho tất cả
                        # Thuộc tính thể hiện
                            # self.color = color #  Đặc trưng riêng của mỗi đối tượng
        #Object(Đối tượng)
            # Vd: Tạo ra thực thể cụ thể dựa trên Lớp
            # Khởi tạo một đối tượng mới
                # my_car = Car(color="Black", stype="Sedan")
            # Sử dụng phương thức của lớp trong đối tượng
                # my_car.change_color('Orange')
            # Truy cập thuộc tính của đối tượng: instance_name.attribute = value
                # my_car.color = "orange"
            # Xoá thuộc tính của đối tượng
                # del my_car.color
# Các đặc điểm chính trong lập trình hướng đối tượng:
    # Inheritance : Tính kế  thừa
        # Class ChildClass(ParentClass)
        # Tạo ra lớp con kế thừa lớp cha
            # class FuelCar(Car)
            # Truy cập giống với mycar.change_color("Yellow")
        # Viết đè phương thức
            # class FuelCar(Car):
                # num_wheels = 4
                # def __init__(self, color, style, fuel_type):
                    # self.color = color
                    # self.style = style
                    # self.fuel_type = fuel_type
                    # self.speed=0
        # Hàm super() : Gọi từ class Cha và cho class cha chạy trước
            # class FuelCar(Car)
                # num_wheels = 4
                # def __init__(self, color, style, fuel_type):
                    # super().__init__(color, style)
                    # self.fuel_type = fuel_type
    # Encapsulation: Tính đóng gói
    # Polymorphism; Tính đa hình
    # Abstraction: Tính trừu tượng
