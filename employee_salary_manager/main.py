# main.py

from salary_utils import fetch_employees, post_salary_update

def main():
    # Bonus percentage
    bonus_percentage = 10  

    # Fetch employees (GET request)
    employees = fetch_employees()

    # Process each employee
    for emp in employees:
        emp.apply_bonus(bonus_percentage)
        print(emp)  # Print report
        post_salary_update(emp)  # POST update


if __name__ == "__main__":
    main()
