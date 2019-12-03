import copy

def first_star():

    central_port = (0, 0)

    with open('input.txt', 'r') as f:
        first_wire, second_wire = f.read().split('\n')
        first_wire = first_wire.split(',')
        second_wire = second_wire.split(',')
    
    tiles_occupied_by_first_tile = set()
    intersections = []

    current_position = [0, 0]
    for command in first_wire:
        direction = command[0]
        steps = int(command[1:])
        for i in range(steps):
            if direction == 'U':
                current_position[0] += 1
            elif direction == 'D':
                current_position[0] -= 1
            elif direction == 'L':
                current_position[1] -= 1
            elif direction == 'R':
                current_position[1] += 1
            tiles_occupied_by_first_tile.add(tuple(current_position))

    current_position = [0,0]
    for command in second_wire:
        direction = command[0]
        steps = int(command[1:])
        for i in range(steps):
            #find current move
            if direction == 'U':
                current_position[0] += 1
            elif direction == 'D':
                current_position[0] -= 1
            elif direction == 'L':
                current_position[1] -= 1
            elif direction == 'R':
                current_position[1] += 1
            if tuple(current_position) in tiles_occupied_by_first_tile:
                intersections.append(copy.copy(current_position))

    min_distance = min(intersections, key=lambda x : abs(x[0])+abs(x[1]))
    return abs(min_distance[0]) + abs(min_distance[1]), min_distance





def second_star():
    central_port = (0, 0)

    with open('input.txt', 'r') as f:
        first_wire, second_wire = f.read().split('\n')
        first_wire = first_wire.split(',')
        second_wire = second_wire.split(',')
    
    tiles_occupied_by_first_tile = dict()
    intersections = []

    current_position = [0, 0]
    steps_taken = 0
    for command in first_wire:
        direction = command[0]
        steps = int(command[1:])
        for i in range(steps):
            if direction == 'U':
                current_position[0] += 1
            elif direction == 'D':
                current_position[0] -= 1
            elif direction == 'L':
                current_position[1] -= 1
            elif direction == 'R':
                current_position[1] += 1
            steps_taken += 1
            tiles_occupied_by_first_tile[tuple(current_position)] = steps_taken

    current_position = [0,0]
    steps_taken = 0
    for command in second_wire:
        direction = command[0]
        steps = int(command[1:])
        for i in range(steps):
            #find current move
            if direction == 'U':
                current_position[0] += 1
            elif direction == 'D':
                current_position[0] -= 1
            elif direction == 'L':
                current_position[1] -= 1
            elif direction == 'R':
                current_position[1] += 1
            steps_taken += 1
            if tuple(current_position) in tiles_occupied_by_first_tile:
                intersections.append((current_position[0], current_position[1], steps_taken + tiles_occupied_by_first_tile[tuple(current_position)]))

    min_distance = min(intersections, key = lambda x : x[2])
    return min_distance[2]

# Doesn't work for some reason
def first_star_interval():
    with open('input.txt', 'r') as f:
        first_wire, second_wire = f.read().split('\n')
        first_wire = first_wire.split(',')
        second_wire = second_wire.split(',')

    first_wire_intervals = [(0,0),]
    current_position = [0, 0]
    for command in first_wire:
        direction = command[0]
        steps = int(command[1:])
        if direction == 'U':
            current_position[0] += steps
        elif direction == 'D':
            current_position[0] -= steps
        elif direction == 'L':
            current_position[1] -= steps
        elif direction == 'R':
            current_position[1] += steps
        first_wire_intervals.append(tuple(current_position))

    second_wire_intervals = [(0,0),]
    current_position = [0, 0]
    for command in second_wire:
        direction = command[0]
        steps = int(command[1:])
        if direction == 'U':
            current_position[0] += steps
        elif direction == 'D':
            current_position[0] -= steps
        elif direction == 'L':
            current_position[1] -= steps
        elif direction == 'R':
            current_position[1] += steps
        second_wire_intervals.append(tuple(current_position))


    intersections = []
    for i in range(len(second_wire_intervals)-1):
        sw_interval1, sw_interval2 = sorted([second_wire_intervals[i], second_wire_intervals[i+1]])
        sw_orientation = is_vertical_line(sw_interval1, sw_interval2)
        sw_var = sw_interval1[1] if sw_orientation else sw_interval1[0]
        sw_interval = [sw_interval1[0], sw_interval1[0]] if sw_orientation else [sw_interval1[1], sw_interval2[1]]

        for j in range(len(first_wire_intervals)-1):
            fw_interval1, fw_interval2 = sorted([first_wire_intervals[j], first_wire_intervals[j+1]])
            fw_orientation = is_vertical_line(fw_interval1, fw_interval2)
            fw_var = fw_interval1[1] if fw_orientation else fw_interval1[0]
            fw_interval = [fw_interval1[0], fw_interval2[0]] if fw_orientation else [fw_interval1[1], fw_interval2[1]]

            if sw_orientation == fw_orientation:
                if sw_var == fw_var: #never happens
                    pass
            else:
                if intersection(fw_var, fw_interval, sw_var, sw_interval):
                    intersections.append(list([fw_var, sw_var]))

    min_distance = min(intersections, key=lambda x : abs(x[0])+abs(x[1]))
    return abs(min_distance[0]) + abs(min_distance[1]), min_distance

def is_vertical_line(intervalA, intervalB):
    y1, x1 = intervalA
    y2, x2 = intervalB
    return x2 == x1

def intersection(fw_var, fw_interval, sw_var, sw_interval):
    if sw_interval[0] <= fw_var <= sw_interval[1] and fw_interval[0] <= sw_var <= fw_interval[1]:
        return True
    return False


def second_start_interval():
    pass

if __name__ == '__main__':
    print(first_star())
    print(second_star())

    #print(first_star_interval())
    #print(second_star_interval())