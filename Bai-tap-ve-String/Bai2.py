#2. Chèn "HAN XINH DEP" vào sau index = 3 và in ra màn hình
#Input: "01234567"
#Output: "0123HAN XINH DEP4567"

input_text = input('Please input free text: ') 
new_text = f'{input_text[:4]}HAN XINH DEP{input_text[4:]}'
print(new_text)