'''
Bài 5: Viết hàm nhận vào n (n là cạnh của tam giác cân) => In ra hình tam giác cân như Ví dụ.
Output:
____*
___***
__*****
-*******
*********
'''

def func5(n):
  """
  In ra hình tam giác cân có cạnh n

  Args:
    n: Độ dài cạnh của tam giác cân

  Returns:
    None
  """

  for i in range(n):
    # In khoảng trắng
    for j in range(n-i-1):
      print(" ", end="")
    # In dấu sao
    for j in range(2*i+1):
      print("*", end="")
    print()

# Gọi hàm với n = 5
func5(8)

