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


def Day3():

    f = open("AdventOfCode2020/input3.txt", "r")
    area = []
    for line in f:
        area.append(line.rstrip("\n"))

    # area = [
    #     "..##.......",
    #     "#...#...#..",
    #     ".#....#..#.",
    #     "..#.#...#.#",
    #     ".#...##..#.",
    #     "..#.##.....",
    #     ".#.#.#....#",
    #     ".#........#",
    #     "#.##...#...",
    #     "#...##....#",
    #     ".#..#...#.#",
    # ]
    slops = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = []
    for slop in slops:
        tree = 0
        flat = 0
        x = 0
        y = 0
        while (y < len(area) - 1):
            y += slop[1]
            x += slop[0]
            pos = x % len(area[0])
            if area[y][pos] == '#':
                tree += 1
            else:
                flat += 1

        print(tree)
        res.append(tree)
    tot = 1
    for x in res:
        tot = tot * x
    print(tot)


def Day4():

    f = open("AdventOfCode2020/input4.txt", "r")
    passports = []
    for line in f:
        passports.append(line.rstrip("\n"))

    # passports = [
    #     "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    #     "byr:1937 iyr:2017 cid:147 hgt:183cm",
    #     "",
    #     "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    #     "hcl:#cfa07d byr:1929",
    #     "",
    #     "hcl:#ae17e1 iyr:2013",
    #     "eyr:2024",
    #     "ecl:brn pid:760753108 byr:1931",
    #     "hgt:179cm",
    #     "",
    #     "hcl:#cfa07d eyr:2025 pid:166559648",
    #     "iyr:2011 ecl:brn hgt:59in",
    # ]
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None
    validpass = 0
    invaldipass = 0
    nrpass = 0
    x = 0
    while (x < len(passports)):
        if passports[x] == "":

            try:
                if (int(byr) <= 2002 and int(byr) >= 1920 and
                    int(iyr) <= 2020 and int(iyr) >= 2010 and
                    int(eyr) <= 2030 and int(eyr) >= 2020 and
                    ((hgt[-2:] == "cm" and int(hgt[0:-2]) <= 193 and int(hgt[0:-2]) >= 150) or
                    (hgt[-2:] == "in" and int(hgt[0:-2]) <= 76 and int(hgt[0:-2]) >= 59)) and
                    hcl[0] == "#" and int(hcl[1:], 16) and
                    (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth") and
                        len(pid) == 9 and int(pid) > 0):
                    validpass += 1
            except:
                pass
            byr = None
            iyr = None
            eyr = None
            hgt = None
            hcl = None
            ecl = None
            pid = None
            cid = None
        else:
            entries = passports[x].split(" ")
            for ent in entries:
                if ent[:4] == "byr:":
                    byr = ent[4:]
                elif ent[:4] == "iyr:":
                    iyr = ent[4:]
                elif ent[:4] == "eyr:":
                    eyr = ent[4:]
                elif ent[:4] == "hgt:":
                    hgt = ent[4:]
                elif ent[:4] == "hcl:":
                    hcl = ent[4:]
                elif ent[:4] == "ecl:":
                    ecl = ent[4:]
                elif ent[:4] == "pid:":
                    pid = ent[4:]
        x += 1
    try:
        if (int(byr) <= 2002 and int(byr) >= 1920 and
                    int(iyr) <= 2020 and int(iyr) >= 2010 and
                    int(eyr) <= 2030 and int(eyr) >= 2020 and
                    ((hgt[-2:] == "cm" and int(hgt[0:-2]) <= 193 and int(hgt[0:-2]) >= 150) or
                    (hgt[-2:] == "in" and int(hgt[0:-2]) <= 76 and int(hgt[0:-2]) >= 59)) and
                    hcl[0] == "#" and int(hcl[1:], 16) and
                    (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth") and
                        len(pid) == 9 and int(pid) > 0):
            validpass += 1
    except:
        pass
    print(validpass, invaldipass, nrpass)




if __name__ == '__main__':
    Day4()