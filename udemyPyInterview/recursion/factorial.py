def fact(n):

    # Base case
    if n == 0:
        return 1

    else:
        return n * fact(n - 1)

print(fact(1))
print(fact(2))
print(fact(3))
print(fact(5))
print(fact(10))