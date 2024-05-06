import datetime

import application.salary as salary
import application.db.people as people

def main():
    current_date = datetime.datetime.now()
    print(f'Текущая дата: {current_date}')
    salary.calculate_salary()
    people.get_employees()

if __name__ == '__main__':
    main()

