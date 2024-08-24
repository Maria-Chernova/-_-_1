from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
def main():
    employees = get_employees()
    for employee in employees:
        salary = calculate_salary(employee)
        print(f"Employee: {employee['name']}, Salary: {salary}")
    now = datetime.now()
    print(f"Текущая дата: {now.strftime('%d.%m.%Y')}")

if __name__ == "__main__":
    main()

