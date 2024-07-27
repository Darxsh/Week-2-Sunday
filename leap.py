def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Non Leap Year"

year1 = 1990
year2 = 2024

print(f"Input: {year1}\nOutput: {is_leap_year(year1)}")
print(f"Input: {year2}\nOutput: {is_leap_year(year2)}")
