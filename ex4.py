# thực hiện hàm trong python

# def function_name(parameters):
#     statements
#     [return value]

# Tham số giá trị yêu cầu và đối số gia trị truyền vào khi gọi hàm

# Các dạng đối số : đối số vị trí và đối số từ khoá và đối số mặc định
# Đối số vị trí truyền đúng thứ tự khi truyển đối số vào
    # def func(name, job):
    #     print(name, "is a", job)
    #
    # func("Than", "Developer")

# Đối số từ khoá
    # def func(name,job):
    #     print(name, "is a", job)
    #
    # func(job="Developer", name="Bob")

# Kết hợp đối số vị trí và từ khoá (ds vtr truoc tu khoa)
    # def func(name, job, location):
    #     print(name, "is a", job, "in a", location)
    #
    # func("Bob", job="Developer",location="Gotham" )
# Default agrument
    # def func(name, job, location="Gotham"):
    #     print(name, "is a", job, "in a", location)
    # func("Bob", job="Developer" )
# DocString
# def get_sum(a,b):
    #     """
    #     Sum up 2 numbers and return the result
    #     Parameters:
    #     a.firstNumber
    #     b.SencondNumber
    #     Returns
    #           The sum of the two numbers
    #     """
    #     return a+b
    # print(get_sum(2,3))
#Các hàm tích hợp sẵn
    # print : in giá trị ra màn hình
    # len  : truyền độ dài ví dụ: len("Today") hoặc len([1,2,3,4,5])
    # range: Tạo giá trị liên tục từ 0
    # str: chuyển giá trị số thành chuỗi giá trị
    # int : truyền chuỗi giá trị thành số
    # float: chuyển giá trị nguyên thành thực
    # type:
    # min: trả giá trị nhỏ nhất của mảng
    # max: trả giá trị lớn nhất
    # sorted: Sắp xếp giá trị theo thứ tự giảm hoặc tăng dần sorted([3,4,1,2],reverse=True)
    # input : Nhận giá trị từ người dùng thông qua bàn phím
    # sum :Trả về Tổng của các soos trong 1 danh sach
    # abs: Trả về giá trị tuyệt đối của 1 số
    # round:Làm tròn 1 đến 2 chữ số thập phân
# Các hằng số giá trị trong module math
    # from math import e, pi, tau, inf, nan
    # e: số euler ~ 2.7182
    # pi: số pi ~ 3.1415
    # tau: Số tau ~ 6.2831
    # inf: Dương vô cùng
    # nan: Đây khong phải số hợp lệ
# Các hàm toán học trong module math
    # from math import sqrt, pow, log, log2, log10, exp, degrees, radians
    # sqrt  : Trả về căn bậc 2 của 1 số ~ sqrt(16) ~ 4
    # pow   : Trả về luỹ thừa của 1 số ~ pow(4,3) ~ 64
    # log   : Trả về loga cơ số tự nhiên (loga nepe) của 1 số ~ log(3) ~ 1.0986
    # log2  : Trả về loga cơ số 2 của 1 số ~ log2(8) ~ 3
    # exp  : Trả ve giá trị với cơ số tự nhiên của 1 số ~ exp(2) ~ 7.3890
# Các hàm trong module random
    # from random import randint, random, choice, shuffle
    # randint: Trả về 1 số tự nhiên ngẫu nhieen giữa hai số

"""
    Bài 1 Viết hàm tính và trả về khoảng cách giua hai điểm
        -A(xa, ya, za)
        -B(xb, yb, zb)
    trong không gian 3 chiều
"""
    # from math import sqrt, pow
    # def caculate_distance(a, b):
    #     distance = 0
    #     for i in range(len(a)):
    #         distance += (b[i] - a[i]) ** 2
    #     return sqrt(distance)
    #
    # a_coord= (1,3,6)
    # b_coord= (2,-1,-3)
    #
    # result = caculate_distance(a_coord,b_coord)
    # print(result)

#Hàm zip
    # a = [1, 3, 5]
    # b = [2, 4, 6]
    # for i,j in zip(a,b):
    #     print(i, j)

# Các kieu dữ liệu cơ bản trong python
    # List: là 1 chuỗi giá trị các phần tử: có thứ tự, khả biến,
    # Dictionary
    # Tuple
    # Set
# Cắt list : list_name[begin:end:step]
    #  data = ["red","green","blue","yellow","black"]
    #  print(data[0:3]) -> red ,green ,blue
    #  print(data[::-1]) lấy giá trị từ phải sang trái
# Insert: chèn giá trị cụ thể tại vị trí cụ thể
# : Inplace function : Thay đổi ngay tại chỗ không trả về gì
    # data = [2, 4, 6]
    # data.insert(1, 10)
    # print(data)
# Hàm append : chèn vào cuối mảng (append phần tử mới)
#     data = [2, 4, 6]
#     data.append( 10)
#     print(data)
# Hàm extend (extend từng phần tử khác nhau)
    # data = [2, 4, 6]
    # data.extend([10, 6, 2, 3])
    # print(data)
# Sử dụng toán tử cộng
    # data = [2, 4, 6]
    # data = data + [3, 5]
    # print(data)
# Toán tử xoá (pop) xoá tại phần tử index
    # data = [2, 4, 6]
    # removed_item = data.pop(0)
    # print(data)
    # print(removed_item)
#  del (cách 2)
    # data = [2, 4, 6]
    # del data[2]
    # print(data)
#  del (cách 3)
    # data = [2, 4, 6]
    # del data[0:2]
    # print(data)
# remove xoá phần tử đầu tiên khỏi list_name
    # data = [2, 4, 6, 6]
    # data.remove(6)
    # print(data)
# clear
    # data = [2, 4, 6]
    # data.clear()
    # print(data)
# len
    # data = [2, 4, 6]
    # print(len(data))
# Tìm phần tử trong list
    # data = [2, 4, 6]
    # print(data.index(2))
# Hàm sort or Sorted
# Hàm count đếm giá trị xuất hiện bao nhiêu laanf trong mảng

"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1: 1 list bao gồm các số bất kỳ
    2: 1 số tự nhiên k
    Trả về kết quả là 1 list trong đó các phần tử bị dịch
    sang ben trái k đơn vị
    
    Ví dụ: input: array = [1, 2, 3, 4, 5]
    k = 2
    Output:
    array = [3, 4, 5, 1, 2]
"""

def shift_array(array, k):
    num_elements = len(array)
    new_array = [0] * num_elements
    for i in range(num_elements):
        new_array[i] = array[(i+k)%num_elements]
        print(i, i+k, new_array)
    return new_array

data = [1, 2, 3, 4, 5, 6]
k = 2
result = shift_array(data, k)
print(result)

