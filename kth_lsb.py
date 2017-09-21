test_cases = int(input(''))

for count in range(0, test_cases):
    n , k = map(int, input('').split())
    print((n >> (k-1)) & 1)
