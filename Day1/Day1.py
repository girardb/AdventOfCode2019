from functools import reduce


def first_star():
    with open('Day1Input.txt', 'r') as f:
        masses = f.read().split('\n')
    fuel_req = lambda x : int(x)//3 -2

    masses[0] = fuel_req(masses[0])
    return reduce(lambda x,y: x + fuel_req(y), masses)

def first_star_():
    with open('Day1Input.txt', 'r') as f:
        masses = f.read().split('\n')
    return sum([int(mass)//3 - 2 for mass in masses])




def second_star_():
    with open('Day1Input.txt', 'r') as f:
        masses = f.read().split('\n')
    return sum([fuel_requirement(int(mass)) for mass in masses])

def fuel_requirement(mass):
    total = 0
    fuel = mass//3 - 2
    while fuel > 0:
        total += fuel
        fuel = fuel//3 - 2
    return total

def second_star():
    with open('Day1Input.txt', 'r') as f:
        masses = f.read().split('\n')
    return sum([fuel_requirement_rec(int(mass), 0) for mass in masses])

def fuel_requirement_rec(mass, total):
    fuel = mass//3 - 2
    if fuel <= 0:
        return total
    return fuel_requirement_rec(fuel, total+fuel)
    

if __name__ == '__main__':
    print(first_star())
    print(first_star_())

    print(second_star_())
    print(second_star())