
# import csv
import pandas as pd
df = pd.read_csv('D:/python challenge/python-challenge/pypoll/resources/election_data.csv')



# getting total number of votes cast
total_votes = len(df)


# calculating total number of votes each candidate won, using frequency table
candidate_votes = df['Candidate'].value_counts()

Diana = candidate_votes.iat[0]
Charles = candidate_votes.iat[1]
Raymon= candidate_votes.iat[2]

# calculating percentage of votes each candidate won, using a relative frequency table
candidate_votes_percent = round(df['Candidate'].value_counts(normalize=True)*100,3)

Diana_perc = candidate_votes_percent.iat[0]
Charles_perc = candidate_votes_percent.iat[1]
Raymon_perc= candidate_votes_percent.iat[2]


# converts frequency tabel to a data frame
data = (pd.DataFrame(candidate_votes)
            .reset_index()
            .rename(columns = {'index' : 'Candidate', 'Candidate' : "Votes"}))


# uses data frame to get winners name
winner = candidate_votes.max()

for i in range(len(data)):
    if data.iat[i,1] == winner:
        winner = (data.iat[i,0])


# prints results

print('Election Results')
print('------------------------------------------------------------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------------------------------------------------------------')
print('Charles Casper Stockham: ' + str(Charles_perc) + '% (' + str(Charles) +')')
print('Diana DeGette: ' + str(Diana_perc) + '% (' + str(Diana) +')')
print('Raymon Anthony Doane: ' + str(Raymon_perc) + '% (' + str(Raymon) +')')
print('--------------------------------------------------------------------------------')
print('Winner: ' + str(winner))


        
# writes results to a text file
import sys
sys.stdout = open('poll_results.txt', 'w')

print('Election Results')
print('------------------------------------------------------------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------------------------------------------------------------')
print('Charles Casper Stockham: ' + str(Charles_perc) + '% (' + str(Charles) +')')
print('Diana DeGette: ' + str(Diana_perc) + '% (' + str(Diana) +')')
print('Raymon Anthony Doane: ' + str(Raymon_perc) + '% (' + str(Raymon) +')')
print('--------------------------------------------------------------------------------')
print('Winner: ' + str(winner))
