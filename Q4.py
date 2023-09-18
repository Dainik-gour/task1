def shortest_initial_string(s):
    length = len(s)
    
    if length == 1:
        return 1
    elif length % 2 == 0:
        return 0
    else:
        return 3

T = int(input("Enter the number of test cases: "))

for _ in range(T):
    s = input().strip()
    result = shortest_initial_string(s)
    print(result)







