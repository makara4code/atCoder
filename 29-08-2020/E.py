import math
 
n=int(input())
a=list(map(int,input().split()))
 
dp=[0 for _ in range(1000001)]
 
for d in a:
  dp[d]+=1
  
ch1=0
for i in  range(2,1000001):
  ch=0
  x=i
  while x<=1000000:
    ch+=dp[x]
    x+=i
  if ch>1:
    ch1+=1
    
if ch1==0:
  print('pairwise coprime')
  
else:
  g=a[0]
  for h in range(1,n):
    g=math.gcd(g,a[h])
    
  if g==1:
    print('setwise coprime')
    
  else:
    print('not coprime')