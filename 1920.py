import sys

def binary_search(li, target):
    count=0
    start=0
    end=len(li)-1
    for i in range(len(li)):
        if li[i]==target:
            count+=1
    while start<=end:
        mid=(start+end)//2
        if target==li[mid]:
            return 1 # True
        elif target>li[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0 # False

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort() # binary search needs sorted list
M = int(sys.stdin.readline().rstrip())
M_li = list(map(int,sys.stdin.readline().rstrip().split()))

for ele in M_li:
    print(binary_search(A,ele))

