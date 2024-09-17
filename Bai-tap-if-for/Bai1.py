#1. Đếm có bao nhiêu chữ h trong chuỗi
#Input: "han xinh dep"
#Output: 2

input_text = input('Please input free text: ')
'''
Note cach khac: 
count = input_text.count('h')
print(count)'''

count = 0
for i in range(len(input_text)):
    if input_text[i] == 'h':
        count += 1
print(count) 