#                       0  1 2  
nums=[[5,20,3],       # 5 20 3  0
      [7,-10,9],      #  -10 9  1
      [1,-52,6]]      #      6  2
row=len(nums)
col=len(nums[0])
summ=0
for i in range(0,row):
  for j in range(0,col):
     summ+=nums[i][j]
     print(nums[i][j], end=" ")
  print('')
print(summ)