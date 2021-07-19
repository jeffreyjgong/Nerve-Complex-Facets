n = int(input("Please enter n (the number of vertices on S1): \n"))
print(f'You entered {n}')
k = int(input("Please enter k (the length of the arc): \n"))
print(f'You entered {k}')
print(f'Here is the facet matrix for {n} vertices on S1 with an arc length of {k}')

Matrix = [[0 for x in range(k+1)] for y in range(n)]
for x in range(0, n):
  for y in range(0, k+1):
    Matrix[x][y]= (x+y)%n
print(Matrix)
