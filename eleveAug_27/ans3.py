def fact(num):
    f = 1
    for i in range(1,num + 1):
        f *= i
    print(f)
n = int(input("Enter a number : ")) 
fact(n)       