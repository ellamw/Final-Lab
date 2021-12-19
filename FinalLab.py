def EmployeeID():
   
    # Employee ID - required
    # must be 7 digits or less
    ID = input("\nREQUIRED - Enter the employee's ID: ")
    
    while len(ID) > 7:
        print("Can not have more than 8 characters. Try again.")
        ID = input("REQUIRED - Enter the employee's ID: ")

    return ID


def EmployeeName():

    # Employee Name - required 
    # upper/lowercase letters, spaces, the ' character, and the - character
    Name = input("REQUIRED - Enter the employee's name: ")

    while Name.isalpha() == False:
        print("This is not a valid name. Try again.")
        Name = input("Enter the employee's name: ")

    return Name


def EmployeeEmail():

    while True:
    
        # Employee Email Address - required
        # alphanumeric characters, and can NOT contain any of the following: ! " ' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \
        Email = input("REQUIRED - Enter the employee's email address: ")

        if len(set("!'#$%^&*()=+,<>/?;:[]{}\"").intersection(set(Email))) > 0:
            print("Not a valid email address. Try again.")
            Email = input("Enter the employee's email address: ")
        else: 
            break

    return Email

            
def EmployeeAddress():

    # Employee Address - not required
    # alphanumeric characters, and can NOT contain any of the following: ! " ' @ $ % ^ & * _  = + < >  ? ; : [ ] { } 
    decision = input("OPTIONAL - Do you wish to provide the employee's address? ")
    if decision == "yes":
        while True:
            Address = input("Enter the employee's address: ")
            if len(set("!'@$%^&*_ =+<>?;:[]{}").intersection(set(Address))) > 0:
                print("Not a valid address. Try again.")
                Address = input("Enter the employee's address: ")
            else:
                break
    else:
        Address = "Employee address has not been provided"

    return Address


def EmployeeSalary():

    # Employee Salary - required
    # floating point number between 18 and 27
    Salary = float(input("REQUIRED - Enter the employee's salary: "))
    if Salary > 27 or Salary < 18:
        print("Not a valid salary. Try again.")
        Salary = float(input("Enter the employee's salary: "))

    return Salary







employeeList = list()
while True:
    ID = EmployeeID()
    Name = EmployeeName()
    Email = EmployeeEmail()
    Address = EmployeeAddress()
    Salary = EmployeeSalary()

    employeeInfo = {
        "ID": ID,
        "Name": Name,
        "Email": Email,
        "Address": Address,
        "Salary": Salary
    }

    employeeList.append(employeeInfo)

    moreEmployees = input("\nDo you want to enter more employees? ")
    if moreEmployees == "no":
        break

for employeeInfo in employeeList:
    employeeInfo["Name"] = "IT Department " + employeeInfo["Name"]
    employeeInfo["Salary"] = employeeInfo["Salary"] * 1.3

print("\n", employeeList)