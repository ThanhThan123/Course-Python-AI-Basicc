# String
    # String là tập hợp các chuỗi ký tự trong nháy đơn, đôi, 3 nháy đơn hoặc 3 nháy kép
    # Biến đổi kiểu dữ liệu khác sang String
        # a = str(a)
    # Thay đổi kiểu dữ liệu trong String (bất biến)
        # string = "ABCDEF"
        # new_string = "P" + string[1:] # kết hợp với slice
        # print(new_string) #PABCDEF
    # Cộng 2 String
        # print(stringa+stringb)
        # print("today""so sad")
    # Nhân
        # a = "today" * 10
    # Độ dài
        # len(a)
    # Thay thế old_text bằng new_text (dùng nhiều)
        # string = "long, longer, longest"
        # string = string.replace("long","high")
        # print(string) # old higher highest
    # Chuyển đổi in hoa / in thươn trong String
        #lower: Viết thường tất cả ký tự (dùng nhiều)
        #upper: Viết hoa tất cả ký tự
        #capitalize: Ký tự đầu tiên viết hoa còn lại viết thường
        #title: Ký tự đầu tiên của mỗi từ viết hoa. Còn lại viêết thường
    # Substring bên trong String: Trả về true khi substring_name nằm trong string_name
        # string = "Today is bad"
        # substring = "Today"
        # print(substring in string) # True # in Toán tử thành viên
    # 1 vài ký tự đặc biệt
        # \' : Dấu nháy đơn
        # \" : Dấu nháy kép
        # \\ : Dấu gạch chéo ngược
        # \n : Dấu xuống dòng
        # \t : Dấu tab
            # text = 'Than\'s house in Long An '
            # print(text)
    # Tìm vị trí của Substring bên trong string (find):
        # Trả về ký tự và vị trí đầu tiên nằm trong string_name
        # string = "Today is a beautiful day"
        # substring = "beautiful"
        # substring1 = "Today"
        # print(string.find(substring)) # 11
        # print(string.find(substring))
    # Duyệt qua các phần tử của String
        # string = "Today is a beautiful day"
        # for char in string:
        #   print(char)
    #Loại bỏ khoảng trắng trong chuỗi String, và giảm số ký tự ( sử dụng khi lấy dữ liệu trên mạng)
        # strip : Xoá ký tự trắng ở đầu và ở cuối
            # string = "          Today is a beautiful day        "
                # print(string, len(string))
                # text = string.strip()
                # print( text, len(text))
        # lstrip : Xoá khoảng trắng bên trái
        # rstrip: Xoá khoảng trắng bên phải
    # Định dạng String (dùng nhiều trong machine và deep learning)
        # format(value)
            # 1 Biến
                # day = "Monday"
                # string = "Today is {}".format(day)
                # print(string) # Today is Monday
            # Nhiều Biến
                # string = "{0} feel Today is {1} because he\'s {2}".format("Than","lucky","remember" )
                # print(string) # Today is Monday
    # Tách String:
        # split: Tách chuỗi chúng ta thành những mảng con
            # string = "Today is a beautiful day"
            # print(string.split())
        # split(".") :  Tách chuỗi tại dấu chấm thành những mãng con
            # text = """
            # I live in a house near the mountains. I have two brothers and one sister, and I was born last.
            # My father teaches mathematics,and my mother is a nurse at a big hospital.
            # My brothers are very smart and work hard in school. My sister is a nervous
            # girl, but she is very kind. My grandmother also lives with us.
            # She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
            # My family is very important to me. We do lots of things together.
            # My brothers and I like to go on long walks in the mountains.
            # My sister likes to cook with my grandmother. On the weekends we all play board games together.
            #  We laugh and always have a good time. I love my family very much.
            # """
            # print(text.split("."))
    # Nối String
        # delimiter.join(interable): Phải chỉ ra phải nối bằng gì trước
            # Bằng dấu phẩy
                # strings = ["blue", "red", "green", "yellow"]
                # result = ", ".join(strings)
                # print(result) # blue, red, green, yellow
            # Bằng khoảng trắng, ...
                # strings = ["blue", "red", "green", "yellow"]
                # result = " ".join(strings)
                # print(result) # blue, red, green, yellow
    # Tổng kết tất cả hàm trong String
        #replace(old_text,new_text)
        #lower: Viết thường tất cả ký tự trong string
        # upper: Viết hoa tất cả ký tự trong string
        # capitalize: Viết hoa duy nhất ký tu đầu của String
        # title: Viết hoa  ký tự đầu của mỗi từ trong String
        # find(substring): Tìm vị trí của substring trong String
        # strip(): Loại bỏ toàn bộ khoảng trắng ở đầu và ở cuối ở string
        # split(delimiter): Tách String bởi Delimiter
        # join(string) : Nối các String laij với nhau

"""
     Viết 1 hàm nhận 2 tham số đầu vào
    1. 1 Chuỗi ký tự bất kỳ
    2. 1 Chuỗi ký tự tự nhiên
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về kết quả
"""

# string = "Today is a beautiful day"
# k = 5
#
# def remove_char(string,k):
#     result = string[:k] + string[k+1:]
#     return result
#
# print(remove_char(string, k))

"""
    Viết 1 hàm nhận tham số đầu vào là 1 chuỗi bất kỳ,
    đếm và trả về số lượng nguyên âm trong chuỗi đó
"""
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# def count_vowels(string):
#     count = 0
#     for char in string.lower() :
#        if char in vowels:
#            count += 1
#     return count
#
#
# text = "Today is a beautiful day"
#
# print(count_vowels(text))



"""
    Yêu cầu người dùng nhập vào 2 chuỗi ký tự bất kỳ. 
    Kiểm tra xem chúng có phải anagrams (phép đảo chữ)
    của nhau không?
    Định nghĩa anagram: 2 từ là anagram của nhau nếu ta có thể 
    thu được từ này bằng cách đổi vị trí các ký tự của từ kia
    Các ví dụ:
    "New York Times" và "monkeys write"
    "coronavirus" và "carnivorous"
    "a gentleman" = "elegant man"
    "silent" = "listen"
"""
str1 = "New York Times"
str2 = "monkeys write"

def are_anagrams(str1, str2):
   str1 = str1.replace(" ","").lower()
   print(str1)
   str2 = str2.replace(" ","").lower()
   print(str2)
   return sorted(str1) == sorted(str2)

print(are_anagrams(str1, str2))