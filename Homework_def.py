#1

def foo(n):
    for i in range(n,-1,-1):
        print(i)

foo(10)

#2

def foo(n):
    for i in range(0,n):
        print(i)

foo(10)

#3

def foo(ls):
    for i in ls:
        print(i)

ls = [1,2,3,4,5]
foo(ls)

#4

def foo(number):
    result = 0
    while number != 0:

        num = number % 10
        result += num
        number = number // 10
    
    print(f"Gumary havasar e {result}")

foo(12345)

#5

def foo(line):
    for i in line:
        if i.isupper():
            print(i)
            break
line = "hellO World"
foo(line)

#6

def max_element(ls):
    max = ls[0]
    for i in range(1,len(ls)):
        if ls[i] > max:
            max = ls[i]
    print(f"Maximum element is {max}")

ls = [10,500,8,30,2]
max_element(ls)

#7

def min_element(ls):
    min = ls[0]
    for i in range(1,len(ls)):
        if ls[i] < min:
            min = ls[i]
    print(f"Minimum element is {min}")

ls = [10,23,4,67,1,0]
min_element(ls)

