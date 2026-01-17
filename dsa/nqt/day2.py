#10
# n=int(input())
# ans=0
# while n>=10: #987
#   temp=n    #987
#   summ=0    #0
#   while(temp>0):#987  98
#     digit=temp%10  #7 8 9
#     summ+=digit #7 15 24
#     temp//=10 #98 9 0
#   n=summ  #7 15 24
#   ans=summ  # 7 15 24
# print(ans)

#11
# import math
# n,m=map(int,input().split())
# print(math.gcd(n,m))

#12
# s=input()
# arr=[]
# count=0
# for ch in s:
#   arr.append(ch)
# for i in range(len(arr)):
#   for j in range(2,i):
#     if i%j!=0:
#       count+=1
# print(count)

#13
# n=int(input())  #16
# ok=False
# while n>0:  #  16
#   if n==1:
#     ok=True
#     break
#   if n%2==0:
#     n//=2  #
#     if n==1:  #
#       ok=True
#       break
#   else:
#     break
# if ok:
#   print('YES')
# else:
#   print('NO')

#14
arr=list(map(int,input().split()))
n=len(arr)+1
add1=n*(n+1)//2
add2=sum(arr)
print(add1-add2)