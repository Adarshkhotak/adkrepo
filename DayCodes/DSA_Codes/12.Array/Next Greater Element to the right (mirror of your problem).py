def next_greater(arr):
    res = [-1] * len(arr)
    stack = []  # monotonic decreasing
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res

print(next_greater([2, 4, 8, 3, 5, 9]))   # [4, 8, 9, 5, 9, -1]