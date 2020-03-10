doc = input()
word = input()

idx = 0
result = 0

while len(doc) - idx >= len(word):
    if doc[idx:idx+len(word)] == word:
        result += 1
        idx += len(word)
    else:
        idx += 1

print(result)