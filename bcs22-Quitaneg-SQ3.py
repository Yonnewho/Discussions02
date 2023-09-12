#write a python program that will compute for the bonus using the specification stated

print("Welcome")

salary = int(input("salary: "))
years_of_service = int(input("Years of service: "))

running_time = 1
n = 1

if years_of_service == 5:
    running_time += 1
    if n != 0:
        running_time += 1
        bonus = salary * (5 / 100)
        amount = bonus + salary
        print(f'You have 5% Bonus {amount}')

elif years_of_service == 10:
    running_time += 1
    if n != 0:
        running_time += 1
        bonus = salary * (10 / 100)
        amount = bonus + salary
        print(f'You have 100% Bonus {amount}')

elif years_of_service == 15:
    running_time += 1
    if n != 0:
        running_time += 1
        bonus = salary * (15 / 100)
        amount = bonus + salary
        print(f'You have 150% Bonus {amount}')

elif years_of_service == 20:
    running_time += 1
    if n != 0:
        running_time += 1
        bonus = salary * (20 / 100)
        amount = bonus + salary
        print(f'You have 200% Bonus {amount}')

else:
    running_time += 1
    print('No Bonus...')

print(f'Running Time Complexity: {running_time}(n)')
