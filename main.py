# Importing all other code files
import read_input


def execute():
    sales_list = read_input.read_data()
    print("Sales list: {}".format(sales_list))
    # read_input.print_data()
    total_sales = read_input.total_sales()
    # total_sales = read_input.total_sales(sales_list)
    print("Total sales from January to December amounts to: {}".format(total_sales))
    avg_sales = read_input.avg_sales()
    print("Average sales per month: {}".format(int(avg_sales)))


# Executing the exec() function
execute()
