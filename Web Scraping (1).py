#!/usr/bin/env python
# coding: utf-8

# In[70]:


from bs4 import BeautifulSoup
import requests


# In[71]:


url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')  


# In[73]:


soup.find_all('div')


# In[74]:


table = soup.find_all('div')[25]


# In[75]:


print(table)


# In[76]:


world_titles = soup.find_all('th')


# In[77]:


world_titles


# In[78]:


world_table_titles = [title.text for title in world_titles]
print(world_table_titles)


# In[79]:


# Remove the last three elements
world_table_titles= world_table_titles[:-4]


# In[80]:


print(world_table_titles)


# In[81]:


import pandas as pd


# In[82]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[87]:


column_data = table.find_all('tr')


# In[89]:


for row in column_data:
    row_data = row.find_all('td')
    print(row_data)


# In[98]:


for row in column_data:
    row_data = row.find_all('td')
    row_text = [td.get_text(strip=True) for td in row_data]
    print(row_text)


# In[100]:


import pandas as pd
import matplotlib.pyplot as plt

# Define column titles
world_table_titles = ['Party', 'Won', 'Leading', 'Total']

# Create an empty DataFrame
df = pd.DataFrame(columns=world_table_titles)

# Data extracted from the HTML table
data = [
    ['Bharatiya Janata Party - BJP', '240', '0', '240'],
    ['Indian National Congress - INC', '99', '0', '99'],
    ['Samajwadi Party - SP', '37', '0', '37'],
    ['All India Trinamool Congress - AITC', '29', '0', '29'],
    ['Dravida Munnetra Kazhagam - DMK', '22', '0', '22'],
    ['Telugu Desam - TDP', '16', '0', '16'],
    ['Janata Dal  (United) - JD(U)', '12', '0', '12'],
    ['Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT', '9', '0', '9'],
    ['Nationalist Congress Party – Sharadchandra Pawar - NCPSP', '8', '0', '8'],
    ['Shiv Sena - SHS', '7', '0', '7'],
    ['Lok Janshakti Party(Ram Vilas) - LJPRV', '5', '0', '5'],
    ['Yuvajana Sramika Rythu Congress Party - YSRCP', '4', '0', '4'],
    ['Rashtriya Janata Dal - RJD', '4', '0', '4'],
    ['Communist Party of India  (Marxist) - CPI(M)', '4', '0', '4'],
    ['Indian Union Muslim League - IUML', '3', '0', '3'],
    ['Aam Aadmi Party - AAAP', '3', '0', '3'],
    ['Jharkhand Mukti Morcha - JMM', '3', '0', '3'],
    ['Janasena Party - JnP', '2', '0', '2'],
    ['Communist Party of India  (Marxist-Leninist)  (Liberation) - CPI(ML)(L)', '2', '0', '2'],
    ['Janata Dal  (Secular) - JD(S)', '2', '0', '2'],
    ['Viduthalai Chiruthaigal Katchi - VCK', '2', '0', '2'],
    ['Communist Party of India - CPI', '2', '0', '2'],
    ['Rashtriya Lok Dal - RLD', '2', '0', '2'],
    ['Jammu & Kashmir National Conference - JKN', '2', '0', '2'],
    ['United People’s Party, Liberal - UPPL', '1', '0', '1'],
    ['Asom Gana Parishad - AGP', '1', '0', '1'],
    ['Hindustani Awam Morcha (Secular) - HAMS', '1', '0', '1'],
    ['Kerala Congress - KEC', '1', '0', '1'],
    ['Revolutionary Socialist Party - RSP', '1', '0', '1'],
    ['Nationalist Congress Party - NCP', '1', '0', '1'],
    ['Voice of the People Party - VOTPP', '1', '0', '1'],
    ['Zoram People’s Movement - ZPM', '1', '0', '1'],
    ['Shiromani Akali Dal - SAD', '1', '0', '1'],
    ['Rashtriya Loktantrik Party - RLTP', '1', '0', '1'],
    ['Bharat Adivasi Party - BHRTADVSIP', '1', '0', '1'],
    ['Sikkim Krantikari Morcha - SKM', '1', '0', '1'],
    ['Marumalarchi Dravida Munnetra Kazhagam - MDMK', '1', '0', '1'],
    ['Aazad Samaj Party (Kanshi Ram) - ASPKR', '1', '0', '1'],
    ['Apna Dal (Soneylal) - ADAL', '1', '0', '1'],
    ['AJSU Party - AJSUP', '1', '0', '1'],
    ['All India Majlis-E-Ittehadul Muslimeen - AIMIM', '1', '0', '1'],
    ['Independent - IND', '7', '0', '7']
]

# Add the data to the DataFrame
for row in data:
    df.loc[len(df)] = row

# Convert numerical columns to integers
df['Won'] = df['Won'].astype(int)
df['Leading'] = df['Leading'].astype(int)
df['Total'] = df['Total'].astype(int)

# Display the DataFrame
print(df)




# In[95]:



print("Top 5 parties by total seats won:")
print(df.sort_values(by='Total', ascending=False).head(5))


# In[108]:


# 1. Bar Chart for Total Seats Won by Each Party
plt.figure(figsize=(10, 8))
plt.barh(df['Party'], df['Total'], color='skyblue')
plt.xlabel('Total Seats Won')
plt.title('Total Seats Won by Each Party')
plt.gca().invert_yaxis()
plt.show()


# In[106]:


# 2. Pie Chart for Seat Distribution of Top 5 Parties
top_5_parties = df.head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_5_parties['Total'], labels=top_5_parties['Party'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Seat Distribution of Top 5 Parties')
plt.show()


# In[109]:


# Insights

# 1. Top 5 parties by total seats won
print("Top 5 parties by total seats won:")
print(df.sort_values(by='Total', ascending=False).head(5))
print(top_5_parties)


# In[110]:


# 2. Percentage of seats won by top 5 parties
total_seats = df['Total'].sum()
top_5_total = top_5_parties['Total'].sum()
percentage_top_5 = (top_5_total / total_seats) * 100
print(f"Percentage of seats won by the top 5 parties: {percentage_top_5:.2f}%")


# In[111]:


# 3. Total number of parties
total_parties = df.shape[0]
print(f"Total number of parties: {total_parties}")


# In[112]:


# 4. Party with the maximum seats
max_seats_party = df.iloc[0]['Party']
max_seats = df.iloc[0]['Total']
print(f"Party with the maximum seats: {max_seats_party} ({max_seats} seats)")


# In[113]:


# 5 Median Number of Seats Won
median_seats = df['Total'].median()
print(f"Median number of seats won: {median_seats}")


# In[114]:


#6 Standard Deviation of Seats Won
std_deviation = df['Total'].std()
print(f"Standard deviation of seats won: {std_deviation:.2f}")


# In[115]:


# 7 Number of Parties with More Than 10 Seats
parties_above_10 = df[df['Total'] > 10].shape[0]
print(f"Number of parties with more than 10 seats: {parties_above_10}")


# In[116]:


# 8 Top 3 Parties' Combined Seats:
top_3_total = df.head(3)['Total'].sum()
print(f"Total seats won by the top 3 parties: {top_3_total}")


# In[117]:


# 9 Least Represented Party
least_seats_party = df.iloc[-1]['Party']
least_seats = df.iloc[-1]['Total']
print(f"Party with the least seats: {least_seats_party} ({least_seats} seat)")


# In[118]:



# 10 Total Seats Won by Parties with Less Than 5 Seats
seats_less_than_5 = df[df['Total'] < 5]['Total'].sum()
print(f"Total seats won by parties with less than 5 seats: {seats_less_than_5}")


# In[ ]:




