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
    return abs(min_distance[0]) + abs(min_distance[1])




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

if __name__ == '__main__':
    print(first_star())
    print(second_star())