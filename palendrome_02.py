# check the palendrome

string_01 = input("Enter text: ")
reverse_01 = string_01[::-1]

if reverse_01 == string_01:
    print(string_01 ,"is palendrome")
else:
    print(string_01 ,"is not palendrome")