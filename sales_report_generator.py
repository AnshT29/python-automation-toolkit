import csv

t_sales = 0
t_employees = 0

highest_sales = 0
highest_sales_employee = ""

lowest_sales = float("inf")
lowest_sales_employee = ""

with open("sample_data.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        t_sales += int(row[1])
        t_employees += 1

        current_employee = row[0]
        current_sales = int(row[1])

        if current_sales > highest_sales:
            highest_sales = current_sales
            highest_sales_employee = current_employee

        if current_sales < lowest_sales:
            lowest_sales = current_sales
            lowest_sales_employee = current_employee

average = t_sales / t_employees

with open("sales_report.txt", "w") as file:
    file.write("Sales Report\n")
    file.write("============\n")

    file.write(f"Total Sales: {t_sales}\n")
    file.write(f"Total Employees: {t_employees}\n")
    file.write(f"Average Sales: {average}\n\n")

    file.write(f"Highest Sales Employee: {highest_sales_employee}\n")
    file.write(f"Highest Sales: {highest_sales}\n\n")

    file.write(f"Lowest Sales Employee: {lowest_sales_employee}\n")
    file.write(f"Lowest Sales: {lowest_sales}\n")

print(f"Total Sales: {t_sales}")
print(f"Total Employees: {t_employees}")
print(f"Average Sales: {average}")

print()

print(f"Highest Sales Employee: {highest_sales_employee}")
print(f"Highest Sales: {highest_sales}")

print()

print(f"Lowest Sales Employee: {lowest_sales_employee}")
print(f"Lowest Sales: {lowest_sales}")
