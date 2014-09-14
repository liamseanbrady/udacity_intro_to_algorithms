#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#

import random

def minimize_absolute(L):
    pos = len(L)/2 + 1
    return max( top_k(L, pos) )

def partition(L, v):
    smaller = []
    bigger = []
    same = []
    for val in L:
        if val < v: smaller.append(val)
        elif val > v: bigger.append(val)
        else: same.append(val)
    return (smaller, same, bigger)

def top_k(L, k):
    v = random.choice(L)
    (left, middle, right) = partition(L, v)
    if len(left) > k: return top_k(left, k)
    elif len(left) == k: return left
    elif len(left) + len(middle) == k: return left + middle 
    elif len(left) + len(middle) > k: return left + middle[: k - len(left)] 
    elif len(left) < k:
        return left + middle + top_k(right, k - len(left) - len(middle))