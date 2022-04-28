first_number = int(input("put first number :"))
second_number = int(input("put second number :"))
for i in range ( second_number , first_number*second_number+1):
    if i % first_number == 0 and i % second_number ==0 :
        kmm = i
print(kmm)