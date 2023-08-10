import csv
import pandas as pd

# Function to read the spreadsheet which needs to be analyzed and stores the 'sales' in a List


def read_data():
    with open("./input_data/sales.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        sales_data = []
        months = []
        expenditure = []
        for row in spreadsheet:
            # sales_data.append(row)
            sales_data.append(int(row['sales']))
            months.append(row['month'])
            expenditure.append(row['expenditure'])
        # print(months)
        return sales_data, months, expenditure

# Function that displays the output


def print_data():
    sales_data = read_data()
    for row in sales_data:
        print(row)


# Function that calculates the total sales from Jan to Dec
def total_sales(sales_calc):
    # sales_calc = read_data()
    total_sale = sum(sales_calc)
    return total_sale

# Function that calculates the sales average

def avg_sales(sales_calc):
    avg_sale = total_sales(sales_calc)/12
    return avg_sale

# Function to determine the month which has the highest sale
def highest_sales(sales_calc, months):
    max_sale_value = max(sales_calc)
    max_sale_index = sales_calc.index(max(sales_calc))
    # print("Max sale amount: {}".format(max_sale_value))
    ## print("Index of maximum sale is: {}".format(max_sale_index))
    max_sale_month = months[max_sale_index].upper()
    # print("Month with maximum sale is: {}".format(max_sale_month))
    ## print("Month with maximum sale is: {}".format(months[max_sale_index].capitalize()))
    return max_sale_value, max_sale_month

# Function to determine the month which has the lowest sale
def lowest_sales(sales_calc, months):
    min_sale_value = min(sales_calc)
    min_sale_index = sales_calc.index(min(sales_calc))
    min_sale_month = months[min_sale_index].upper()
    return min_sale_value, min_sale_month


def monthly_profit():
    profits=[]
    sale=[]
    exp=[]

    with open("./input_data/sales.csv", "r") as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            profit = round((int(row['sales']) - int(row['expenditure']))*100/int(row['expenditure']),3)
            sale.append(int(row['sales']))
            exp.append(int(row['expenditure']))
            profits.append(profit)

    # print(sale)
    # print(exp)
    # print(profits)

    with open('./output_data/2018_profit.csv', 'w', encoding='utf-8', newline='') as write_csv:
        field_names = ['Sales', 'Expenditure', 'Profit']
        writer=csv.DictWriter(write_csv, fieldnames=field_names, delimiter=' ')
        writer.writeheader()
        writer = csv.writer(write_csv, delimiter=',')
        writer.writerows(zip(sale,exp,profits))

    # Using Pandas
    data = {'Sales': sale,
        'Expenditure': exp,
        'Profit': profits}
    df = pd.DataFrame.from_dict(data)
    df.to_csv('./output_data/out.csv', index = False)
