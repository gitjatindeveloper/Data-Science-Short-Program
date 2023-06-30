# take a string as input and reverse string

# function to reverse the string
def check_reverse(string_1):
    reverse_string01 = string_1[::-1]
    return reverse_string01

str1 = input("Enter text here: ")
check_str1= check_reverse(str1)
print("The string", str1,"is reversed into", check_str1)