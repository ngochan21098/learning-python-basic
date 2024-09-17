#5. In ra màn hình 2/3 theo chiều dài của chuỗi. (Làm tròn xuống VD: len = 10, Lấy từ 1 => 6 (10*2/3 = 6.66 = 6)
#Input: "HelloWorld"
#Output: "HelloW"

import math 
input_text = input('Please input free text: ')
count = math.trunc(len(input_text) *2/3)
new_text = input_text[:count]
print(new_text)