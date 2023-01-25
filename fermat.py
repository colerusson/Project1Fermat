import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    # This function is the modular exponentiation test
    # You will need to implement this function and change the return value.

    # initialize the result to 1 that we will eventually return
    result = 1
    x = x % N

    # loop while y is greater than 0 and still has bits
    while y > 0:

        # check if y is even
        if y % 2:
            result = (result * x) % N
            y = y - 1
        # if y is odd
        else:
            x = (x ** 2) % N
            y = y // 2

    # return the result modded by N
    return result % N


def fprobability(k):
    # This function is for the probability that k Fermat trials gives the correct answer
    # You will need to implement this function and change the return value.
    return 1 - ((1/2)**k)


def mprobability(k):
    # This function is for the probability that k Miller-Rabin trials gives the correct answer
    # You will need to implement this function and change the return value.   
    return 1 - ((1/4)**k)


def fermat(N, k):
    # This function is the fermat primality test
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # getting rid of the edge cases of low primes and non primes to avoid
    # unnecessary calculation
    if N <= 1 or N == 4:
        return 'composite'
    if N <= 3:
        return 'prime'

    # loop through each value up to k
    for i in range(k):
        # call the modular exponentiation function
        output = mod_exp(random.randint(2, N - 2), N - 1, N)

        # break out of the loop early if the value is found to be composite
        if output != 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # This function is the Miller-Rabin primality test
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # getting rid of the edge cases of low primes and non primes to avoid
    # unnecessary calculation
    if N <= 1 or N == 4:
        return 'composite'
    if N <= 3:
        return 'prime'

    b = N - 1
    while b % 2 == 0:
        b = b // 2

    # loop through the values up to k to test each value
    for i in range(k):
        # break out of the calculation early if found to be composite
        if miller_rabin_helper(b, N) == 'composite':
            return 'composite'

    return 'prime'


def miller_rabin_helper(b, N):
    # initialize the random value
    a = 2 + random.randint(1, N - 4)

    # call the modular exponentiation function
    x = mod_exp(a, b, N)
    if x == 1 or x == N - 1:
        return 'prime'

    while b != N - 1:
        # break down the power value in half
        x = (x * x) % N
        b = b * 2

        # return early as composite if found composite before reaching all base cases
        if x == 1:
            return 'composite'
        # return early as prime if found prime before reaching all base cases
        if x == N - 1:
            return 'prime'

    return 'composite'
