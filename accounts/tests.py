from django.test import TestCase

# Create your tests here.
def sieve(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i in range(2, math.floor(math.sqrt(limit))):
        if primes[i]:
            for j in range(i*i, limit, i):
                #print(primes[j])
                primes[j] = False
    return primes