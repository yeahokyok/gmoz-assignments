def is_palindrome(input):
    return input == input[::-1]


test_cases = [
    ("anna", True),
    ("level", True),
    ("radar", True),
    ("madam", True),
    ("abcdefg", False),
    ("abcdeedcba", True),
    ("hello", False),
]

for input, expected in test_cases:
    result = is_palindrome(input)
    assert result == expected, f"Input: {input}, Output: {result}, Expected: {expected}"
    print(f"Input: {input}, Output: {result}")
