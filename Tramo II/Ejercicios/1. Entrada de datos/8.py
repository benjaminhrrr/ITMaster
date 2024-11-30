value_hours = float(input('Ingrese valor monetario por hora de trabajo: '))
hours_per_day = float(input('Ingrese cantidad de horas trabajadas: '))

WEEK_DAYS = 5

weekly_salary = value_hours * hours_per_day * WEEK_DAYS
saturday_salary = value_hours * hours_per_day / 2
total_salary = weekly_salary + saturday_salary

print(f'Salario total: {total_salary}')
