#3. In ra màn hình những chữ số chia hết cho 2
#Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Output: 2 4 6 8

input_text = input('Please input free text: ')
input_arr_convert = [int(x) for x in input_text.split(',')]
for item in input_arr_convert:
    if item % 2 == 0: 
        print(item)

