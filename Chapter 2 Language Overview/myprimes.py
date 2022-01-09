def isprime(n):
    if n <= 1:
        return False
    for x in range (2, n):
        if n % x == 0: # % is for the remainder
            return False    
    else :
        return True

def listprime():
    for n in range(100):
        if isprime(n):
            print(n, end=' ')

n = 6
if isprime(n):
    print("{} is prime".format(n))
    #print(f"{n} is prime")
else:
    print("{} is not a prime". format(n))
    #print(f"{n} is not a prime)

listprime()
