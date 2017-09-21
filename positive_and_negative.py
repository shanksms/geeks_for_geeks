#number of test cases
n = int(input(''))
for i in range(1, n + 1):
    number_of_elements = int(input(''))
    elements = list(map(int, input('').split()))
    #print(elements)
    pos_list = [element for element in elements if element > 0]
    neg_list = [element for element in elements if element < 0]
    final_list = []
    for e1, e2 in zip(pos_list, neg_list):
        final_list.append(str(e1))
        final_list.append(str(e2))
    print(" ".join(final_list))
