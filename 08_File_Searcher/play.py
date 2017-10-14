

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)



print('3! = {}'.format(factorial(3)))
print('10! = {:,}'.format(factorial(10)))

# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    nums = []
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


print('No yeild')
for n in (fibonacci(100)):
    print(n, end=', ')


def fibonacci_co(limit):

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current

print()
print('With yield')
for n in (fibonacci_co(100)):
    print(n, end=', ')
