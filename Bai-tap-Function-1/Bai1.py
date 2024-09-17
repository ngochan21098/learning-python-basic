'''1. Viết hàm nhập vào n phần tử của mảng và trả về mảng đó.
Input: mang = func1(5)
Output: print(mang) => VD: [1, 2, 3, 4, 5]'''

def return_item(num):
   arr = []
   for x in range(1,num+1):
     arr.append(x)
   return arr

mang = return_item(5)
print(mang)

    