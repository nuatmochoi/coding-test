import pytest
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while True:
        if len(heap) == 1:
            break
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        if heap[0] >= K:
            return answer
    return -1

@pytest.mark.parametrize("scoville, K, expected", [
    ([1, 2, 3, 9, 10, 12], 7, 2),
])
def test_simple(scoville, K, expected):
    assert solution(scoville,K) == expected