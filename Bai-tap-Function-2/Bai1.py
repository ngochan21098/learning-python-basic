'''Bài 1: Viết hàm nhập vào 1 mảng số nguyên (Nếu nhập ký tự thì bắt nhập lại đến khi nào nhập đúng thì thôi) => trả về lại mảng có giá trị nguyên.
Input: mang = func1(5)
Output: print(mang) =>  [5, 4, 1, 4, 3]
Gợi ý: Sử dụng while để check (https://www.w3schools.com/python/python_while_loops.asp)'''

def print_mang(num):
    x = 0
    arr = []
    while x < num:
         arr.append(int(input(f'Nhap so thu {x+1}:')))
         x += 1
        
    return arr 

mang = print_mang(5)
print(mang) 

