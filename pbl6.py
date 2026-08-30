employee = {}

while True:
    print("1. View Records")
    print("2. Add Employee")
    print("3. Remove Employee")
    print("4. Update Employee Details")
    print("5. Search Employee Details")
    print("6. Sort")
    print("7. Exit \n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(employee) == 0:
            print("No records present \n\n")

        else:
            print(employee)

    elif choice == 2:
        print("Enter Employee Details: \n")
        emp_id = int(input("Enter the ID of the employee "))

        if emp_id in employee:
            print("Employee ID already exists")

        else:
            name = input("Enter the name: ")
            department = input("Enter the Department name: ")
            designation = input("Enter the Designation: ")
            salary = float(input("Enter the salary: "))

            employee[emp_id] = {
                "Name": name,
                "Department": department,
                "Designation": designation,
                "Salary": salary
            }

    elif choice == 3:
        if len(employee) == 0:
            print("Empty list \n\n")

        else:
            e_id = int(input("Enter employee ID for deletion: "))
            if e_id in employee:
                employee.pop(e_id)

            else:
                print("Invalid ID \n")

    elif choice == 4:
        if len(employee) == 0:
            print("Empty list \n\n")

        else:
            e_id = int(input("Enter the ID for updation: "))
            if e_id in employee:
                name = input("\nEnter the name: ")
                department = input("Enter the Department name: ")
                designation = input("Enter the Designation: ")
                salary = float(input("Enter the De salary: "))

                employee[e_id] = {
                    "Name": name,
                    "Department": department,
                    "Designation": designation,
                    "Salary": salary
                }

            else:
                print("Invalid ID \n")

    elif choice == 5:
        if len(employee) == 0:
            print("Empty list \n\n")

        else:
            e_id = int(input("Enter the Employee ID: "))
            if e_id in employee:
                print(employee[e_id])

            else:
                print("Invalid ID \n")

    elif choice == 6:
        print("Choose from the following options: ")
        print("1. Sort by Name")
        print("2. Sort by Salary")
        print("3. Sort by Employee ID")
        print("4. Back\n")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            sorted_emp = sorted(employee.items(),
                                 key=lambda x: x[1]["Name"])

            print("\nEmployee sorted by Name: \n")
            for emp_id, details in sorted_emp:
                print("Employee ID: ", emp_id)
                print("Name: ", details["Name"])
                print("Department: ", details["Department"])
                print("Designation: ", details["Designation"])
                print("Salary: ", details["Salary"])
                print()

        elif choice == 2:
            sorted_emp = sorted(employee.items(),
                                 key=lambda x: x[1]["Salary"])

            print("\nEmployee sorted by Salary: \n")
            for emp_id, details in sorted_emp:
                print("Employee ID: ", emp_id)
                print("Name: ", details["Name"])
                print("Department: ", details["Department"])
                print("Designation: ", details["Designation"])
                print("Salary: ", details["Salary"])
                print()

        elif choice == 3:
            sorted_emp = sorted(employee.items(),
                                 key=lambda x: x[0])

            print("\nEmployees sorted by Employee ID: \n")
            for emp_id, details in sorted_emp:
                print("Employee ID: ", emp_id)
                print("Name: ", details["Name"])
                print("Department: ", details["Department"])
                print("Designation: ", details["Designation"])
                print("Salary: ", details["Salary"])
                print()

        elif choice == 4:
            continue

        else:
            print("Invalid choice\n")

    elif choice == 7:
        print("Exiting\n")
        break

    else:
        print("Invalid choice\n")