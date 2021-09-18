#Presentation - Working & Experimentation project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# File import and treatment section
# Assign filename: file
file = 'output.csv'

# Import file: data
medals = pd.read_csv(file, sep=',', na_values=['Nothing'])
print(medals['Year'].unique())
print(medals['Country'].unique())
print(medals.columns)
print(medals.isnull().sum())



# File review and summary section
# Display sample data of the DataFrame
print(medals.head(5))

# Display max medals count by country
print("Max amount of gold medals by one country at any one Olympic games: " + str((medals["Gold"].max())))
print("Max amount of silver medals by one country at any one Olympic games: " + str((medals["Silver"].max())))
print("Max amount of bronze medals by one country at any one Olympic games: " + str((medals["Bronze"].max())))

#Display countries with the most Gold medals
top_10_countries_by_year = medals.groupby('Country')['Gold'].sum().sort_values(ascending=False).head(10)
print(top_10_countries_by_year)

yearly_view = (medals.pivot_table (index = "Country", columns="Year",values=['Gold'], fill_value=0))
print(yearly_view)

# Display Gold medal wins by reference to the relative wealth of countries
medals.groupby(["GDP_Strata", "Gold"]).sum()
wealthiest_countries = (medals.pivot_table (index = "Country", columns="GDP_Strata",values=['Gold'], fill_value="0"))
print(wealthiest_countries)

# Display Gold Medal wins by reference to the most populous countries
medals.groupby(["Population_Strata", "Gold"]).sum()
populous_countries = (medals.pivot_table (index = "Country", columns="Population_Strata",values=['Gold'], fill_value="0"))
print(populous_countries)



#Display Charts section
# List top performing countries by ref to gold medals
top_countries = ['USA', 'URS', 'GBR', 'CHN', 'JPN'] # Note Japan only entered top 4 only when Olympics were in Japan 2020
team_medals = pd.pivot_table(medals,index = 'Year',columns = 'Country',values = 'Gold',aggfunc = 'sum')[top_countries]
team_medals.plot(linestyle = '-', marker = 's', linewidth = 3)
plt.xlabel('Olympic Year')
plt.ylabel('Number of Medals')
plt.title('Top Countries - Olympic Performance Comparison')
plt.grid()
plt.show()

#Display medal wins against population level of the countries
plt.figure
sns.catplot(x='Population_Strata',kind='count',data=medals, order=medals.Population_Strata.value_counts().index)
plt.title('Gold Medal wins versus population level',fontsize=16)
plt.grid()
plt.show()


#Display medal wins against relative wealth level of the countries
plt.figure
sns.catplot(x='GDP_Strata',kind='count',data=medals, order=medals.GDP_Strata.value_counts().index)
plt.title('Gold Medal wins versus GDP per capita',fontsize=12)
plt.grid()
plt.show()


medals.groupby('GDP_Strata')[['Gold','Bronze','Silver']].sum().plot.bar(color=['gold','red','grey'])
plt.xlabel('Country',fontsize=12)
plt.ylabel('Medal Count',fontsize=12)
plt.title('All Countries All medals by GDP per capita',fontsize=14)
plt.grid()
plt.show()


# Focus on Ireland performance
# Display ALL Irish medal wins
medals[medals['Country']=='IRL'][['Gold','Bronze','Silver']].sum().plot.bar(color=['gold','red','grey'])
plt.xlabel('IRELAND OLYMPIC MEDALS TOTAL',fontsize=10)
plt.ylabel('TOTAL MEDALS',fontsize=10)
plt.title('Total Irish Olympic Medal Wins',fontsize=14)
plt.grid()
plt.show()

# Display ALL Irish medal wins
ireland_results = medals[medals['Country']=='IRL'].sort_values(['Year'], ascending=True)
print (ireland_results)
sns.barplot(y='Gold', x='Year' , data=ireland_results.sort_values(['Gold']),color="green")
plt.xlabel('Ireland performance by year',fontsize=10)
plt.ylabel('Year',fontsize=10)
plt.title('All Irish Gold Medal Wins by year',fontsize=14)
plt.grid()
plt.show()


# Focus on USA performance at 1904 and 1984 games
USA_results = medals[medals['Country']=='USA'].sort_values(['Year'], ascending=True)
print (USA_results)
sns.barplot(y='Gold', x='Year' , data=USA_results.sort_values(['Gold']),color="blue")
plt.xlabel('USA performance by year',fontsize=10)
plt.ylabel('Year',fontsize=10)
plt.title('All USA Gold Medal Wins by year',fontsize=14)
plt.grid()
plt.show()


# Focus on China performance since 1984
# Display ALL Chinese medal wins
china_results = medals[medals['Country']=='CHN'].sort_values(['Year'], ascending=True)
print (china_results)
sns.barplot(y='Gold', x='Year' , data=china_results.sort_values(['Gold']),color="red")
plt.xlabel('China performance by year',fontsize=10)
plt.ylabel('Year',fontsize=10)
plt.title('All Chinese Gold Medal Wins since 1984',fontsize=14)
plt.grid()
plt.show()

