from collections import deque

def solution_easy(bridge_length, weight, truck_weights):
    answer = 0
    q= [0] * bridge_length
    truck_weights = deque(truck_weights)
    while q:
        answer += 1
        q.pop(0)
        if len(truck_weights) != 0:
            if truck_weights[0] + sum(q) <= weight:
                q.append(truck_weights.popleft())
            else:
                q.append(0)
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque() # 다리를 건너는 트럭 queue
    cnt = deque() # 다리 위에서 몇 초나 있었는지 확인하는 queue - dependency가 q와 동일함
    truck_weights = deque(truck_weights) # 대기트럭 queue
    while True:
        if len(truck_weights) == 0 and len(q) == 0: # 대기트럭과 다리 위 트럭 전부 없다면 break
            break
        for i in range(len(q)): 
            cnt[i] += 1
        if len(q) != 0:
            if cnt[0] == bridge_length:
                q.popleft()
                cnt.popleft()
        if len(truck_weights) != 0:
            if truck_weights[0] + sum(q) <= weight:
                q.append(truck_weights.popleft())
                cnt.append(0)
        answer += 1
    return answer

a= 100
b= 100
c= [10]

print(solution(a,b,c))