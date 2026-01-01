nums=list(map(int,input("Enter the array elements:").split()))
n=len(nums)
exp=n*(n+1)//2
summ=sum(nums)
missing=exp-summ