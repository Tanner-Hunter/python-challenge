#%%
from http.client import GATEWAY_TIMEOUT
import pandas as pd
df = pd.read_csv("D:/python challenge/python-challenge/pybank/resources/budget_data.csv")

# %%

# calculating total number if months in the dataset.
total_months = len(df)


# %%
total = df['Profit/Losses'].sum()

# %%

changes = []

for x in range(len(df) - 1):
    numchange = df.iat[x + 1,1] - df.iat[x , 1]
    changes.append(numchange)

mean = round(sum(changes) / len(changes), 2)   

# %%
changes = [0] + changes
df['changes'] = changes

# %%
df['changes'] = changes
# %%
gip = 0
for x in range(len(df)):
    if df.iat[x, 2] > gip:
        gip = df.iat[x, 2]
        date = df.iat[x, 0]
    else: gip = gip

# %%
gdp = 0
for x in range(len(df)):
    if df.iat[x, 2] < gdp:
        gdp = df.iat[x, 2]
        date2 = df.iat[x, 0]
    else: gdp = gdp
 #%%


print('Financial Analysis')
print('-----------------------------------------')

print('total months: ' + str(total_months))
print('total: $' + str(total))
print('average change: $' + str(mean))
print('Greatest Increase in Profits: ' + str(date)  +' ($'+ str(gip) + ')')
print('Greatest Decrease in Profits: ' + str(date2) +' ($'+  str(gdp) + ')')
# %%
import sys
sys.stdout = open('bank_results.txt', 'w') 