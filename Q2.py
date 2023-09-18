n = int(input("Enter a number n: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = (num % n) + 1
    print()