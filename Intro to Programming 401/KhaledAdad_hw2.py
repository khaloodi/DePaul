print("Membership Categories:")
print("1 Standard adult membership (40)")
print("2 Child (age 12 and under) (20)")
print("3 Student (25)")
print("4 Senior Citizen (30)")
print()

print("Optional Services:")
print("0 No lessons")
print("1 Yoga Lessons(10)")
print("2 Personal trainer(50)")
print("3 Yoga and Personal trainer(60)")
print()

print("Discount:")
print("0% Months 1-3")
print("5% Months 4-6")
print("8% Months 7-9")
print("10% Months 10 or more months")
print()

# print("Enter number of membership type, services, number of months:")
number = input("Enter number of membership type, services, number of months: ")

first_digit = int(number[0])
second_digit = int(number[1])
remaining_digits = int(number[2:])

def membership_type(digit):
    switch = {
        1: "Standard adult membership",
        2: "Child (age 12 and under)",
        3: "Student",
        4: "Senior Citizen (age 65 and older)"
    }
    return switch.get(digit, "Enter a valid membership type")

def membership_cost(digit):
    switch = {
        1: 40,
        2: 20,
        3: 25,
        4: 30
    }

print(f"{membership_type(first_digit)} with ")