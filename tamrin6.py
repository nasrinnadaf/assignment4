first_number = int(input("put first number : "))
second_number = int(input("put second number : "))
for i in range (1 , first_number+1 ) :
        if first_number % i == 0 and second_number % i == 0 :
         bmm = i
print(bmm)