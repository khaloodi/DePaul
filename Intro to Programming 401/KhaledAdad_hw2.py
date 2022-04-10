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

# store input string and separate out characters
first_digit = int(number[0])
second_digit = int(number[1])
remaining_digits = int(number[2:])

# using a switch statement (more concise/readable), determine the membership type for output string
def membership_type(digit):
    switch = {
        1: "Standard adult membership",
        2: "Child (age 12 and under)",
        3: "Student",
        4: "Senior Citizen (age 65 and older)"
    }
    return switch.get(digit, "Enter a valid number for membership type")

# using a switch statement (more concise/readable), calculate the membership cost based on 1st character
def membership_cost(digit):
    switch = {
        1: 40,
        2: 20,
        3: 25,
        4: 30
    }
    return switch.get(digit)

# using a switch statement (more concise/readable), determine if there are optional services based on 2nd char
def optional_services(digit):
    switch = {
        0: "no lessons",
        1: "yoga lessons",
        2: "personal trainer",
        3: "yoga and personal trainer"
    }
    return switch.get(digit, "Enter a valid number for optional services type")

# using a switch statement (more concise/readable), cost of any optional services based on 2nd char
def optional_services_cost(digit):
    switch = {
        0: 0,
        1: 10,
        2: 50,
        3: 60
    }
    return switch.get(digit)

# use if statements to calculate the discount based on 3rd char, and store in variable discount_rate
if remaining_digits <=3:
    discount_rate = 0
elif remaining_digits <=6:
    discount_rate = 5/100
elif remaining_digits <= 9:
    discount_rate = 8/100
else:
    discount_rate = 10/100

# output what the user input on a new line
print(f"\n{membership_type(first_digit)} with {optional_services(second_digit)} for {remaining_digits} months")

# calculate monthly fee
monthly_fee_before_discount = membership_cost(first_digit) + optional_services_cost(second_digit)
discount = monthly_fee_before_discount * discount_rate
monthly_fee_after_discount = monthly_fee_before_discount - discount
# print(membership_cost(1))

# calculate total
total = monthly_fee_after_discount * remaining_digits

print(f"Monthly fee =: ${monthly_fee_after_discount:.2f}")
print(f"Total = ${total:.2f}")

# print the discount code for fun
print("Redeem your free drink at the juice bar using code: " + number)

'''
Test Case 1:

Enter number of membership type, services, number of months: 4312

Senior Citizen (age 65 and older) with yoga and personal trainer for 12 months
Monthly fee =: $81.00
Total = $972.00
Redeem your free drink at the juice bar using code: 4312

Test Case 2:

Enter number of membership type, services, number of months: 309

Student with no lessons for 9 months
Monthly fee =: $23.00
Total = $207.00
Redeem your free drink at the juice bar using code: 309
'''