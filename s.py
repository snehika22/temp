function power(arr):
    n = length(arr)
    result = []
    for i from 0 to 2^n - 1:
        subset = []
        for j from 0 to n - 1:
            if (i & (1 << j)) != 0:
                append arr[j] to subset
        append subset to result
    return result

arr = [1, 2, 3]
result = power(arr)
print(length(result))