def is_palindrome(input):
    return input == input[::-1]


print(is_palindrome("anna"))
print(is_palindrome("level"))
print(is_palindrome("radar"))
print(is_palindrome("madam"))
print(is_palindrome("abcdefg"))
print(is_palindrome("abcdeedcba"))
print(is_palindrome("hello"))
