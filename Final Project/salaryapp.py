from employee import Employee

def readData():
    employees = []
    infile = open("data.txt", 'r')
    for line in infile.readlines():
        tokens = line.split(";")
        employee = Employee(tokens[0], tokens[1], tokens[2], float(tokens[3]), float(tokens[4]))
        employees.append(employee)

    infile.close()
    return employees

def displayAll(employees):
    for employee in employees:
        print(employee)
        
def displaySalaryInfo(employees):
    total = 0.0
    for employee in employees:
        total += employee.getWeekSalary()

    print("Total Salary: {0:0.2f}".format(total))
    print("Average Salary: {0:0.2f}".format(total / len(employees)))

def displayHighestSalary(employees):
    highest = employees[0]
    for employee in employees[1:]:
        if employee.getWeekSalary() > highest.getWeekSalary():
            highest = employee
    print("Highest earning employee's name is {0} and the salary is ${1:0.2f}"\
        .format(highest.getFullName(), highest.getWeekSalary()))

def displayLowestSalary(employees):
    lowest = employees[0]
    for employee in employees[1:]:
        if employee.getWeekSalary() < lowest.getWeekSalary():
            lowest = employee
    print("Lowest earning employee's name is {0} and the salary is ${1:0.2f}"\
        .format(lowest.getFullName(), lowest.getWeekSalary()))

def sortEmployees(employees):
    employees.sort(key=lambda x: x.getWeekSalary(), reverse=True)
    displayAll(employees)
    
def main():
    employees = readData()
    displayAll(employees)
    displaySalaryInfo(employees)
    displayHighestSalary(employees)
    displayLowestSalary(employees)
    sortEmployees(employees)

if __name__ == "__main__":
    main()



















