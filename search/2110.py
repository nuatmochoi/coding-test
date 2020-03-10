
# log(10억)* 집의 개수200000 => log(10억)이 30정도 이므로 600만의 계산 안에 해결 가능

n, c = list(map(int, input().split()))

arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

start = arr[1] - arr[0]
end = arr[-1] - arr[0]
result = 0

while(start <= end):
    mid = (start + end) // 2 # Gap
    value = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)