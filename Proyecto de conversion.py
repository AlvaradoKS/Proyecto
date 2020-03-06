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


def ConvertirABase(n,b,c):
    if b==0:
        return "Base inválida"
    if b<2 or b>9:
        return "Base inválida"
    if n==b:
        return 10
    else:
        if n>1:
            return ConvertirABase(n//b,b,(c*10)+(n%b))
        else:
            return (inversion(c*10+n))
    
def ConvertirABaseDiez(n,b,c,d):
    if b<2 or b>9:
        return "Base inválida"
    if n<10:
        return c+n*b**cd(n)
    else:
        return ConvertirABaseDiez(n//10,b,c+(n%10)*b**(cd(n)-(cd(n)-d)),d+1)
print (ConvertirABaseDiez(13,7,0,0))
print (ConvertirABase(37,3,0))


