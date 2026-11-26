
def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus


def employee_details(name, department, salary):
    return {
        "name": name,
        "department": department,
        "salary": salary
    }


employee = employee_details("Bhavesh", "DevOps", 25000)
total_salary = calculate_salary(employee["salary"], 5000)

print("Employee Management System")
print("--------------------------")
print("Employee:", employee["name"])
print("Department:", employee["department"])
print("Basic Salary:", employee["salary"])
print("Bonus:", 5000)
print("Total Salary:", total_salary)
