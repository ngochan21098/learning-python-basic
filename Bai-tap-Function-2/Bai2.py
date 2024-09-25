'''Bài 2: Viết hàm nhận vào 1 mảng => In ra màn hình số dấu "*" tương ứng của mỗi Item.
Input:
mang = func1(5) => VD: [5, 4, 1, 4, 3]
func2(mang)
Output:
*****
****
*
****
***'''

def print_mang(num):
    x = 0
    arr = []
    while x < num:
         arr.append(int(input(f'Nhap so thu {x+1}:')))
         x += 1   
    return arr

def convert_star(array):
     item_convert = ""
     for item in array: 
        item_convert = "*"*item
        print(item_convert) 


mang = print_mang(3) 
convert_star(mang) 
     