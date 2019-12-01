from functools import reduce


def first_star():
    with open('FirstStarInput.txt', 'r') as f:
        masses = f.read().split('\n')
    fuel_req = lambda x : int(x)//3 -2

    masses[0] = fuel_req(masses[0])
    return reduce(lambda x,y: x + fuel_req(y), masses)

def first_star_():
    with open('FirstStarInput.txt', 'r') as f:
        masses = f.read().split('\n')
    return sum([int(mass)//3 - 2 for mass in masses])





# n*log(n) operations
def second_star_():
    with open('FirstStarInput.txt', 'r') as f:
        masses = f.read().split('\n')
    return sum([fuel_requirement(int(mass)) for mass in masses])

def fuel_requirement(mass):
    total = 0
    fuel = mass//3 - 2
    while fuel > 0:
        total += fuel
        fuel = fuel//3 - 2
    return total
    

if __name__ == '__main__':
    print(first_star())
    print(first_star_())

    print(second_star_())