a = ["{", "[", "("]
b = ["}","]",")"]

def is_matched(expression):
    ctr = 0
    answer = True
    last_letter =""
    for letter in expression:
        if letter in a:
            ctr += 1
        elif letter in b:
            ctr -= 1
            if ctr<0:
                answer = False
                break
        if (last_letter in a) and (letter in b):
            if a.index(last_letter) != b.index(letter):
                answer = False
                break
        last_letter = letter
    if ctr !=0 :
        answer = False

    return answer

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")