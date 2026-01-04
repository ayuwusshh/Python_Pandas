row,col=map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(row)]
result=[[0]*row for _ in range(col)]
for i in range(0,row):
  for j in range(0,col):
    result[j][i]=nums[i][j]
print(result)
