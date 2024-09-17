'''3. Kết hợp bài 1, 2 đếm xem có bao số nguyên tố trong mảng được nhập vào.
Input: mang = func1(5) => VD: [2, 3, 4, 5, 6]
Output: 3'''

input_text = input('Please input free text: ')
input_arr_convert = [int(x) for x in input_text.split(',')]
snt_count = 0
def check_snt (num): 
    count = 0
    if num < 2: 
        return False
    elif num == 2: 
        return True
    else: 
        for x in range(2,num+1):
            if num % x == 0:
                count += 1
    return False if count > 1 else True
    return 

for item in input_arr_convert:
    if check_snt(item) == True:
        snt_count += 1 

print(snt_count)
    
