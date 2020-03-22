li = list(map(int, input().split()))

if sorted(li) == li:
    print("ascending")
elif sorted(li, reverse=True) == li:
    print("descending")
else:
    print("mixed")