from collections import deque
n,k=map(int,input().split())

deq=deque([i for i in range(1,n+1)])
cnt=[]
while len(deq)!=0 :
    for _ in range(k-1):
        deq.append(deq.popleft())
    cnt.append(str(deq.popleft()))



print("<"+", ".join(cnt)+">")