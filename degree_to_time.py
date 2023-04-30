def degree_to_time(degree):
    half_day_minutes = 12 * 60
    minute_per_degree = half_day_minutes / 360
    minutes = degree * minute_per_degree

    clock_hours = minutes // 60
    clock_minutes = minutes % 60

    return f"{clock_hours:02.0f}:{clock_minutes:02.0f}"


test_cases = [
    (0, "00:00"),
    (28, "00:56"),
    (60, "02:00"),
    (180, "06:00"),
    (202, "06:44"),
    (300, "10:00"),
]

for input, expected in test_cases:
    result = degree_to_time(input)
    assert result == expected, f"Input: {input}, Output: {result}, Expected: {expected}"
    print(f"Input: {input}, Output: {result}")
