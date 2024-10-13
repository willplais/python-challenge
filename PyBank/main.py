# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

month_month_changes = []
previous_month_profit = 0

# Add more variables to track other necessary financial data
greatest_month = {
    "month": "",
    "adjustment": 0
}
weakest_month = {
    "month": "",
    "adjustment": 0
}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        month_net = int(row[1])

        # Track the net change
        total_net = total_net + month_net

        if total_months > 1:
            print(f"{month_net} - {previous_month_profit}")
            month_change = (month_net - previous_month_profit)
            print(month_change)
            month_month_changes.append(month_change)

            # Calculate the greatest increase in profits (month and amount)
            if greatest_month["adjustment"] < month_change:
                greatest_month["month"] = row[0]
                greatest_month["adjustment"] = month_change

            # Calculate the greatest decrease in losses (month and amount)
            if weakest_month["adjustment"] > month_change:
                weakest_month["month"] = row[0]
                weakest_month["adjustment"] = month_change
        
        previous_month_profit = month_net



# Calculate the average net change across the months
# avg_net = round(float(total_net / total_months), 2)
# print(f"{month_month_changes}")
avg_net = sum(month_month_changes) / len(month_month_changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${round(avg_net, 2)}\n"
    f"Greatest Increase in Profits: {greatest_month["month"]} (${greatest_month["adjustment"]})\n"
    f"Greatest Decrease in Profits: {weakest_month["month"]} (${weakest_month["adjustment"]})\n"
)

# Print the output
print(f"{output}")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"{output}")
