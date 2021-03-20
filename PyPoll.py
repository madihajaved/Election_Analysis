# Add our dependencies  
import csv 
import os 

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to direct or indirect path 
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize vote counter
total_votes = 0

# Candidate options
candidate_options = []

# declare eempty dictionary 
candidate_votes = {}

# winning candidate and winning count tracker 
winning_candidate =  ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file 
with open(file_to_load) as election_data:

    # To do: read and analyze data here 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    
    # Read the header row 
    headers = next(file_reader)
    
    # Print each row 
    for row in file_reader:
        # 2. Add to the total vote count 
        total_votes += 1

        # Print the candidate name from each row 
        candidate_name = row [2]

        # If the name does not match existing candidate 
        if candidate_name not in candidate_options:
            # Add name to candidate list 
            candidate_options.append(candidate_name) 

            # Begin tracking candidate votes within the dictionary 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count 
        candidate_votes[candidate_name] += 1       

# Save the results to our text file
with open(file_to_save, "w") as txt_file:   
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")

    # Save the final count to the text file 
    txt_file.write(election_results)           

    # Determine the percentage of votes for each candidate by looping through the counts
    # 1. Iterate through the list 
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of each candidate 
        votes = candidate_votes[candidate_name]
        # 3. Calculate percentage of votes 
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print each candidate, their voter count, and percentage 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Save the results to our text file 
        txt_file.write(candidate_results)

        # Determine winning count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"_______________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"_______________________\n")

    print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file 
    txt_file.write(winning_candidate_summary)


# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# A complete list of candidates who received votes 

# The percentage of votes each candidate won 

# The total number of votes each candidate won 

# The winner of the election based on popular vote 

