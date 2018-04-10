input_file = 'QuickSort.txt' # input file that has a list of integers

counter = 0
with open(input_file, 'r') as data: # accessing the integers in the data
    line = data.read().split("\n")
    integers = list(map(int, line))



def partition(A,l):
    global counter
    r = len(A)
    pivot = A[l]
    i = 1
    for j in range(l+1, r):
        counter += 1
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j] # swaping in case comparison hold true
            i += 1
    A[l], A[i-1] = A[i-1], A[l] # moving the pivot element
    return i-1 # note, although we are returning i-1, we have changed A in place


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        l = 0
        m = partition(A, l)
        left = QuickSort(A[:m])
        right = QuickSort(A[m+1:])
        A[:m], A[m+1:] = left, right
        return A

print(QuickSort(integers))
print(counter)
