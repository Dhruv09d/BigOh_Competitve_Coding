'''

Find the largest number less than N whose each digit is prime number
'''

def largest_prime(N):

    for i in range(N-1, 1, -1):
        curr_prime = True
        # curr_lst = []

        a = i
        while a != 0:
            digit = a%10
            # curr_lst.append(digit)
            a = a//10

            if digit != 2 and digit != 5 and digit != 7:
                # print(digit, end=" ")
                curr_prime = False
                break
        # print(i)
        if curr_prime == True:
            return i



print(largest_prime(56))

