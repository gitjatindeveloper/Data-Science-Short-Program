# check palendrome from user input

string1 = input("enter your text: ")
reversestring1 = string1[::-1]

if string1 == reversestring1:
    print("The", string1,"and", reversestring1,"is palendrome")
else:
    print("The", string1,"and", reversestring1,"is not palendrome")