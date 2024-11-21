def Thap(n,a,b,c):
    if(n==1):
        print('Chuyen dia ',n,' tu ', a,' ====> ',c)
        return
    else:
        Thap(n-1,a,c,b)
        print('Chuyen dia ',n,' tu ', a,' ====> ',c)
        Thap(n-1,b,a,c)

n=int(input('Nhap so dia : '))
a='A'
b='B'
c='C'
Thap(n,a,b,c)