# -*- coding: UTF-8 -*-

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0 
candidates = []
candidate_votes = []

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if any(candidate_name in candidate for candidate in candidates):
            candidate_index = candidates.index(candidate_name)
            candidate_votes[candidate_index]["votes"] += 1
        else:
            candidates.append(candidate_name)
            candidate_votes.append({
                "name": candidate_name,
                "votes": 1
            })

# print(f"{candidate_votes}")

print("\n")
candidate_summary = ""
winning_candidate = ""
winning_votes = 0

for candidate in candidate_votes:
    candidate_summary = f"{candidate_summary}{candidate["name"]}: {round((candidate["votes"] / total_votes) * 100, 3)}% ({candidate["votes"]})\n"
    if candidate["votes"] > winning_votes:
        winning_candidate = candidate["name"]
        winning_votes = candidate["votes"]

# Generate the output summary
output = (
    f"Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n{candidate_summary}"
    f"----------------------------\nWinner: {winning_candidate}\n"
    "----------------------------\n"
)

# Print the output
print(f"{output}")

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"{output}")
