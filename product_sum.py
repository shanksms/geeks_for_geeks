n = int(input(''))
for i in range(0, n):
    numbers_str = input('')
    n1 = int(numbers_str.split(' ')[0])
    n2 = int(numbers_str.split(' ')[1])
    x = abs(n1 * n2)
    c = 0
    first_pass = True
    while first_pass or x > 0:
        first_pass = False
        x = int(x / 10)
        c = c + 1
    print(c)
