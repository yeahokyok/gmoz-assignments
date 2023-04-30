import re


def length_longest_substring_without_repeating_characters(input):
    # input = re.sub(r"[^a-zA-Z]", "", input)
    left, right = 0, 0
    longest_length = 0
    unique_chars = set()

    while right < len(input):
        if input[right] not in unique_chars:
            unique_chars.add(input[right])
            longest_length = max(longest_length, len(unique_chars))
            right += 1
        else:
            unique_chars.remove(input[left])
            left += 1

        # print(
        #     f"char: {input[right-1]} left: {left} right: {right} set: {unique_chars}  'longest_length:' {longest_length}"
        # )

    return longest_length


test_cases = [
    ("pwwkew", 3),
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("", 0),
    (
        """aaaaaabbbbbbbbbbbbbcccccccc
abcdefgh
aabbccddee
aaaaccccddddd
abcdefgabcdefgh
bbbbcccccccccccccbbbbbb
aaaaaaaaaaaaaaa
abbbbbbbbbbbaaaaaa""",
        8,
    ),
]

for input, expected in test_cases:
    result = length_longest_substring_without_repeating_characters(input)
    assert result == expected, f"Input: {input}, Output: {result}, Expected: {expected}"
    print(f"Input: {input}, Output: {result}")
