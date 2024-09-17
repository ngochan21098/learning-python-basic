'''5. Viết hàm nhận vào a, b (a < b) => trả về mảng chứa tất cả số chẵn trong [a, b]
Input: mang = func5(1, 10)
Output: [2, 4, 6, 8, 10]'''

def return_even (a,b):
    arr = []
    if a >= b: 
        print('Nhap so khong hop le')
    else: 
        for x in range(a,b+1):
            if x%2 == 0: 
                arr.append(x)
    return arr

mang = return_even(1,10)
print(mang) 