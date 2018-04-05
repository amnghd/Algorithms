import time

input1 = int(input("please enter the first number:\n"))
input2 = int(input("please enter the second number:\n"))


t0 = time.time()


def divider(A, B): #used to perform the division required as the first step of karatsuba
    m = max(len(str(A)),len(str(B)))
    m2 = (m // 2)
    output = [A//10**(m2), A%10**(m2), B//10**(m2), B%10**(m2), m2]
    return output


def karatsuba(num1, num2):
    if (num1 < 10 or num2 < 10):
        return num1 * num2
    else:
        divided_map = divider(num1, num2) #dividing the data in halves
        divided = list(divided_map)
        highA = divided[0]
        lowA = divided[1]
        highB = divided[2]
        lowB = divided[3]
        m2 = divided[4]

        #performing calculations
        z0 = karatsuba(lowA,lowB)
        z1 = karatsuba((highA+lowA),(highB+lowB))
        z2 = karatsuba(highA, highB)
        multiplication = (z2*10**(2*m2))+((z1-z2-z0)*10**(m2))+(z0)
        return multiplication



print(karatsuba(input1,input2))

print("*"*37)
t1 = time.time()
total = t1-t0

print(" Multiplying a {} dig number by a {} dig number using karatsuba took {} seconds.".format(len(str(input1)), len(str(input2)), round(total,3)))