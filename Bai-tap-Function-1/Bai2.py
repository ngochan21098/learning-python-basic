'''2. Viết hàm kiểm tra xem 1 số có phải là số nguyên tố hay không (SNT là số chỉ chia hết cho 1 và chính nó).
Input: print(func2(5))
Output: True'''

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

print(check_snt(2))
            
