def calculate_salary(employee):
    base_salary = 50000
    bonus = employee.get('bonus', 0)
    return base_salary + bonus
