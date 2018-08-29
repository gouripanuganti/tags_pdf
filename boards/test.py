def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
# driver code
a = [54, 546, 548, 60, ]
sorted_array = sorted(a, key=cmp_to_key(comparator))
number = "".join([str(i) for i in sorted_array])
print(number)

import math

def sieve(limit):
    # Sieve of Eratosthenes to find prime numbers
    primes = [True] * limit
    primes[0] = primes[1] = False
    for j in range(2, math.floor(math.sqrt(limit))):
        if primes[j]:
            for i in range(j*j ,limit, j ):
                primes[i] = False
    return primes


def main():
    """Main function. This is teh driver function where It print the circular Primes"""
    limit = 100000
    count = 0
    sum = 0
    primes = sieve(limit)

    for num in range (2, limit):
        q = False
        num = str(num)
        for i in range(len(num)):
            try:
                if primes[int(num[i:]+num[:i])]:
                    q = True
                else:
                    q = False
                    break
            except IndexError as ie:
                pass
        if q:
            count += 1
            sum = int(num) + sum
            print(num)
    print(count)
    print(sum)
if __name__ == "__main__":
    main()
# import itertools
# import math
#
#
# def is_prime(n):
#     for num in range(2,math.floor(math.sqrt(n)+1)):
#         if n%num == 0:
#             return False
#     return True
#
# def main():
#     """Main function"""
#     print("Hello, world!")
#     count = 4
#     nb_digits = 9
#     final_numbers = {'1', '3', '7', '9'}
#     for l in range(2, nb_digits+1):
#         for p in itertools.product(final_numbers, repeat=l):
#             p_int = int(''.join(p))
#             perm = {int(''.join(p[i:]+p[:i])) for i in range(len(p))}
#             if p_int == min(perm) and all(is_prime(n) for n in perm):
#                 #print(p, len(perm))
#                 count += len(perm)
#     print (count)

new_str = input("Please enter a string to Swap cases: ")
print(new_str.swapcase())

import re
def count_substring(string, sub_string):
    count = start = 0
    print(len(re.findall('(?={0})'.format(re.escape(sub_string)),string)))
    while True:
        start  = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count