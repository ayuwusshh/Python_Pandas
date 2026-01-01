nums=list(map(int,input("Enter your elements: ").split()))
count=0
mx=0
for i in nums:
  if i==1:
    count+=1
    mx=max(mx,count)
  else:
    count=0
print(mx)