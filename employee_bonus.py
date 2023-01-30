import csv

employee_pay = open("EmployeePay.csv", "r")


employee_file = csv.reader(employee_pay, delimiter=",")

next(employee_file)

for record in employee_file:

    print("Name:", record[1], record[2])
    print("ID:", record[0])
    print("Salary:", record[3])
    print("Bonus:", record[4], "\n")
