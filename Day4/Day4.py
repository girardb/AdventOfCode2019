from collections import Counter


def first_star():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
 
    count = 0
    password = end
    if valid_password(password):
        count += 1    
    """
    while password >= start:
        password = next_password(password)
        count += 1
    """
    # bruteforce
    while password >= start:
        password -= 1
        if valid_password(password):
            count += 1
    
    return count

def next_password(number):
    return password

def valid_password(password):
    password = str(password)

    # Ever increasing
    if password != ''.join(sorted(password)):
        return False
        
    # double digit 
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return True    

    return False

def second_star():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
 
    count = 0
    password = end
    if valid_password_2(password):
        count += 1    
    """
    while password >= start:
        password = next_password(password)
        count += 1
    """
    # bruteforce
    while password >= start:
        password -= 1
        if valid_password_2(password):
            count += 1
    
    return count


def valid_password_2(password):
    password = str(password)
    
    if password != ''.join(sorted(password)):
        return False

    counter = Counter(password)
    for letter, occurences in counter.most_common():
        if occurences == 2:
            return True
    return False

if __name__ == '__main__':
    print(first_star())
    print(second_star())
