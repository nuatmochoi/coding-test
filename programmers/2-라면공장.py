import pytest
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    heap = []
    while stock < k:
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                heapq.heappush(heap, (-supplies[i]))
                idx += 1
            else:
                break
        stock += (-heapq.heappop(heap))
        answer += 1
    return answer

@pytest.mark.parametrize("stock, dates, supplies, k, expected", [
    (4, [4, 10, 15], [20, 5, 10], 30, 2),
])
def test_simple(stock, dates, supplies, k, expected):
    assert solution(stock, dates, supplies, k) == expected