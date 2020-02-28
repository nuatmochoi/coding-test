def find(x):
    if x == parent[x]: # 부모를 찾아서 
        return x
    else:
        p = find(parent[x])
        parent[x] = p # 자기자신을 부모로 
        return parent[x]

def union(x, y): # 찾은 부모끼리 연결
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(int(input())):
    parent = dict()
    number = dict()

    for _ in range(int(input())):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(x)])