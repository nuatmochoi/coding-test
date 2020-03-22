import sys

for _ in range(int(input())):
    result = sys.stdin.readline().rstrip()
    cnt = 0
    score = 0
    for idx, ele in enumerate(result):
        if ele == 'O':
            cnt+=1
            score += cnt
        else:
            cnt = 0 

    print(score)