t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    value = 0
    max = 0
    for i in range(len(array) - 1, -1, -1):
        if array[i] > max:
            max = array[i]
        else:
            value += max - array[i]
    print(value)