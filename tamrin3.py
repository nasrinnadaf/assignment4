def multi_table (m, n):
    for i in range (1 , m+1):
        for j in range (1 , n +1):
            print(i*j, end = " ")
            if (j == n):
                print()
first_number= int(input("put first number : "))
second_number = int(input("put second number :"))
multi_table(first_number,second_number)