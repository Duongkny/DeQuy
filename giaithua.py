def GiaiThua(n):
    if(n==0):
        return 1
    else:
        return n*GiaiThua(n-1)
    
n=int(input('Nhap vao n : '))
print('Giai thua cua ', int(n) , ' = ' , GiaiThua(n))