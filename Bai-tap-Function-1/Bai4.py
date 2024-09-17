'''4. Viết hàm nhận vào 1 mảng => trả lại mảng mới không trùng giá trị
Input: mang = func4([1, 2, 3, 4, 4, 4, 5, 5])
Output: print(mang) => [1, 2, 3, 4, 5]'''
def check_trung_mang (arr):
    arr_new = []
    for item in arr: 
        if item in arr_new:
            continue
        else: 
            arr_new.append(item)
    return arr_new 

mang = check_trung_mang([1,2,3,4,4,4,5,5])
print(mang)