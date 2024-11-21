def fi(n):
    if(n<=2):
        return 1
    else:
        return fi(n-2) + fi(n-1)
    
n=int(input('Nhap vao n : '))
print('fibonaci cua ', n,' = ' ,fi(n))