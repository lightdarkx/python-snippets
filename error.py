def sieve(n):
    
    lst = [True for i in range(n+1)]
    
    p = 2
    
    print(lst)
    while(p*p <= n):      
        
        if(lst[p] == True):

            for x in range(2*p,n+1,p):
                lst[x] = False
            
        
    
        
    return lst         
        

    


n = 775146
final = sieve(n)
print(final)