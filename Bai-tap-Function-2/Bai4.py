'''Bài 4: Viết hàm nhận vào n => In ra hình tam giác như Ví dụ.
Output:
****
***
**
*
'''

def print_tri(m): 
    for i in range(m):
        print('*' * (m-i), end='')
        print()

print_tri(6) 

