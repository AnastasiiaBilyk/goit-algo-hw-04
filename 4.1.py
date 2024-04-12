path = 'C:\Projects\My_repo\goit-algo-hw-04\salary_file.txt'

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print('файл не знайдено')

    average_salary = int(total / count)
    return total, average_salary

result = total_salary(path)

if result:
    total, average = result
    print(f"Загальна сума зарплат: {total}")
    print(f"Середня зарплата: {average}")
