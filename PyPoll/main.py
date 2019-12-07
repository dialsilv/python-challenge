import os
import csv

# Path to collect data from the Resources folder
pool_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(pool_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')

    tracker = {}

    for row in csvreader:

        the_name = row['Candidate']

        if the_name in tracker:
            tracker[the_name] += 1
        else:
            tracker[the_name] = 1

total_votes = 0
winner_name = ''
winner_votes = 0

for name, votes in tracker.items():
    total_votes += votes
    if votes > winner_votes:
        winner_name = name
        winner_votes = votes

print(f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------""")
for name, votes in tracker.items():
    print(f'{name}: {"{:.3f}".format((votes/total_votes)*100)}% ({votes})')
print(f"""-------------------------
Winner: {winner_name}
-------------------------""")

# Specify the file to write to
output_path = os.path.join("main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # write in txtfile
    txtfile.write(str(f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    """))
    for name, votes in tracker.items():
        txtfile.write(str(f'{name}: {"{:.3f}".format((votes/total_votes)*100)}% ({votes}})\n    '))

    txtfile.write(str(f"""
    -------------------------
    Winner: {winner_name}
    -------------------------"""))



    # close txtfile
    txtfile.close()
