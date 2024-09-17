#4. Dừng việc in ra màn hình nếu không phải là số
#Input: [1, 2, 3, 4, "5", 6, 7, 8, 9]
#Output: 1 2 3 4

num_list =   [1, 2, 3, 4, "5", 6, 7, 8, 9]

for item in num_list: 
    if isinstance(item, int):
       print(item)
    else:
        break 
    

        
