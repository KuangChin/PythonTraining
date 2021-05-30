from itertools import permutations


def get_permutations(input):
    if len(input)==1:
        return [input[0]]
    results = []
    for i, j in enumerate(input):
        others = input[0:i]+input[i+1:]
        for k in get_permutations(others):
            results.append(j + k)
    return results
        
        

def is_VampireNumber(input):
    # num_factors = permutations(input)
    num_factors = get_permutations(input)
    # print(type(num_factors))
    for i in num_factors:
        # i = ''.join(i)
        for j in range(1, len(i)-1):
            if (int(''.join(i[0:j])) * int(''.join(i[j:]))) == int(input):
                print(int(''.join(i[0:j])), int(''.join(i[j:])))
                return True
    return False
        

print(is_VampireNumber('110758'))
# print(get_permutations('123'))
# t = ('1', '2', '6', '0')
# print(t[:0] + t[1:])
# print(['1'+substr for substr in ['2','3']])