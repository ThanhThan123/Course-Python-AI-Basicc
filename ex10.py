# Thực hành tính kế thừa trong lập trình hướng đối tượng
# class Car:
#     num_wheels = 4
#
#     def __init__(self, color, style):
#         self.__color = color
#         self.style = style
#
#     def change_color(self, new_color):
#         self.color = new_color
#     def change_style(self, new_style):
#         self.style = new_style
#
# # Lớp con có thể sử dụng phương thức của lớp cha. Nhưng ngược lại là không
# class FuelCar(Car):
#     def __init__(self, color, style, type):
#         super().__init__(color, style)
#         self.type = type
#         self.speed = 0
#
#     #  Tạo thêm phương thức cho lớp con
#     def change_speed(self, new_speed):
#         self.speed = new_speed
#
#     def stop(self):
#         self.speed = 0

# Khuyến khích thay đổi các giá trị bên trong phương thức
# if __name__ == "__main__":
#     my_car = Car(color ="red", style = "sport")
#     your_car = FuelCar(color ="blue", style = "sport", type = "sport")
#
#     print(my_car._Car__color)
#     your_car.change_speed(50)
#
#     your_car.num_wheels = 3 # Thay đổi thuộc tính lớp đúng đối tượng đó thay đổi
#     FuelCar.num_wheels # Thay đổi lun cho cả lớp đó


# Tính đóng gói (Encapsulation)
    # public: cho phép truy cập ở bên ngoài và bên trong lớp
    # protected: Chỉ cho phép truy cập bên trong lớp đó và các lớp con của lớp đó (k tồn tại trong python)
        # Quy ước trong python : đặt trước tên thuộc tính 1 dấu : _
        # print(my_car._color)
    # private: Chỉ có thể truy cập bên trong class đó (k tồn tại trong python)
        # Quy ước trong python : đặt trước tên thuộc tính 2 dấu : __
            # seft.__color = color # Khai báo
            #print(my_car(_Car.__color)) # Cách để truy cập

# Tính đa hình (Polymorphism)
    # Ví dụ thường được dùng là hàm len() được dùng cho nhiều kiểu dữ liệu khác nhau
        # print(len("VietNam"))
        # print(len([1, 2, 3, 4, 5]))
        # print(len({"Name": "Than", "Job":"engineer"}))


# Các loại file cơ bản
    # CSV

    #.txt
        # Mở file .txt
            # f = open(file_path, mode)
                # file_path: bao gồm đường dẫn tuyệt đối hoặc tương đối
                    # Đường dẫn tương đối: Từ vị trí hiện tại của tôi đến điểm đích
                        # relation_path = "./src/dataset.py"
                    # Đường dẫn tuyệt đối: Là đường đẫn đi từ gốc pc đến điểm đích
                        # absolute_path = "C:\\Users\\Admin\\PycharmProjects\\PythonProject\\my_script.py"
                # mode: file được mở dùng để làm gì
                    # Các loại mode
                    # "r": Mở file chỉ để đọc
                    # "w": Mở file chỉ để ghi (ghi đè nội dung cũ nếu có)
                    # "a": Mở file và gắn thêm nội dung mới vào cuối file
                    # "r+": Mở file vừa để đọc vừa để ghi
                    # "x": Tạo file mới
                # Đọc file 1 dòng (read)
                    # print(f.readline())
                # Đọc file trả về nhiều dòng
                    # print(f.read)
                    # print(f.readlines())
                    # print(list(f))
                # Viết file (w)
                    # f.write("Today is beautiful day \n")
                # Viết file nhiều dòng
                    # f.writelines(["Today is beautiful day \n", "Its not good"
                # Viết thêm dòng vào file
                    # f = open(relative_path, mode="a")
                # Đóng file thủ công
                    # f.close()
                # Đóng file tự động
                    # with open("data.txt") as f:
                        # print(f.read()) // or do something in here
                    # print("At the line, file is ready closed")
# relative_path = "file"
# absolute_path = "C:\\Users\\Admin\\PycharmProjects\\PythonProject\\my_script.py"
#
# f = open(relative_path, mode="a")
#
# f.write("\n 1991")
# f.close()
# f.write("\n 1991")

# Tìm hiểu về xử lý ngoại lệ
    # Error có 2 loại
        # Lỗi cú pháp (syntax error)
            # Xảy ra khi cú pháp được quy định của Python không được tuân thủ
            # Chương trình sẽ không thể chạy khi có lỗi này
        # Lỗi logic (Logic error) (Exception)
            # Lỗi xảy ra sau khi các cú pháp đều đã thoả mãn quy định của Python.
                # Phép chia cho số 0
                # Thực hiện phép cộng giữa số và 1 chuỗi ký tự
                # Đến chỗ lỗi thì nó không chạy
    # Một vài ngoại lệ phổ biến
        # IndexError: Xảy ra khi chỉ số của List(Tuple) nằm ngoài khoảng cho phép
        # AttributeError: Xảy ra khi truy cập đến 1 thuộc tính không tồn tại của lớp
        # ImportError: Xảy ra khi import 1 module hoặc 1 thư viện không tồn tại
        # KeyError: Xảy ra khi Key(từ khoá) không tồn tại
        # NameError: Xảy ra khi truy cập 1 biến không tồn tại
        # TypeError: Không hỗ trợ cho string và int
        # ZeroDivisionError
# Khối lệnh try và except (để xử lý ngoại lệ)
    # try
        # statements
    # except:
        # statements
    # try:
    #     a = 5
    #     a = a / 0
    # except :      # nếu không thêm loại xử lý nó sẽ xử lý mọi loại ngoại lệ (vd ZeroDivisionError)
    #     print("Something wrong is here")
    # else:
    #     print("everything is find") # chỉ xảy ra khi không có ngoại lệ
    # finally:
    #     print('this message will always be printed") # Sẽ lun được thực thi dù cho try hoặc except có lỗi hay không
