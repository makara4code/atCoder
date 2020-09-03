N = int(input())
A = list(map(int,input().split()))
sumA = sum(A)%(1000000007)
sumA2 = (sumA * sumA)%(1000000007)
square = 0
for i in range(N):
    square +=  ( A[i]**2 ) % (1000000007)
    square = square % (1000000007)
buf = sumA2 - square
if buf < 0:
  buf = buf + (1000000007)
res = ( buf * ((1000000007+1)//2)) % 1000000007
print(int(res))