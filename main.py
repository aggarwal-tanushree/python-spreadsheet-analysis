# Importing all other code files
import read_input


def execute():
    sales_list,month_list, exp_list = read_input.read_data()
    print("Sales list: {}".format(sales_list))
    # print("Expenditure list: {}".format(exp_list))
    # read_input.print_data()
    # total_sales = read_input.total_sales()
    total_sales = read_input.total_sales(sales_list)
    print("Total sales from January to December amounts to: {}".format(total_sales))
    # avg_sales = read_input.avg_sales()
    avg_sales = read_input.avg_sales(sales_list)
    print("Average sales per month: {}".format(int(avg_sales)))

    # month with max sale
    highest_sale, highest_sale_month = read_input.highest_sales(sales_list, month_list)
    print("Month with highest sale is {} with sale amounting to: {}".format(highest_sale_month, highest_sale))

    # month with min sale
    lowest_sale, lowest_sale_month = read_input.lowest_sales(sales_list, month_list)
    print("Month with lowest sale is {} with sale amounting to: {}".format(lowest_sale_month, lowest_sale))


    # calculating monthly profit
    read_input.monthly_profit()


# Executing the exec() function
execute()
