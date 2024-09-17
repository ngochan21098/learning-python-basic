#2. In ra số lượng chẵn, lẽ trong mảng bên dưới.
#Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Output: (4, 5)

input_text = input('Please input free text: ')
input_arr_convert = [int(x) for x in input_text.split(',')]
count_even = 0
for item in input_arr_convert:
    if item%2 == 0: 
        count_even += 1
print(count_even, len(input_arr_convert)-count_even) 