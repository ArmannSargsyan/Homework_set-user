#1

def makeMultiplierOf(n):
    def multiplier (x):
        return x * n
    return multiplier

result = makeMultiplierOf(4)
print(result(5))
print(result(2))
print(result(10))


#2

def makeCounter():
    count = 0
    def counter():
        nonlocal count;
        count += 1
        return count
    return counter

result = makeCounter()
print(result())
print(result())
print(result())
print(result())
print(result())


