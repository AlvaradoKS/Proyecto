def inversion(n):
    if n<10:
        return n
    else:
        return (n%10)*(10**(cd(n)-1))+inversion(n//10)

def cd(n):
    if n<10:
        return 1
    else:
        return 1+cd(n//10)

'''
assert ConvertirABase(n,b==0,c)
assert ConvertirABase(n,b>9,c)
assert ConvertirABase(n,b<2,c) 
'''

def ConvertirABase(n,b,c):
    if n==b:
        return 10
    else:
        if n>1:
            return ConvertirABase(n//b,b,(c*10)+(n%b))
        else:
            return (inversion(c*10+n))
    
'''
assert b>9, "error"
assert b<2, "error"
assert n>=b, "error"
'''

def ConvertirABaseDiez(n,b,c,d):
    if n<10:
        return c+(n*b**cd(n-1))
    else:
        return ConvertirABaseDiez(n//10,b,c+(n%10)*b**(cd(n)-(cd(n)-d)),d+1)

print (ConvertirABaseDiez(32,4,0,0))
print (ConvertirABase(14,4,0))


