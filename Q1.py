def check_characters_present(str1, str2):
   
    set1 = set(str1)
    set2 = set(str2)

    if set1.issubset(set2):
        return "Yes"
    else:
        return "No"

T = int(input())
for _ in range(T):
    input_strings = input().split()
    result = check_characters_present(input_strings[0], input_strings[1])
    print(result)
