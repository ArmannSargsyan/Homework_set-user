#1

ls = [1, [2, [3, 4], 5], 6, [7, 8]]
def flatten_list(ls):
    flattened = []
    for item in ls:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)

    return flattened

result = flatten_list(ls)

print(result)

#2

def ls_sum(ls):
    result = 0
    for i in ls:
        result  += i  
        ls_sum(ls[1:])
    
    return result

print(ls_sum([1,2,3,5,-9]))

#3

def ls_ascending(ls):
    
    if len(ls) <= 1:
        return True
    
    elif ls[0] > ls[1]:
        return False
    
    else:
        return True

    ls_ascending(ls[1:])

    
    

ls = [1,2,3,4,5]


print(ls_ascending(ls))

#4

def prime_number(number):
    if number <= 1:
        return False
    
    elif number <= 3:
        return True
    
    elif number % 2 == 0 or number % 3 ==0:
        return False

    start_num = 5
    
    while start_num * start_num <= number:
        
        if n % i == 0 or n % (i+2) == 0:
            return False
    
    return True

print(prime_number(7))
print(prime_number(14))

#5

def numbers_max(a,b,c):
    max = a
    if max < b and b < c:
        max = c
    elif max < b and c < b:
        max = b
    
    print(max)

numbers_max(10,20,30)
numbers_max(5,1,2)
numbers_max(1,10,5)

#6

def fibonacci(number):
    if number == 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0,1]

    start_point = [0,1]
    for i in range (2,number):
        next_number = start_point[-1] + start_point[-2]
        start_point.append(next_number)
    
    return start_point

number = 5
print(f"First {number} fibonacci numbers is {fibonacci(number)}")

#7

def power_of_2(number):
    if number <= 0:
        return False

    while number % 2 == 0:
        number /= 2

    return number == 1

print(power_of_2(16))
print(power_of_2(20))
        
        

        
