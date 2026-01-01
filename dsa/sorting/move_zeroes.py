'''
nums=[1,0,2,4,3,0,0,3,5,1]
def move(nums):
 write=0
 for i in range(len(nums)):
  if nums[i]!=0:
   nums[write]=nums[i]
   write+=1
 for i in range(write,len(nums)):
  nums[i]=0
 return nums
print(move(nums))
'''
nums=[1,0,2,4,3,0,0,3,5,1]
freq=[] # 1 2 4 3 3 5 1
n=len(nums)
for i in nums:
  if i!=0:
    freq.append(i)
for i in range(0,len(freq)):
  nums[i]=freq[i]
f=len(freq)
for i in range(f,n):
  nums[i]=0
print(nums)
