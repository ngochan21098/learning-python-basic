'''Bài 4: Viết hàm nhận vào n => In ra hình tam giác như Ví dụ.

Input: func4(4)
Output:
****
***
**
*
'''

def print_tri(m): 
    x = m
    arr = []
    while x<=m and x>0: 
        arr.append(x)
        x -= 1
    for i in arr:
        print("*" * i,end ='')
        print()


print_tri(6) 