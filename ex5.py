# list
"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận,
    kết quả trả về là ma trận tổng của chúng. Nếu phép
    cộng không thực hiện được thì trả về giá trị 0
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    Output:
        array = [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10],
    ]

"""
# Cách 1: Khởi tạo ma trận zero
# def add_matrices(mat1, mat2):
#     # check 2 matrix could be added to each other
#     if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
#         return 0
#
#     # Initial zero matrix for sum
#     result = []
#     for i in range(len(mat1)):
#         zero_row = [0] * len(mat1[0])  # [0,0,0,0]
#         result.append(zero_row) #inplace function
#
#     # add two matrix with each other
#     for i in range(len(mat1)):
#         for j in range(len(mat1[0])):
#             result[i][j] = mat1[i][j] + mat2[i][j]
#     return result

# Cách 2 Không cần khởi tạo ma trận zero for sum

# def add_matrices(mat1, mat2):
#     # check 2 matrix could be added to each other
#     if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
#         return 0
#
#     # add two matrix with each other
#     for i in range(len(mat1)):
#         for j in range(len(mat1[0])):
#             mat1[i][j] = mat1[i][j] + mat2[i][j]
#     return mat1
# mat1 = [
#     [1, 2, 3, 4],
#     [4, 5, 6, 5],
#     [7, 8, 9, 6],
# ] #nested list
#
# mat2 = [
#     [9, 8, 7, 1],
#     [6, 5, 4, 2],
#     [3, 2, 1, 3],
# ]
# sum_matrix = add_matrices(mat1, mat2)
# print(sum_matrix)

"""
    Yêu cầu người dùng nhập vào 1 số nguyên dương
    Kiểm tra xem số đó có phải là 1 số may mắn hay không

    Số may mắn là số được định nghĩa theo quá trình sau: bắt đầu với số nguyên dương x
    và tính tổng bình phương y các chữ số của x, sau đó tiếp tục tính tổng bình phương
    các chữ số của y. Quá trình này lặp đi lặp lại cho đến khi thu được kết quả là 1
    thì dừng (tổng bình phương các chữ số của số 1 chính là 1) hoặc quá trình sẽ kéo dài vô tận.
    Số mà quá trình tính này kết thúc bằng 1 gọi là số may mắn.
    Số có quá trình tính kéo dài vô tận là số không may mắn hay còn gọi là số đen đủi
    Ví dụ: 19 là số may mắn vì
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1 (End)

    Some happy numbers are: 1, 7, 13, 19, 23, 28, 44, 49, 68, 79, 129, 133, 139, 167, 188,
    226, 236, 239, 338, 356, 367, 368, 379, 446, 469, 478, 556, 566, 888, 899
"""

# number = input("Enter the number: ")
# sum_squared_digits = 0
# seen_numbers = []
# for digit in number:
#     sum_squared_digits += int(digit)**2
# seen_numbers.append(sum_squared_digits)
# print(seen_numbers)

number = "110823"
seen_numbers = []
while int(number) != 1 and number not in seen_numbers:
    seen_numbers.append(number)
    print(number)
    sum_squared_digits = 0
    for digit in number:
        sum_squared_digits += int(digit)**2
    number = str(sum_squared_digits)


print("---------")
print(number)
if(int(number) == 1):
    print('happy number')
else:
    print('not happy number')