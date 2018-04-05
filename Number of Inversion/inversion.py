# This code is dedicated to the calculation of number of inversions in an array
# The array to input to the program is a text file where each line is a distinct
# integer number to be input to the program

# we import time to profile the code and see how it is working
import time
t0 = time.time()

# importing inegers
input_file = 'IntegerArray.txt'
with open(input_file, 'r') as data:
    line = data.read().split("\n")
    integers = list(map(int, line))

# this is used to calculated the inversion when the left array has elements higher than left array
# in essential this code takes care of the third part of divide and conquer algorithm, "combining"
def sort_N_countsplit(L, R, n):
    #print("input to split{},{},{}".format(L, R, n)) # uncomment for troubleshooting
    D = [0] * n # initializing an array with length equal to the concatanation of  the two inputs
    j = 0 # initializing left half counter
    i = 0 # initializing right half counter
    inversion_count = 0 # counter for the number of inversions
    flag_i = 0 # to flag that we reached the end of the left array
    flag_j = 0 # to flag that we reached the end of the right array
    for k in range(n):
        if (L[i] < R[j]  or flag_j ==1) and flag_i == 0 :
            D[k] = L[i]
            i += 1
            if i == len(L):
                flag_i = 1
                i = len(L)-1

        elif (L[i] > R[j]  or flag_i ==1) and flag_j == 0 :
            D[k] = R[j]
            j += 1
            # here is the core of the program, how we calculate the number of inversions?
            # if we jump from the left array to the right array, we count the number of inversions as the
            # number of components left inside the left array
            inversion_count += (len(L) - i - flag_i ) # this is the conquer part
            if j == len(R):
                flag_j = 1
                j = len(L)-1
        #print("inversion_count-{}".format(inversion_count)) # uncomment for troubleshooting
        #print("D-{}".format(D)) # uncomment for troubleshooting
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
        return (total_sorted, X + Y + Z)

# reporting the results
_, inversions =  sort_N_count(integers)
print("For the input set of integers in file \""+input_file+"\" there are {} numbers of inversions.".format(inversions))


# reporiting the timing of the code
print("*"*100)
t1 = time.time()
total = t1-t0

print("Counting inversions in an array of length {}K take {} seconds.".format(len(integers)/1000, round(total,3)))

# results:
#######################################################################################
#For the input set of integers in file "IntegerArray.txt" there are ##### numbers of inversions.
#****************************************************************************************************
#Counting inversions in an array of length 100.0K take 0.799 seconds.