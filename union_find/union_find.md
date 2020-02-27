# Union-Find 
- Kruskal 알고리즘에서 간선의 양 끝점을 비교할 때 cycle이 안 생기면, 연결을 어떻게 할 지를 union-find에 따라 판단
- 간선끼리 이미 연결된 노드들을 부분집합으로 관리
- 간선이 연결된 특정 두 노드가 root node가 동일하다면, find logic에 의해서 cycle이 있다. root node가 다르면 cycle이 없다.
- 연결을 union logic에 따라서 tree 구조체와 tree 구조체를 같이 연결하여 하나의 tree를 만드는 방식을 택한다.

## Union
- 두 개별 집합을 하나의 집합으로 합침 (두 트리를 하나의 트리로 만듦)

## Find
- 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 같은 graph에 속하는지 판단하기 위해 root node 확인

## 주의점
- union 순서에 따라서 성능의 차이가 크다. 최악의 경우 linked list와 같은 형태의 O(n)가 될 수 있기 때문에
- 해당 문제를 해결하기 위해, union-by-rank, path compression 기법을 사용, 결과적으로 상수값에 가까운 복잡도에 도달

## union-by-rank 
- 각 트리에 대해 높이(rank)를 기억해두고,
- union을 할 때, 두 트리의 높이가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙인다.
- 둘의 높이가 동일하다면, 아무 트리나 높이를 1 증가시키고, 다른 쪽을 해당 트리에 붙인다.
    - 높이가 h인 트리가 만들어지기 위해, h-1인 트리 두 개가 합쳐져야 한다.
    - 높이가 h-1인 트리에 n개의 원소가 있다면, h인 트리에는 최소 2n개가 필요
    - union-by-rank 기법을 이용함으로써, O(n)에서 O(logN)으로 낮출 수 있음

## path compression
- 특정 노드에서 find로 root node를 찾는 것
- 해당 노드의 부모를 root로 설정함으로써, 다음 번에 해당 노드의 root를 한 번에 찾을 수 있음
