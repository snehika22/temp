def power(arr):
    n = len(arr)
    result = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset.append(arr[j])
        result.append(subset)
    return result

arr = [1, 2, 3]
result = power(arr)
print(len(result))  # Should print 2^3 = 8
