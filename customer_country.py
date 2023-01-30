import csv

customers = open("customers.csv", "r")
customers2 = open("customer_country.csv", "a")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

for record in customer_file:

    lines = [
        "Name: ",
        record[1],
        " ",
        record[2],
        "\n",
        "Country:",
        " ",
        record[4],
        "\n",
        "\n",
    ]
    customers2.writelines(lines)

customers.close()
customers2.close()

f = open("customer_country.csv", "r")
print(f.read())
