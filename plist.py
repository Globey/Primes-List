#Calculates all primes up to 10000 and returns a list containing said primes using a very slow trial method.
def prime_lister():
    primeList = range(2,10001)
    #print primeList
    for n in range(1,10001):
        #print n
        floored_root = int(math.floor(sqrt(n)))
        #print 'the floored_root is ' + str(floored_root)
        for i in range(2,floored_root+1):
            #print 'i is ' + str(i)
            #print 'the boolean for n%' + str(i) + ' is' + str(n%i)
            if n%i == 0 and n in primeList:
                #print "Removing " + str(n)
                primeList.remove(n)
    return primeList
