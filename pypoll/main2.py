#%%

import pandas as pd
df = pd.read_csv('D:/python challenge/python-challenge/pypoll/resources/election_data.csv')


# %%

total_votes = len(df)



candidate_votes = df['Candidate'].value_counts()

Diana = candidate_votes.iat[0]
Charles = candidate_votes.iat[1]
Raymon= candidate_votes.iat[2]

candidate_votes_percent = round(df['Candidate'].value_counts(normalize=True)*100,3)

Diana_perc = candidate_votes_percent.iat[0]
Charles_perc = candidate_votes_percent.iat[1]
Raymon_perc= candidate_votes_percent.iat[2]

#%%

data = (pd.DataFrame(candidate_votes)
            .reset_index()
            .rename(columns = {'index' : 'Candidate', 'Candidate' : "Votes"}))



# %%
winner = candidate_votes.max()

for i in range(len(data)):
    if data.iat[i,1] == winner:
        winner = (data.iat[i,0])
#%%



print('Election Results')
print('------------------------------------------------------------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------------------------------------------------------------')
print('Charles Casper Stockham: ' + str(Charles_perc) + '% (' + str(Charles) +')')
print('Diana DeGette: ' + str(Diana_perc) + '% (' + str(Diana) +')')
print('Raymon Anthony Doane: ' + str(Raymon_perc) + '% (' + str(Raymon) +')')
print('--------------------------------------------------------------------------------')
print('Winner: ' + str(winner))


        
# %%
import sys
sys.stdout = open('poll_results.txt', 'w')