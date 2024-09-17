#5. In ra màn hình tất cả giá trị trong mảng dưới
#Input: [1, 2, 3, [4, 5, 6], 7, ["han", "xinh", "dep"], 9]
#Output: 1 2 3 4 5 6 7 "han" "xinh" "dep" 9

mix_list =   [1, 2, 3, [4, 5, 6], 7, ["han", "xinh", "dep"], 9]

for item in mix_list: 
    if isinstance(item, list):
      for item2 in item:
            print(item2)
    else:
        print(item)