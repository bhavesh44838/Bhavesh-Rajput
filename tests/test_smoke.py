
from app import calculate_salary, employee_details


def test_calculate_salary():
    result = calculate_salary(25000, 5000)
    assert result == 30000


def test_employee_details():
    employee = employee_details("Bhavesh", "DevOps", 25000)

    assert employee["name"] == "Bhavesh"
    assert employee["department"] == "DevOps"
    assert employee["salary"] == 25000
