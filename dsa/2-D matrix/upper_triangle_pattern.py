nums=[[1,2,3],
      [4,5,6],
      [7,8,9]]
row=len(nums)
for i in range(row):
  for j in range(row):
    if j>=i:
      print(nums[i][j], end=" ")
    else:
      print("*",end=" ")
  print()