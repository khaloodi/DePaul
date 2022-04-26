
#Khaled Adad

def earnings(name, age, salary):
    total_earned = salary
    annual_rate = .055
    salary = salary
    age = age

    f = open('yearly_earnings.txt', 'a')

    print(f'Summary for {name}')
    print(f'Starting salary at age ${age} was ${salary:0,.2f}')
    print(f'Salary increases 5.5% per year')

    f.write("Prepared by: Khaled Adad")
    f.write("\nAge Salary Total") #print these values comma separated
    for i in range(age, 64):
        age+= 1
        salary *= 1+annual_rate
        total_earned +=salary

        
        f.write('\n{:3},{:.2f},{:.2f}'.format(age, salary, total_earned))

    print(f'Projected annual salary at age 64 is ${salary:0,.2f}')
    print(f'Projected accumulated earnings by age 65 is ${total_earned:0,.2f}')
        
print(earnings('Sally Sunshine', 30, 75000.00))
print("To view yearly data, go to yearly_earnings.txt")
print('Thank you for using the earnings() function.')