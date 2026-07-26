print("*** Payroll Calculation System ***")


emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))


if basic_salary >= 50000:
    allowance = basic_salary * 0.20      
elif basic_salary >= 30000:
    allowance = basic_salary * 0.15      
else:
    allowance = basic_salary * 0.10      


deduction = basic_salary * 0.05


gross_salary = basic_salary + allowance
net_salary = gross_salary - deduction


print("========== PAYROLL SLIP ==========")
print("Employee ID      :", emp_id)
print("Employee Name    :", emp_name)
print("Basic Salary     : ", basic_salary)
print("Allowance        : ", allowance)
print("Deduction        : ", deduction)
print("Gross Salary     : ", gross_salary)
print("Net Salary       : ", net_salary)
print("==================================")