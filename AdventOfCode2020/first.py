def Day1():
    f = open("AdventOfCode2020/input1.txt", "r")
    expense = []
    for lines in f:
        expense.append(int(lines))

    for x in expense:
        for y in expense:
            if x + y == 2020:
                print(x * y)

    for x in expense:
        for y in expense:
            for z in expense:
                if x + y + z == 2020:
                    print(x * y * z)


def Day2():
    f = open("AdventOfCode2020/input2.txt", "r")
    passwords = []
    for lines in f:
        passwords.append(lines)

    # passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    invalid_pass = 0
    for password in passwords:
        pass_split = password.split(' ')
        (min_nr, max_nr) = pass_split[0].split('-')
        occur = pass_split[2].count(pass_split[1][0])
        # if occur < int(min_nr) or occur > int(max_nr):
        #     invalid_pass += 1
        if (pass_split[2][int(min_nr)-1] == pass_split[2][int(max_nr)-1] or
                (pass_split[2][int(min_nr)-1] != pass_split[1][0] and
                 pass_split[2][int(max_nr)-1] != pass_split[1][0])):
            invalid_pass += 1
    print(len(passwords) - invalid_pass)


if __name__ == '__main__':
    Day2()