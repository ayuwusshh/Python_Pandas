prices=list(map(int,input("Enter your elements: ").split()))
# 7 2 1 5 6 4 8
min_price=prices[0]
max_profit=0
for i in range(0,len(prices)):
  if(prices[i]<min_price):
    min_price=prices[i]
  else:
    max_profit=max(max_profit,prices[i]-min_price)
  
print(max_profit)