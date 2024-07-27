def is_dream_package(salary):
    if salary > 500000:
        return "DREAM"
    else:
        return "NOTDREAM"

salary1 = 100000
salary2 = 600000

print(f"Input: {salary1}\nOutput: {is_dream_package(salary1)}")
print(f"Input: {salary2}\nOutput: {is_dream_package(salary2)}")
