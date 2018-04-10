input_file = 'QuickSort.txt'

with open(input_file, 'r') as data:
    line = data.read().split("\n")
    integers = list(map(int, line))

def partition(A,l):
    l = 0 # pivot point
    r = len(A)
    if r ==1:
        return A
    elif r > 1:
        pivot = A[l]
        i = 1
        for j in range(l+1, r):
            if A[j] < pivot:
                A[j], A[i] = A[i], A[j]
                i += 1
        A[l], A[i-1] = A[i-1], A[l]
        left = A[:i-1]
        right = A[i:]
        sorted_left = [].extend(partition(left, 0))
        sorted_right = [].extend(partition(right, 0))

        return sorted_left.append(pivot).append(sorted_right)

print (partition ([2,3],0))
