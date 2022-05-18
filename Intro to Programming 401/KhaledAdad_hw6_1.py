# Khaled Adad
# HW 6 Problem 1

def phone_number_formatter(phone_number):
    return f'{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:10]}'

def contacts():
    first_name = input('Enter first name: ')
    if first_name == '' or ' ' in first_name:
            return None
    last_name = input('Enter last name: ')
    if last_name == '' or ' ' in last_name:
            return None
    phone_number = input('Enter 10-digit phone number 9999999999: ')
    if phone_number == '' or ' ' in phone_number:
            return None

    contacts = []
    contacts.append((first_name, last_name, {phone_number_formatter(phone_number)}))
    phone_book = {(contacts[0][1], contacts[0][0]): contacts[0][2]}

    while contacts:
        first_name = input('Enter first name: ')
        if first_name == '' or ' ' in first_name:
            break
        last_name = input('Enter last name: ')
        if last_name == '' or ' ' in last_name:
            break
        phone_number = input('Enter 10-digit phone number 9999999999: ')
        if phone_number == '' or ' ' in phone_number:
            break

        if ((last_name, first_name) not in phone_book.keys()):
            # contacts.append((first_name, last_name, {phone_number_formatter(phone_number)}))
            phone_book[(last_name, first_name)] = {phone_number_formatter(phone_number)}

        if ((last_name, first_name) in phone_book.keys()):
            phone_book[(last_name, first_name)].add(phone_number_formatter(phone_number))

    print()

    output = f'Contact Dictionary\n'

    for key, value in sorted(phone_book.items()):
        output += f'{key[0]}, {key[1]} {value} \n'

    return output

print(contacts())