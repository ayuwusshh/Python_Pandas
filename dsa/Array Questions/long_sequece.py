nums=list(map(int,input('Emter the numbers: ').split()))
count=1
nums.sort() # 1 2 3 4 100 200
mx=1
if len(nums)==0:
  print('0')
if len(nums)==1:
  print('1')
for i in range(0,len(nums)-1):
    if nums[i+1]-nums[i]==0:
        continue
    if nums[i+1]-nums[i]==1:
      count+=1
      mx=max(mx,count)
    else:
        count=1
print(mx)