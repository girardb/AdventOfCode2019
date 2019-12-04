from collections import Counter


def first_star_bruteforce():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
 
    count = 1 if valid_password_bf1(end) else 0
    
    while end >= start:
        end -= 1
        if valid_password_bf1(end):
            count += 1
    
    return count

def next_decreasing(number):
    number -= 1
    list_number = list(str(number))  

    index = len(list_number) - 1 
    while list_number != sorted(list_number):
        list_number[index] = '9'
        list_number[index-1] = str(int(list_number[index-1]) -1)
        index -= 1

    return int(''.join(list_number))

def valid_password_bf1(password):
    password = str(password)
    
    # Ever increasing
    if password != ''.join(sorted(password)):
        return False
        
    # double digit 
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return True    
    return False

def second_star_bruteforce():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
 
    count = 1 if valid_password_bf1(end) else 0
    
    # bruteforce
    while end >= start:
        end -= 1
        if valid_password_bf2(end):
            count += 1
    
    return count


def valid_password_bf2(password):
    password = str(password)
    
    if password != ''.join(sorted(password)):
        return False

    counter = Counter(password)
    for letter, occurences in counter.most_common():
        if occurences == 2:
            return True
    return False


def first_star():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
    
    count = 1 if valid_password_bf1(end) else 0
    while end >= start:
        #end = next_password(end)
        end = next_decreasing(end)
        if valid_password_bf1(end): 
            count += 1 
    return count

def next_increasing(number):
    pass

def next_doubles(number):
    pass

def next_password(number):
    number = next_increasing(number)
    
    # next with at least doubles
    number = next_doubles(number)

def second_star():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
    
    count = 1 if valid_password_bf2(end) else 0
    while end >= start:
        end = next_password(end)
        if valid_password_bf2(end):
            count += 1 
    return count
    


if __name__ == '__main__':
    print(first_star_bruteforce())
    #print(second_star_bruteforce())

    print(first_star())
    #print(second_star())
