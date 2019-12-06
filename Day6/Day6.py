def first_star():
    
    orbits = create_map('input.txt')

    total_orbits = 0
    for space_object in orbits:
        total_orbits += 1
        while orbits[space_object] != 'COM':
            space_object = orbits[space_object]
            total_orbits += 1
    return total_orbits        


def second_star():
    orbits = create_map('input.txt')
    orbits['COM'] = None    
    visited = dict()

    # Start at both locations and continue searching until they have both met the same object and then add the distance from the first object that reached it plus the distance from the second one
    YOU_distance = -1
    YOU_position = 'YOU'
    SAN_distance = -1
    SAN_position = 'SAN'
   
    # TODO: change while loop
    while True:
        # YOU
        if YOU_position not in visited and YOU_position != None:
            YOU_distance += 1
            visited[YOU_position] = YOU_distance
            YOU_position = orbits[YOU_position]
        else:
            return visited[YOU_position] + YOU_distance -1
        
        # SAN
        if SAN_position not in visited and SAN_position != None:
            SAN_distance += 1
            visited[SAN_position] = SAN_distance
            SAN_position = orbits[SAN_position]
        else:
            return visited[SAN_position] + SAN_distance -1


def create_map(text_file):
    with open('input.txt', 'r') as f:
        direct_orbits = f.read().split('\n')[:-1] #trailing space
    
    orbits = dict()
    for orbit in direct_orbits:
        TO, FROM = orbit.split(')')
        orbits[FROM] = TO
    return orbits 


if __name__ == '__main__':
    print(first_star())
    print(second_star())
