#code
n = int(input(''))
for i in range(0, n):
    number = int(input(''))
    power_of_eight = True
    while number != 1:
        if number % 8 != 0:
            power_of_eight = False
            break
        else:
            number = number/8

    if power_of_eight == True:
        print('Yes')
    else:
        print('No')
