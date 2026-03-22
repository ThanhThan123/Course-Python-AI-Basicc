# Giải các bài tập liên quan đến Dictionary

"""
    Bài 1: Cho list bao gồm các số bất kì
    Đếm xem số lần xuất hiện của số đó trong list
"""

# numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]

# Method 1
    # for digit in numbers:
    #     print(digit, "appear" ,numbers.count(digit))

# Method 2
    # def count_frequency(numbers):
    #     count = {}
    #     for num in numbers:
    #         if num in count.keys():
    #             count[num] += 1
    #         else:
    #             count[num] = 1
    #
    #     for key, value in count.items():
    #         print(key, "appear", value, "times")
    #
    # count_frequency(numbers)

"""
    Viết chương trình kết hợp 2 dictionary vào làm 1.
    Nếu key xuất hiện ở cả 2 dictionary thì cộng 2 value
    tương ứng lại
"""
# dict1 = {'a': 100, 'b': 200, 'c': 300}
# dict2 = {'a': 300, 'b': 200, 'd': 400}
# for key, value in dict2.items():
#     if key in dict1.keys():
#         dict1[key] += value
#     else:
#         dict1[key] = value
#
# print(dict1)

"""
    Viết 1 hàm với tham số đầu vào là 1 chuỗi ký tự
    Hàm trả về 1 Dictionary với key là các ký tự xuất
    hiện trong chuỗi ký tự đó, và value là số lần ký 
    tự đó xuất hiện 
"""


def count_occurrences(string):
    char_count = {}
    for char in string.lower():
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


text = """
I live in a house near the mountains. I have two brothers and one sister, and I was born last.
My father teaches mathematics,and my mother is a nurse at a big hospital.
My brothers are very smart and work hard in school. My sister is a nervous
girl, but she is very kind. My grandmother also lives with us.
She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
My family is very important to me. We do lots of things together.
My brothers and I like to go on long walks in the mountains.
My sister likes to cook with my grandmother. On the weekends we all play board games together.
 We laugh and always have a good time. I love my family very much.
"""

print(count_occurrences(str(text)))




