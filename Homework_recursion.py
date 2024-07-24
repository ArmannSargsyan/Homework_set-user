#1
def foo(x):
    if x <= 0:
        return
    foo(x-1)
    print(x)
    return

foo(5)

#2

def foo(x):
    if x <= 0:
        return
    print(x)
    foo(x-1)
    return

foo(5)

#3

def fac(x):
    if x == 1 :
        return 1
    return x * fac(x-1)

result = fac(5)
print(f"Factorial = {result}")

#4

def sum(n):
    if n == 0 :
        return n
    return n + sum(n-1)

result = sum(3)
print(f"Sum = {result}")

#5

def ls_elements(ls):
    if not ls:
        return
    print(ls[0])
    ls_elements(ls[1:])
    

ls = [1,2,3,4,5]
ls_elements(ls)

#6

length = 0
def ls_length(ls):
    
    if not ls:
        return
    global length;
    length += 1
    ls_length(ls[1:])
    return length

ls = [1,2,3,4,5,6,7,8]
length = ls_length(ls)
print(f"Length of ls = {length}")

#7

def rev_str(st):
    if not st:
        return
    print(st[len(st)-1])
    rev_str(st[:len(st)-1])

st = "Hello"
rev_str(st)

#8

def fibonacci(n):
    if n <= 0:
        return
    elif n == 1 :
        return 0
    elif n == 2: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
n = 10
number = fibonacci(n)
print(f"The {n}-th fibonacci number is {number}")

#9

def characters_of_string(st):
    if not st:
        return
    print(st[0])
    characters_of_string(st[1:])

st = "Hello"
characters_of_string(st)

#10

def characters(st):
    if not st:
        return
    return st[0]
    characters(st[1:])

def rev_characters(st):
    if not st:
        return
    return st[len(st)-1]
    rev_characters(st[:len(st)-1])

st = "Hello"

if characters(st) == rev_characters(st):
    print("Word is palidrome")
else:
    print("Word isn't palidrome")

#11

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

number = 123
result = sum_of_digits(number)
print(f"The sum of {number} digits is {result}")

