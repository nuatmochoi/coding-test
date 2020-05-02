# Greedy 

- 여러 경우 중 하나를 결정해야할 때마다, **매순간 최적이라고 생각되는 경우를 선택**하는 방식으로 진행하여, 최종값을 구하는 방식

- 대표적인 문제로 동전문제, 부분 배낭 문제(knapsack problem)이 있다.
    - 동전이 여러 개(50,10,5,1원) 있을 때 지금 각 동전의 시점(현재 단계)에서, 전체 동전의 조합 or 다음 단계의 동작을 고려하지 않고, 그 순간에 가치가 가장 값이 높은 동전만 생각하는 것. 

- Greedy Algorithm의 한계 
    - 최적의 해에 가까운 값만 구하는 것. 반드시 최적의 해를 구하는 것은 아니다.
    - 아래 그림은 트리에서 각 분기마다 최대값을 찾아가는 문제인데, greedy algorithm을 따르면 마지막에 12에 도달하지만, 실제 최대값은 99임을 알 수 있다.
    ![탐욕알고리즘의 한계](https://media.vlpt.us/post-images/cyranocoding/c8b8eff0-b228-11e9-89af-8fc0a61dbc3e/1CeFxqV8wFf2NaQm1hqYGMQ.png)

- Greedy 는 **탐욕스러운 선택조건**과 **최적 부분 구조 조건** 이 성립되어야 쓸 수 있다.
    - 탐욕스러운 선택조건 : 앞의 선택이 이후의 선택에 영향을 주지 않는다.
    - 최적 부분 구조 조건 : 문제에 대한 최종 해결 방법이 부분 문제에 대해서도 최적 문제 해결 방법이라는 조건

