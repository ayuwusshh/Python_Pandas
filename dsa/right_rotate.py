def krotate(nums,k):
  n=len(nums) 
  nums[:]=nums[n-k:n]+nums[0:n-k]
  return nums
nums=[5,-2,3,9,0,6,10,7]
print(nums)
print(krotate(nums,4))