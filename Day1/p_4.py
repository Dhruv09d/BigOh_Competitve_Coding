'''
Write a program to find the smallest number divisible by all the numbers between 1 to 9

'''

def sm_num():
    num_found = False
    i = 1
    divisor = [2, 3, 4, 5, 6, 7, 8]
    while num_found != True:
        curr = True
        for j in range(len(divisor)):
            if i % divisor[j] != 0:
                curr = False
                break

        if curr == True:
            num_found = True
            return i
        i += 1

print(sm_num())
# print(2*3*4*5*6*7*8) = 40320