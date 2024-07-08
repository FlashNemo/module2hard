n = int(input())
password = ''

for i in range(1,n+1):
    for j in range(i+1,n):
        if n % (i + j ) == 0:
            password += str(i)
            password += str(j)
print(password)