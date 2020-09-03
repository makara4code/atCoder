from collections import deque
 
N, M = map(int, input().split())
rinsetu = [set() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, (input().split()))
    rinsetu[a].add(b)
    rinsetu[b].add(a)
 
grp = 0
color = ["white"] * (N + 1)
color_2 = ["white"] * (N + 1)
color[0] = "black"
for i in range(1, N + 1):
    count=1
    if color[i] == "white":
        d = deque()
        d.append(i)
        a = set()
        a.add(i)
        while (d):
            k = d.popleft()
            color[k] = "black"
            color_2[k]="black"
            for j in rinsetu[k]:
                if color[j] == "white" and color_2[j]=="white":
                    color_2[j]="black"
                    d.append(j)
                    count+=1
        grp=max(grp,count)
print(grp)