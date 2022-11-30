'''Display Fibonacci series up to 10 terms'''

n1 = 0
n2 = 1

for i in range (0, 11):

    print(n1)

    next_num = n1 + n2

    n1 = n2
    n2 = next_num