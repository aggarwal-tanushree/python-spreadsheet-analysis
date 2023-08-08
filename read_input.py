import csv

# Function to read the spreadsheet which needs to be analyzed and stores the 'sales' in a List


def read_data():
    with open("./input_data/sales.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales_data = []
        months = []
        for row in spreadsheet:
            # sales_data.append(row)
            sales_data.append(int(row['sales']))
            months.append(row['month'])
        # print(months)
        return sales_data

# Function that displays the output


def print_data():
    sales_data = read_data()
    for row in sales_data:
        print(row)


# Function that calculates the total sales from Jan to Dec
def total_sales():
    sales_calc = read_data()
    total_sale = sum(sales_calc)
    return total_sale

# Function that calculates the sales average


def avg_sales():
    avg_sale = total_sales()/12
    return avg_sale

# Function to determine the month which has the highest sale
# def highest_sales():
# max_sale_value=

# Function to determine the month which has the lowest sale
# def lowest_sales():
