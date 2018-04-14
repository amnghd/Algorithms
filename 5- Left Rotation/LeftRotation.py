def array_left_rotation(a, n, k):
    B = [0 for x in range(n)]
    for i in range(n):
        B[i-k] = a[i]
    return B

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
