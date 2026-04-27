def sumDigits(num):
    total=0
    while(num>0):
        total+=num%10
        num//=10
    
    return total

n=int(input())

meet = False
startSearch = max(1,n-50) # Because of the constraints (1<=n<=100000)
# Then the maximum of sum digits will be 9+9+9+9+9 or 45 before touching the constraints limit
# In this case, just set it to 50 (or more)

for x in range(startSearch,n):
    if(x+sumDigits(x)==n):
        meet = True
        break

if meet:
    print("YES")
else:
    print("NO")