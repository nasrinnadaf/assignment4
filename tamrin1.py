def chest_sheet(m, n):
    for i in range (n):
        for j in range(m):
            if (i+j)%2==0:
                print('*',end="")
            else : 
                print('#',end="")
        print("\n")
n = int(input("put num= n:"))
m = int(input("put num= m"))
chest_sheet(m,n)