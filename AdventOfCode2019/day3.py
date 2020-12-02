from pprint import pprint
from typing import List


def get_input(file):
    ret = []
    with open(file, 'r') as f:
        for x in f.readlines():
            ret.append(x.rstrip().split(','))
    return ret


def translate_to_coordinates(data):
    points = [[(0, 0)], [(0, 0)]]  # type: List
    i = 0
    for wire in data:
        current_pos = (0, 0)
        for movement in wire:
            if movement[0] == 'U':
                current_pos = (current_pos[0] + int(movement[1:]), current_pos[1])
            elif movement[0] == 'D':
                current_pos = (current_pos[0] - int(movement[1:]), current_pos[1])
            elif movement[0] == 'R':
                current_pos = (current_pos[0], current_pos[1] + int(movement[1:]))
            elif movement[0] == 'L':
                current_pos = (current_pos[0], current_pos[1] - int(movement[1:]))
            points[i].append(current_pos)
        i += 1
    return points


def trace(t_point, line):
    intersections = []
    for x in range(0, len(line)-1):
        if line[x][0] == t_point[0]:
            # print(t_point, line[x])
            if t_point[1] in range(min(line[x][1], line[x + 1][1]),
                                   max(line[x][1], line[x + 1][1])):
                intersections.append(t_point)
        elif line[x][1] == t_point[1]:
            # print(t_point, line[x])
            if t_point[0] in range(min(line[x][0], line[x + 1][0]),
                                   max(line[x][0], line[x + 1][0])):
                intersections.append(t_point)
    return intersections


if __name__ == "__main__":
    data = get_input("day3.input")
    # data = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    #         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
    # data = [['R8', 'U5', 'L5', 'D3'],
    #         ['U7', 'R6', 'D4', 'L4']]

    wire_locations = translate_to_coordinates(data)
    # print(wire_locations[0])
    # print(wire_locations[1])
    cross_sections = []  # type: List
    prev_point = (0, 0)
    for point in wire_locations[0]:
        if prev_point[0] == point[0]:
            for x in range(min(prev_point[1], point[1]), max(prev_point[1], point[1])):
                cross_sections += trace((point[0], x), wire_locations[1])
        else:
            for x in range(min(prev_point[0], point[0]), max(prev_point[0], point[0])):
                cross_sections += trace((x, point[1]), wire_locations[1])
        prev_point = point

    # print(cross_sections)
    closes_point = (0, 0)
    prev_length = abs(cross_sections[0][0]) + abs(cross_sections[0][1])
    for p in cross_sections:
        length = abs(p[0]) + abs(p[1])
        if (length < prev_length):
            closes_point = p
            # print(closes_point)
            # print(length)
            prev_length = length
    print(closes_point)
    print(prev_length)
