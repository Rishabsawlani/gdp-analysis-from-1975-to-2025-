''' importing the dataset'''
import kagglehub

# Download latest version
path = kagglehub.dataset_download("codebynadiia/gdp-1975-2025")

# print("Path to dataset files:", path)


''' reading the data and getting its info and creating its copy '''

import pandas as pd
df = pd.read_csv('GDP_1975_2025_uploaded.csv')
# print(df.head(10))

# print("displaying the info of data set")
# print(df.info())

df_copy = df.copy()

''' amount of missing values and then replacing them  '''
# print(df_copy.isnull().sum())

# since the null values signify the countries didnt exist at that time so replacing those null gdp values with 0
df_copy.fillna(0 , inplace = True)
# print(df_copy.head(10))


''' Total Global GDP Over Time (1975–2025) → line plot'''
import matplotlib.pyplot as plt
import numpy as np
# sum of all economies from 1975 to 2025 and accessing all columns for plotting 

years_columns =  df_copy.loc[: , '1975':'2025'].columns.to_list()
global_gdp_list= df_copy.loc[: , '1975':'2025'].sum().to_list()
global_gdp= df_copy.loc[: , '1975':'2025'].sum()
# print(years_columns)
# print(sums)

# plot the graph 

# plt.figure(figsize = (15,15))
# plt.plot(years_columns , global_gdp_list , linestyle = '--' , linewidth = 2 , marker = 'o')
# plt.title('global gdp 1975 to 2025')
# plt.xlabel(" years")
# plt.ylabel("global gdp")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('global_gdp_vs_years.png')
# plt.show()


''' GDP Growth Rate per Year (global average) → line/bar plot'''

gdp_growth_rate = (global_gdp.pct_change()*100).tolist()
# plt.figure(figsize = (15,15))
# plt.plot(years_columns , gdp_growth_rate , linestyle = '--' , linewidth = 2 , marker = 'o')
# plt.title('global gdp growth rate 1975 to 2025')
# plt.xlabel(" years")
# plt.ylabel("global gdp growth rate")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('global_gdp_vs_years_growth_rate.png')
# plt.show()


'''Top 10 Economies by GDP (2025 projection) → horizontal bar chart'''

df_copy.sort_values(by = '2025' , ascending = False , inplace = True)
# plt.figure(figsize = (15,15))
# plt.barh(df_copy['Country'].head(10) , df_copy['2025'].head(10) , color = 'teal' )
# plt.title('top 10 economies in 2025')
# plt.xlabel("economy in 2025")
# plt.ylabel("countries ")
# plt.legend()
# plt.grid(True)
# plt.savefig('top_10_economies_2025.png')
# plt.show()


''' GDP Share of Top 5 vs Rest of World (stacked bar or pie) → pie or area chart '''

top_5_gdp = df_copy['2025'].head(5)
top_5_gdp_sum = df_copy['2025'].head(5).sum()
rest_gdp_sum = df_copy['2025'].tail(201).sum()
shares = [top_5_gdp_sum , rest_gdp_sum]

# plt.figure(figsize = (15,15))
# plt.pie(shares , labels = ['top 5 gdp' , 'rest of the world'], autopct='%1.1f%% ', colors = ['blue' , 'coral'])
# plt.title('gdp share of top 5 vs rest of world')
# plt.legend()
# plt.savefig('top_5_vs_rest_gdp.png')
# plt.show()


''' Individual Country GDP Trend (e.g., India, USA, China) → line plots per country'''

# india

years_columns =  df_copy.loc[: , '1975':'2025'].columns.to_list()
India_gdp_list = df_copy.loc[df_copy['Country'] == 'India', '1975':'2025'].values.flatten().tolist()
# plt.figure(figsize = (15,15))
# plt.plot(years_columns , India_gdp_list , linestyle = '--' , linewidth = 2 , marker = 'o' , label = 'india gdp')
# plt.title('India gdp 1975 to 2025')
# plt.xlabel(" years")
# plt.ylabel("india gdp")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('india_gdp_1975_2025.png')
# plt.show()

# united states of america 

years_columns =  df_copy.loc[: , '1975':'2025'].columns.to_list()
usa_gdp_list = df_copy.loc[df_copy['Country'] == 'United States', '1975':'2025'].values.flatten().tolist()
# plt.figure(figsize = (15,15))
# plt.plot(years_columns , usa_gdp_list , linestyle = '--' , linewidth = 2 , marker = 'o' , label = 'usa gdp')
# plt.title('USA gdp 1975 to 2025')
# plt.xlabel(" years")
# plt.ylabel("Usa gdp")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('Usa_gdp_1975_2025.png')
# plt.show()

# china - people's republic of china

years_columns =  df_copy.loc[: , '1975':'2025'].columns.to_list()
china_gdp_list = df_copy.loc[df_copy['Country'] == 'China', '1975':'2025'].values.flatten().tolist()
# plt.figure(figsize = (15,15))
# plt.plot(years_columns , china_gdp_list , linestyle = '--' , linewidth = 2 , marker = 'o' , label = 'china gdp')
# plt.title('china gdp 1975 to 2025')
# plt.xlabel(" years")
# plt.ylabel("china gdp")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('china_gdp_1975_2025.png')
# plt.show()


''' Compare Major Economies Over Time (USA vs China vs Japan vs India) → multi-line chart '''

japan_gdp_list = df_copy.loc[df_copy['Country'] == 'Japan', '1975':'2025'].values.flatten().tolist()
# plt.figure(figsize=(13,13))
# plt.plot(years_columns , china_gdp_list , linestyle = '--' , linewidth = 2 , color = 'red' , marker = 'o' , label = 'china gdp')
# plt.plot(years_columns , India_gdp_list , linestyle = '-' , linewidth = 2 , color = 'blue' ,marker = 'o' , label = 'India gdp')
# plt.plot(years_columns , usa_gdp_list , linestyle = '--' , linewidth = 2 , color = 'green' ,marker = 'o' , label = 'usa gdp')
# plt.plot(years_columns , japan_gdp_list , linestyle = '--' , linewidth = 2 , color = 'yellow' ,marker = 'o' , label = 'japan gdp')
# plt.title('major economies comparision')
# plt.xlabel(" years")
# plt.ylabel("gdp of countries")
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.savefig('major_economies_comparision.png')
# plt.show()


''' Fastest Growing Economies (CAGR from 2000–2025) → bar chart '''

start_year = '2000'
end_year = '2025'
years_diff = int(end_year) - int(start_year)

df_copy['CAGR_2000_2025'] = (( df_copy[end_year]/ df_copy[start_year])** (1/years_diff)-1)*100
df_copy.sort_values(by = 'CAGR_2000_2025' , ascending = False , inplace = True)
# # print(df_copy['CAGR_2000_2025'])
# plt.figure(figsize=(15,15))
# plt.bar(df_copy['Country'].head(10) , df_copy['CAGR_2000_2025'].head(10) )
# plt.title('fastest growing economies 2000-2025')
# plt.xlabel('countries')
# plt.ylabel('Compound Annual Growth Rate (CAGR)')
# plt.tight_layout()
# plt.savefig('fastest_growing_eceonomies.png')
# plt.show()


''' Countries with Declining or Stagnant GDP (negative growth) → bar chart '''

df_copy.sort_values(by = 'CAGR_2000_2025' , ascending = True , inplace = True)
# plt.figure(figsize=(15,15))
# plt.bar(df_copy['Country'].head(10) , df_copy['CAGR_2000_2025'].head(10) )
# plt.title('negative growth economies 2000-2025')
# plt.xlabel('countries')
# plt.ylabel('Compound Annual Growth Rate (CAGR)')
# plt.tight_layout()
# plt.savefig('negative_growing_eceonomies.png')
# plt.show()


''' Group countries by continent (e.g., Asia, Europe, Africa, Americas) '''

import pycountry_convert as pc

# Step 1: Function to get continent name
def country_to_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        return 'Unknown'   # If country not found or old one like USSR

# Step 2: Create a small manual mapping for special countries
continent_map = {
    'Soviet Union': 'Europe/Asia',
    'Yugoslavia': 'Europe',
    'South Sudan': 'Africa'
}

# Step 3: Loop through each row and assign continent
continents = []
for country in df_copy['Country']:
    if country in continent_map:
        continents.append(continent_map[country])
    else:
        continents.append(country_to_continent(country))

# Step 4: Add this as a new column
df_copy['Continent'] = continents


''' Total GDP by Region (2025) → bar chart '''

continent_gdp_2025 = df_copy.groupby('Continent')['2025'].sum().sort_values(ascending=False)
# plt.figure(figsize=(10,10))
# plt.bar(continent_gdp_2025.index, continent_gdp_2025.values)
# plt.title('GDP by Continent (2025)')
# plt.xlabel('Continent')
# plt.ylabel('Total GDP (2025)')
# plt.grid(True)
# plt.savefig('gdp_continent.png')
# plt.show()


''' Regional GDP Growth Trends (1975–2025) → multi-line chart '''

continent_gdp_1975_2025 = (
    df_copy
    .groupby('Continent')[ [str(y) for y in range(1975, 2026)] ]
    .sum()
    .sort_values(by='2025', ascending=False)
)
# plt.figure(figsize=(15,10))
# for continent in continent_gdp_1975_2025.index:
#     plt.plot(
#         [str(y) for y in range(1975, 2026)],
#         continent_gdp_1975_2025.loc[continent],
#         marker='o',
#         label=continent
#     )

# plt.title('Continent-wise GDP (1975–2025)')
# plt.xlabel('Year')
# plt.ylabel('Total GDP (in USD billions)')
# plt.xticks(rotation = 45)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('continental_gdp_growth.png')
# plt.show()


''' Compare USSR (before dissolution) vs Combined GDP of its Successor States (after 1991) → stacked line/area chart'''
USSR_gdp_list = df_copy.loc[df_copy['Country'] == 'Soviet Union', '1975':'1991'].values.flatten().tolist()
USSR_successor_states = [
    'Russia',
    'Ukraine',
    'Belarus',
    'Estonia',
    'Latvia',
    'Lithuania',
    'Moldova',
    'Georgia',
    'Armenia',
    'Azerbaijan',
    'Kazakhstan',
    'Uzbekistan',
    'Turkmenistan',
    'Kyrgyzstan',
    'Tajikistan'
]
successor_gdp_list = (
    df_copy[df_copy['Country'].isin(USSR_successor_states)]
    .loc[:, '1991':'2025']
    .sum()
    .values
    .tolist()
)

# plt.figure(figsize=(14, 8))

# # Plot USSR (1975–1991)
# plt.plot(
#     [str(y) for y in range(1975, 1992)],
#     USSR_gdp_list,
#     label='USSR (1975–1991)',
#     color='red',
#     linewidth=2,
#     marker='o'
# )

# # Plot successor states (1991–2025)
# plt.plot(
#     [str(y) for y in range(1991, 2026)],
#     successor_gdp_list,
#     label='Successor States Combined (1991–2025)',
#     color='blue',
#     linewidth=2,
#     marker='o'
# )

# plt.title('USSR vs Combined Successor States GDP Comparison')
# plt.xlabel('Year')
# plt.ylabel('Total GDP (in USD billions)')
# plt.legend()
# plt.xticks(rotation= 45)
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('ussr_successor_comparision.png')
# plt.show()


''' yugoslovia vs successor states gdp comparision grouped bar chart '''
# List of successor states
successor_states = [
    "Serbia",
    "Croatia",
    "Slovenia",
    "Bosnia and Herzegovina",
    "Montenegro",
    "North Macedonia",
    "Kosovo"
]

# Filter only successor states & get their 2024 GDP
successor_gdp_2024 = df.loc[df["Country"].isin(successor_states), "2024"].values.flatten().tolist()
# print(successor_gdp_2024)

yugoslavia_1975 = df_copy.loc[df_copy['Country'] == 'Yugoslavia' , '1975'].values[0]

# Create bar positions
# x = np.arange(len(successor_states))
# width = 0.35

# Plot grouped bars
# plt.figure(figsize=(10, 6))
# plt.bar(x - width/2, yugoslavia_1975 , width, label='Yugoslavia (1975)', color='gray')
# plt.bar(x + width/2, successor_gdp_2024, width, label='Successor States (2024)', color='skyblue')

# # Labels and formatting
# plt.xlabel("Countries")
# plt.ylabel("GDP (in Billion USD)")
# plt.title("Yugoslavia vs Successor States GDP Comparison")
# plt.xticks(x, successor_states , rotation=30)
# plt.legend()
# plt.tight_layout()
# plt.savefig('yugoslavia_vs_successor_gdp.png')
# plt.show()

# # print(type(successor_gdp_2024))
# # print(successor_gdp_2024)
# print(yugoslavia_1975)
