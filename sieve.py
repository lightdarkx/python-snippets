import math
def primes(n):
    lst = []
    for i in range(2,n+1):
        lst.append(i)
    
    p = 2
    while(p * p < n):
          
        for i in lst:
            if i > p:
                p = i
                break
        #print(p,n)
        
        for x in range(2*p,n+1,p):
            try:
                lst.remove(x)
            except:
                continue
        #print(lst)
            

    return lst         
        
def highestF(lst,n):
    
    factors = []
    for i in lst:
        if n % i == 0:
            factors.append(i)
            print(i)
    
    return factors
        


            




n = 30
#600851475143
root = math.sqrt(n)
print(root)
sieve = primes(int(root)+1)
print(sieve)
final = highestF(sieve,n)
print(final)
print("Highest factor: ",final[-1])