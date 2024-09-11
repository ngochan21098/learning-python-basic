#3. In hoa tất cả ngoại trừ chữ đầu tiên
#Input: "hello World"
#Output: "hELLO WORLD"

input_text = input('Please input free text: ').strip()
new_text = input_text[0].lower()+input_text[1:].upper()
print(new_text)