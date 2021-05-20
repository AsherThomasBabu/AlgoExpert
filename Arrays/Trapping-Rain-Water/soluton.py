def trapRainWater(arr, n):

    result = 0

    for i in range(1, n-1):
        left = arr[i]
        for j in range(i):
                left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        leftover = (min(left, right)-arr[i])
        result += leftover

    return result
