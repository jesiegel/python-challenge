import os
import csv

# importing budget data
budget_data = []

csvpath = os.path.join('budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)

    for row in csv_reader:
        budget_data.append(row)


# total number of months
total_m = len(budget_data)


### finding net total form profit/losses
# profit/losses column needs to be converted in integer
total_sum = sum(int(row[1]) for row in budget_data)


### finding average change in profit/losses
# array to store the difference values between each month
diffs = []
# for loop that takes the current ith month minue the previous month 
# and stores value in array
for i in range(1, total_m):
    diff = int(budget_data[i][1]) - int(budget_data[i - 1][1])
    diffs.append(diff)
# average of those differences
avg_change = round(sum(diffs)/len(diffs), 2)


### Finding greatest increase in profits
# s is the previous profit/loss and gi is the greatest increase value
s = 0
gi = 0
# loop to find greatest increase
for i in range(total_m):
    # difference between current ith value minus previous value
    dif = int(budget_data[i][1]) - s
    # dif is greater than gi, set dif as new gi
    if dif > gi:
        gi = dif
        date1 = budget_data[i][0]
    s = int(budget_data[i][1])

### Finding greatest decrease in profits
# gd is the greatest decrease value
s = 0
gd = 0
# loop to find greatest decrease
for i in range(len(budget_data)):
    # difference between current ith value minus previous value
    dif = int(budget_data[i][1]) - s
    # dif is greater than gi, set dif as new gd
    if dif < gd:
        gd = dif
        date2 = budget_data[i][0]
    s = int(budget_data[i][1])

# results array
budget_results = [
    "Financial Analysis",
    "----------------------------",
    "Total Months: " + str(total_m),
    "Total: $" + str(total_sum),
    "Average Change: $" + str(avg_change),
    "Greatest Increase in Profits: " + str(date1) + " ($" + str(gi) + ")",
    "Greatest Decrease in Profits: " + str(date2) + " ($" + str(gd) + ")"
    ]

# printing and export method found on ChatGBT
print('\n'.join(budget_results))

with open('budget_result.txt', 'w') as file:
    for result in budget_results:
       file.write(result + '\n')
