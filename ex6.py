# Các kiểu dữ liệu còn lại
# Dictionary : là tập hợp các phần tử không có thứ tự,
# được lưu trữ dưới dạng các cặp khoá (key) và (value)
# Cách khai báo các cặp key-value ex: data={"name":"Than"}
    # Kb  1 dic with list vs tuple(uc), tuple voi lists (uc),
    # Khai báo 1 dictionary với các đối số key, data=dict(name="Than")
# Tính chất:
    # Key phải là duy nhất, Nếu value xuất hiện nhiều lần nó sẽ xuất hiện value ở cuối
    # Key của Dic phải là bất biến
    # Value trong dic không có giới hạn gì

# Phân biệt đối tượng (dữ liệu và cấu trúc dữ liệu) bất biến và khả biến
    #Khả biến: List, Dictionary, Set
    #Bất biến: Number, String, Bool, Tuple
# Truy cập vào các phần tử trong Dictionary
    #dictionary_name[key_name]
    #print(data["age"])
    # Sử dụng hàm get: khi bị lỗi sẽ trả về None
    # print(data.get("age"))
# Thêm hoặc cập nhật phần tử trong Dic
    # Dictionary_name[key_name] = value
    # data[age] = 30
# Xoá phần tử khỏi Dic
    # pop
        # dictionary_name.pop(key_name)
        # removed_value = data.pop("age")
    # del
        # del data["age"]
    # clear : Xoá tất cả phần tử
        # dictionary_name.clear()
        # data.clear()
# Duyệt qua tất cả key, value, item trong dictionary
    #data.keys()
    #data.values()
    #data.items()
        # a = {"day": "saturday", "month":"August"}
        # for key, value in a.items():
        #     print(key,value)
# Tính số phần tử trong Dictionary
    #len(dictionar_name)
    #print(len(data))
# Tổng kết các hàm tích hợp sẵn trong Dic
    # get, pop, clear, keys, values, items

# Kiểu dữ liệu Tuple
    # Tuple là tập hợp các phần tử có thứ tự
        # Có rất nhiều đặc điểm giống với List
        # Giống : Có thứ tự, Chỉ số truy cập được, Phần tử: chứa nhiều loại giá trị
        # Khác : Có tính Bất biến, Không thể thêm sửa xoá sau khi được định nghĩa
    # Khai báo Tuple
        # data = ()
        # data = tuple([1,2,3])
    # Khai báo Tuple packing (Trao đổi giá trị các biến trong 1 dòng, gán giá trị cho nhiều biến)
        # data = "red", "green"
    # Tuple unpacking
        # ("a", "a","a","a") = data
        # a, b, c, d = data
        # data = 1, 2, 3, 4
        # (a, b, c, d) = data
        # print(a)
        # print(b)
        # print(c)
        # print(d)
    # Tuple là bất biến nhưng phần tử của nó là khả biến
        # data = ("red","green",["light","green"])
        # data[2][0] = "black"
        # print(data)
    # Xoá tuple chỉ có thể xoá cả
        # del data
    # Tổng hợp các hàm tích hợp có sẵn của Tuple
        # index, sorted, count(đếm), min, max, sum
            # index: trả về vị trí của phần tử đầu tiên với giá trị cụ thể trong tuple
                # a = 1, 2, 3, 4, 5
                # print(a.index(1))

# Set là tập hợp các phần tử không trùng nhau và không có thứ tự (thường được dùng để loại bỏ các phần
#  tử trùng lặp trong dictionary, tuple
    # Không có thứ tự : Không được lưu trữ theo 1 thứ tự nào
    # Không trùng lặp: Không tồn tại các giá trị trùng lặp trong set
    # Không có chỉ số: Không thể truy cập các phần tử của set thông qua chir so
    # Khả biến

    # Khởi tại set
        # data = {"red", 5, True}
            # Nếu có 2 giá trị trùng lặp nó sẽ loại bỏ 1 g trị
            # Set là khả biến nhưng nó không thể chứa phần tử khả biến ở biên trong gồm : [].
        # data = set("Webnesday")
        # data = set([1, 2, 3, 4, 5])
    # Thêm phần tử
        # set_name.add(item)
            #data.add(10)
        # set_name.update(set1,set2,..)
        # data.update({1,2})
    # Xoá phần tử
        # set_name.remove
        # set_name.discard()
        # set_name.pop() Xoá lại phần tử và trả về name của phần tử đã xoá
        # set_name.clear()
    # Tổng hợp các hàm tích hợp trong Set
        # add, update, remove, discard, pop, clear
    # Các phép toán tập hợp trong Set (
        # Union: Hợp giữa hai phần tử
            # print(set1 | set2)
            #print(set1.union(set2))
        # Intersection: Các phần tử chung giữa hai phần tử (Phép giao)
            # print(set1 & set2)
            # print(set1.intersection(set2))
        # Different: Phần tử chỉ thuộc về a hoặc chỉ  thuộc về b
            # print(set1 - set2)
            # print(set1.difference(set2))
        # Symmetric Difference: Phần tử chỉ thuộc về a hoặc chỉ thuộc về b (Phép hiệu đối xứng)
            # print(set1 ^ set2)
            # print(set1.symmetric_difference(set2))

"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
        36 = 2 x 2 x 3 x 3
"""

n = 100
def get_str(n):
    i = 2
    while i * i < n: #Kiểm tra đến căn bậc 2 của n
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1
    if n > 1:
        print(n)

print(get_str(n))







