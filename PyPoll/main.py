import os
import csv

# importing election data
election_data = []

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Header
    csv_header = next(csv_reader)

    for row in csv_reader:
        election_data.append(row)

# total votes by counting number of rows
total_v = len(election_data)

# funtion that find the count of votes a candidate got in the election
def count_votes(name, data = election_data):
    count = 0
    for row in data:
        if row[2] == name:
            count = count + 1
    return(count)

# function that finds the percent of total votes a candidate recieved
def perc(count):
    perc = str(round((count /  total_v) * 100, 3))
    return(perc)

# count for each candidate
stock_count = count_votes(name = "Charles Casper Stockham")
degette_count = count_votes(name = "Diana DeGette")
doane_count = count_votes(name = "Raymon Anthony Doane")

# finding winner based on who has most votes
if stock_count > degette_count and stock_count > doane_count:
    winner = "Charles Casper Stockham"
elif degette_count > doane_count:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"


election_results = [
    "Election Results",
    "-------------------------",
    "Total Votes: " + str(total_v),
    "-------------------------",
    "Charles Casper Stockham: " + str(perc(stock_count)) + "%" + " (" + str(stock_count)  + ")",
    "Diana DeGette: " + str(perc(degette_count)) + "%" + " (" + str(degette_count) + ")",
    "Raymon Anthony Doane: " + str(perc(doane_count)) + "%" + " (" + str(doane_count) + ")",
    "-------------------------",
    "Winner: " + str(winner),
    "-------------------------"
]

# printing and export method found on ChatGBT
print('\n'.join(election_results))
 
with open('election_result.txt', 'w') as file:
    for result in election_results:
       file.write(result + '\n')
