with open('IntegerArray.txt', 'r') as data:
    line = data.read().split("\n")
    integers = list(map(int, line))


sample_list = [1,2,3,4]

def sort_N_countsplit(L, R, n):
    D = list(range(n))
    j = 0
    i = 0
    inversion_count = 0
    flag_i = 0
    for k in range(n):
        if L[i] < R[j] and flag_i == 0:
            D[k] = L[i]
            i += 1
            if i == len(L):
                flag_i = 1
                i = len(L) - 1

        elif L[i] > R[j] or flag_i ==1:
            D[k] = R[j]
            j += 1
            j = min(j, len(R)-1)
            inversion_count += (len(L) - i -1)
    return (D, inversion_count)




def sort_N_count(array):
    n = len(array)
    if n == 1:
        return (array, 0)
    else:
        n2 = n//2
        left_half = array[:n2]
        right_half = array[n2:]
        left_sorted, X = sort_N_count(left_half)
        right_sorted, Y = sort_N_count(right_half)
        total_sorted, Z = sort_N_countsplit(left_sorted, right_sorted, n)
        return (X + Y + Z, total_sorted)

list, inversions = sort_N_countsplit([1,2,4],[3,5,6],6)


print(inversions)