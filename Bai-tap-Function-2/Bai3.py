def print_rec(m, n):
  """
  In ra hình chữ nhật có chiều dài m và chiều rộng n.
    m: Chiều dài của hình chữ nhật.
    n: Chiều rộng của hình chữ nhật.
  """
  if m <= n:
        print('Fail')
  else:   
    for i in range(n):
        for j in range(m):
         print('*', end='')
        print() 

print_rec(2, 4)

