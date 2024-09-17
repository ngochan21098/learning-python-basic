#6. Thay thế tất cả các ký tự giống với ký tự đầu tiên thành * ngoại trừ ký tự đầu tiên.
#Input: "han de thuong, hien hau"
#Output: "han de t*uong, *ien *au"

input_text = input('Please input free text: ')
new_text = input_text[0] + input_text[1:].replace(input_text[0],'*')
    
print(new_text)