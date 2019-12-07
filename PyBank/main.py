import os
import csv


# Define the function and have it accept the 'records' as its sole parameter
#def print_records():

# Path to collect data from the Resources folder
bank_csv = os.path.join('', 'budget_data.csv')

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    first_row = next(csvreader)

    # Define local variables with value from first row to collect the information needed
    count_months = 1
    net_sum = int(first_row[1])
    greatest_increase_value = int(first_row[1])
    greatest_increase_month = first_row[0]
    greatest_decrease_value = int(first_row[1])
    greatest_decrease_month = first_row[0]
    profit_losses_last_month = int(first_row[1])
    delta = 0
    delta_cum = 0


    # Loop through the data
    for row in csvreader:

        # Keep counting the Months
        count_months += 1
        # Add to the net sum of profits/Losses
        net_sum += int(row[1])
        # Check if there is a higher increase/decrease in profit than the one stored
        delta = int(row[1]) - int(profit_losses_last_month)
        delta_cum = delta_cum + delta

        #higher increase
        if delta > greatest_increase_value:
            greatest_increase_month = row[0]
            greatest_increase_value = delta

        #higher decrease
        elif delta < greatest_decrease_value:
            greatest_decrease_month = row[0]
            greatest_decrease_value = delta

        profit_losses_last_month = row[1]

    # Calculate the Average changes
    average_changes = round(delta_cum / (count_months - 1),2)

    # Print the final information
    print(f"""
        Financial Analysis
        ----------------------------
        Total Months: {count_months}
        Total: ${net_sum}
        Average  Change: ${average_changes}
        Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})
        Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})
        """)


# Specify the file to write to
output_path = os.path.join("main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # write in txtfile
    txtfile.write(str(f"""
        Financial Analysis
        ----------------------------
        Total Months: {count_months}
        Total: ${net_sum}
        Average  Change: ${average_changes}
        Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_value})
        Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_value})
        """))



    # close txtfile
    txtfile.close()
