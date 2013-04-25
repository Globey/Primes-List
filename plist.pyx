%cython
from libc.math cimport floor

def prime_lister():
    cdef int n,i,floored_root
    primeList = range(2,10001)
    for n in range(2,10001):
        floored_root = int(floor(sqrt(n)))
        for i in range(2,floored_root+1):
            if n%i == 0 and n in primeList:
                primeList.remove(n)
    return primeList
