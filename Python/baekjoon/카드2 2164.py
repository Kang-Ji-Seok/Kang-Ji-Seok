from collections import deque
n=int(input())
deq=deque([i for i in range(1,n+1)])

while True :
    if len(deq)==1 :
        break
    deq.popleft()

    deq.rotate(-1)


print(deq[0])