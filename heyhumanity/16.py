def f(n):
    if n < 2: return 1
    if n >= 2 and n%2==0: return f(n/2) + 1
    if  n>= 2 and n%2!=0: return f(n-3) + 3
v = 0
for n in range(1,100000+1):
    if f(n) == 12:
        v+=1
print(v)