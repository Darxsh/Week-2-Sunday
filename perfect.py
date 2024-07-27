def is_perfect_number(number):
    if number < 1:
        return "NO"
    
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    
    if sum_of_divisors == number:
        return "YES"
    else:
        return "NO"

number1 = 1
number2 = 96345

print(f"Input: {number1}\nOutput: {is_perfect_number(number1)}")
print(f"Input: {number2}\nOutput: {is_perfect_number(number2)}")
