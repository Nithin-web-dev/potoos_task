# employee_module.py

class Employee:
    def __init__(self, emp_id, name, salary):
        """
        Initialize an employee object
        """
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.bonus = 0.0

    def apply_bonus(self, percentage):
        """
        Apply bonus as a percentage of salary
        """
        self.bonus = (percentage / 100) * self.salary
        self.salary += self.bonus
        return self.salary

    def __str__(self):
        """
        String representation of the employee details
        """
        return f"{self.name} | Final Salary: {self.salary:.2f}"
