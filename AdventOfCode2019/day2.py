
def get_input(file):
    with open(file, 'r') as f:
        results = f.readline().rstrip().split(',')
        return list(map(int, results))


def op(code, x, y):
    if code == 1:
        return x + y
    elif code == 2:
        return x * y


def run(data):
    i = 0
    while data[i] != 99:
        res = op(data[i], data[data[i+1]], data[data[i+2]])
        data[data[i+3]] = res
        i += 4
    return data[0]


def verb_noun(mem, noun, verb):
    mem[1] = noun
    mem[2] = verb
    res = run(mem)
    return res


if __name__ == "__main__":
    data = get_input("day2.input")

    # data = [1,1,1,4,99,5,6,0,99]
    # data = [1,9,10,3,2,3,11,0,99,30,40,50]
    for x in range(0, 99):
        for y in range(0, 99):
            in_data = list(data)
            if (verb_noun(in_data, x, y) == 19690720):
                print(x, y)
                print(100 * x + y)
                break
