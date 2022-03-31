from functools import reduce
import math

def get_gcd(*numbers):
    return reduce(math.gcd, numbers)