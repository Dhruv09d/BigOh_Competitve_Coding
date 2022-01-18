'''
Write a program to find the smallest number divisible by all the numbers between 1 to 9

'''

def sm_num(num):
    divisor = [2, 3, 4, 5, 6, 7, 8]
    for i in range(1, num):
        curr = True
        for j in range(len(divisor)):
            if i % divisor[j] != 0:
                curr = False
                break
        if curr == True:
            return i

print(sm_num(900))
# print(2*3*4*5*6*7*8) = 40320