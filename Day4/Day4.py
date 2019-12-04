from collections import Counter
import time


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
    
    count = 0
    while end >= start:
        if valid_password_bf1(end): 
            count += 1
        end = next_password(end)
    return count


def next_lower_doubles(number):
    # check if it already satisfies the double digit requirement
    list_number = list(str(number)) 
    for i in range(len(list_number)-1):
        if list_number[i] == list_number[i+1]:
            return number
   
    list_number[-1] = list_number[-2]
    return int(''.join(list_number)) 

def next_password(number):
    number = next_decreasing(number)
    
    # next with at least doubles
    number = next_lower_doubles(number)
    return number

def second_star():
    with open('input.txt') as f:
        start, end = f.read().split('-')
    start = int(start)
    end = int(end)
    
    count = 0
    while end >= start:
        if valid_password_bf2(end):
            count += 1
        end = next_password(end)
    return count
    


if __name__ == '__main__':
    start = time.time()
    print(first_star_bruteforce())
    print(time.time() - start)
    
    start = time.time()
    print(first_star())
    print(time.time()-start)
   
    print()

    start = time.time() 
    print(second_star_bruteforce())
    print(time.time() - start)
    
    start = time.time()
    print(second_star())
    print(time.time() - start)
