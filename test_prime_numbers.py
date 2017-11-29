#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 19:49:31 2017

@author: ori
"""

import numpy as np
import time
start_time1 = time.time()

### creating array of palindromes, with odd length, othervise it will be 
### devisible by 11, last and first number should not be 0 or divisible by 2

upp_limit = 10**5 #lowest number with 6 digits
pali = []
for a1 in range(1, 10, 2):
    for a2 in range(0, 10):
        for a3 in range(0, 10):
            for a4 in range(0, 10):
                for a5 in range(0, 10):
                    pali = np.append(pali,int(10**8*a1+10**7*a2+10**6*a3+10**5*a4\
                                         +10**4*a5+10**3*a4+10**2*a3+10*a2+a1))

print('all specific palindromes in range found, amounting {0} instances\n'.format(len(pali))) 

#### creating array of all the odd numbers in range

all_numbers = np.arange(3, upp_limit, 2)
primes = np.int_([])
  
def not_devisible(all_numbers, number):
    return (all_numbers%number != 0)

while len(all_numbers) >= 1:
    if all_numbers[0] <= upp_limit/10-1:
        pali = pali[not_devisible(pali, all_numbers[0])]
    else:
        primes = np.append(primes, all_numbers[0])
    all_numbers = all_numbers[not_devisible(all_numbers, all_numbers[0])]

print('all primes in range found, amounting {0} instances\n'.format(len(primes))) 
print(('reduced number of palindromes to {0} instances '
       'that are not divisible by primes less then {1}\n').format(len(pali),\
                                                   int(upp_limit/10-1))) 

### iterating from the end of the array of pali to find the first number
### that has 0 as the remainder of the division by prime numbers in range

ind = len(pali) - 1
while min(pali[ind]%primes) != 0:
    ind -= 1

print('biggest palindrome satisfiyng constraints: %i\n' %(pali[ind]))
print('corresponding prime numbers are: {0}\n'.format(primes[pali[ind]%primes == 0]))    
print("---total time elapsed: %s seconds ---" % (time.time() - start_time1))

