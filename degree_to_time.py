def degree_to_time(degree):
    half_day_minutes = 12 * 60
    minute_per_degree = half_day_minutes / 360
    minutes = degree * minute_per_degree

    clock_hours = minutes // 60
    clock_minutes = minutes % 60

    return f"{clock_hours:02.0f}:{clock_minutes:02.0f}"


print(degree_to_time(0))
print(degree_to_time(28))
print(degree_to_time(60))
print(degree_to_time(180))
print(degree_to_time(202))
print(degree_to_time(300))
print(degree_to_time(345))
