
# Filename: primes.py
# Description: Generating prime numbers using the Sieve of Eratosthenes.

import math

# the following function takes in a list and removes all elements with
# the value of 0.
def remove_zero(n):
    for x in range(n.count(0)):
        n.remove(0)
    return n

# the following is the main function which generates a list of prime
# numbers from 2 to n
def primes(n):
    p = [x for x in range(2, n)]
    for a in range(0, int(math.sqrt(len(p)))):
        counter = 1
        if p[a] !=  0:
            for b in range(a, len(p), p[a]):
                if counter != 1:
                    p[b] = 0
                counter += 1
    return remove_zero(p)
