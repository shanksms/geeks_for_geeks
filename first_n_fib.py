


cases = int(input(''))
for count in range(0, cases):
    n = int(input(''))
    ls = []
    if n == 1:
        ls.append(1)
    else:
        ls.append(1)
        ls.append(1)
        for count in range(2, n):
            ls.append(ls[count - 1] + ls[count - 2])
    list_str = list(map(str, ls))
    print(" ".join(list_str))
