string = input("Enter a string: ")
string = string.lower()  # Convert the string to lowercase for case-insensitive comparison
is_palindrome = True

length = len(string)
for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
