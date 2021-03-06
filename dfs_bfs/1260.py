"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""

from queue import Queue


def bfs(graph, start_node):
    visit = {}
    q= Queue()

    q.put(start_node)

    while q.qsize()>0:
        node = q.get()
        if node not in visit:
            visit[node]=True
            for nextNode in graph[node]:
                q.put(nextNode)
    return list(visit.keys())

def dfs(graph, start_node):
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node =stack.pop()
        if node not in visit:
            visit[node]=True
            stack.extend(graph[node])
    return list(visit.keys())

if __name__ == '__main__':
    graph = {}
    node, edge, start= map(int, input().split())
    for i in range(edge):
        n1,n2=map(int,input().split())
        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)

    print(dfs(graph, start))
    print(bfs(graph, start))
