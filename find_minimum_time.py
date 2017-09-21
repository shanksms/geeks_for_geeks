
#code
test_cases = int(input(''))


for count in range(0, test_cases):
    i = 0
    input_str = input('')
    ls = input_str.split(' ')
    n1 = int(ls[0])
    n2 = int(ls[1])
    c = int(ls[2])
    while True:
        if i != 0 and i % n1 == 0:
            c = c - 1
        if c == 0:
            break
        if i != 0 and i % n2 == 0:
            c = c - 1
        if c == 0:
            break
        i = i + 1
    print(i)
