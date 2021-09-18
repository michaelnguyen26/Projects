#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Analysis: Open Source Data Provided by Our World in Data
# # The data has been designed to update from the server host 
# # Program and analysis was completed by Michael Nguyen on June 26, 2020

# In[ ]:


import numpy as np
import matplotlib.pyplot as py 
import pandas as pd
import plotly.graph_objects as go
from datetime import *
from termcolor import colored 


# # Loading in COVID-19 Data (Source: Our World in Data)

# In[ ]:


covidData = pd.read_csv("owid-covid-data(updated).csv", delimiter = ",")


# In[ ]:


covidData.tail()


# # Assigning Variables and Figuring Out Where the U.S. is Located

# In[ ]:


totalcases = covidData['total_cases']
newcases = covidData['new_cases']

print(totalcases.tail(),'\n')
print(newcases.tail())


# In[ ]:


usData = np.where(covidData['location'] == 'United States')

np.shape(usData)
usData


# In[ ]:


print(covidData.iloc[27523], "\n")

print(covidData.iloc[27523,4])  #Exctracting data using integer based values at the last known date and fourth column for cases


# # Developing an Algorithm for Finding the Total Cases in the U.S. and Extracting the Formatted Date

# In[ ]:


usCases = np.zeros(np.size(usData))
n = 0

for i in range(np.size(usData)):
    nCases = covidData.iloc[27333+n,4]
    usCases[i] = nCases     
    n += 1
    if n == np.size(usData):
        break 

print(usCases[-1])


# In[ ]:


date = pd.to_datetime(covidData['date'], format = '%Y-%m-%d')
CasesByYear = date[27333:27524]

print(CasesByYear)


# # Visualizing the Data through an Interactive Model

# In[ ]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=CasesByYear, y=usCases,name="U.S. Cases"))
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(legend_title_text='Trend',showlegend=True, title="Total COVID-19 Cases in the U.S. from Dec 2020 to July 2020", 
                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                  font=dict(family="Courier New, monospace",size=14, color="#7f7f7f"))

fig.show()


# # Part 2: Comparing the Total Cases with Total Deaths

# In[ ]:


usData = np.where(covidData['location'] == 'United States')

np.size(usData)
np.reshape(usData,(np.size(usData),1))


# In[ ]:


covidData.iloc[27523,6] #Integer based indexing within the covidData array that was loaded through Pandas. The number
                        #six was chosen for the sixth position where total_deaths is located.


# # Utilizing the Same Algorithm Above and Manipulating the Change in Integer Position

# In[ ]:


usDeaths = np.zeros(np.size(usData))
d = 0

for i in range(np.size(usData)):
    nDeaths = covidData.iloc[27333+d,6]
    usDeaths[i] = nDeaths     
    d += 1
    if d == np.size(usData):
        break 

print(usDeaths[-1])


# # Data Visualization through an Interactive Model

# In[ ]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=CasesByYear, y=usDeaths,name="Rising Deaths"))
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(legend_title_text='Trend',showlegend=True, title="Total COVID-19 Deaths in the U.S. from Dec 2020 to July 2020", 
                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                  font=dict(family="Courier New, monospace",size=14, color="#7f7f7f"))

fig.show()


# # What is the Death Rate in the United States? (as of June 20, 2020)

# In[ ]:


totalLastCases = covidData.iloc[27523,4] #Integer based indexing to find total cases as of July 8, 2020.
totalLastDeaths = covidData.iloc[27523,6] #Integer based indexing to find total deaths as of July 8, 2020.


# In[ ]:


usPercentage = (totalLastDeaths/totalLastCases)*100 #The ratio needed to find how many deaths per case.

print('The percentage of deaths in the United States due to COVID-19 has roughly a {0:.2f}% mortality rate.'
      .format(usPercentage)) #Format method keeps sentence structure clean and easier to read.


# # Part 3: Comparing the U.S. Cases and Deaths with World Countries

# In[ ]:


chinaData = np.where(covidData['location'] == 'China')

print(np.shape(chinaData))
chinaData


# In[ ]:


chinaCases = np.zeros(np.size(chinaData))
c = 0

for i in range(np.size(chinaData)):
    cCases = covidData.iloc[5535+c,4]
    chinaCases[i] = cCases     
    c += 1
    if c == np.size(chinaData):
        break 

print(chinaCases[-1])


# In[ ]:


date = pd.to_datetime(covidData['date'], format = '%Y-%m-%d')
CasesByYear = date[27333:27524]

print(CasesByYear)


# # Convert Time Series into an Array

# In[ ]:


arrayTime = CasesByYear.dt.to_pydatetime() #.dt.to_pydatetime converts the time series into an array of time

print(arrayTime[0:5])


# # Adding in the Other Countries

# In[ ]:


ukData = np.where(covidData['location'] == 'United Kingdom')

print(np.shape(ukData))
ukData


# In[ ]:


ukCases = np.zeros(np.size(ukData))
u = 0

for i in range(np.size(ukData)):
    uCases = covidData.iloc[27142+u,4]
    ukCases[i] = uCases     
    u += 1
    if u == np.size(ukData):
        break 

print(ukCases[-1])


# In[ ]:


brazilData = np.where(covidData['location'] == 'Brazil')

print(np.shape(brazilData))
brazilData


# In[ ]:


brazilCases = np.zeros(np.size(brazilData))
br = 0

for i in range(np.size(brazilData)):
    brCases = covidData.iloc[3718+br,4]
    brazilCases[i] = brCases     
    br += 1
    if br == np.size(brazilData):
        break 

print(brazilCases[-1])


# In[ ]:


norwayData = np.where(covidData['location'] == 'Norway')

print(np.shape(norwayData))
norwayData


# In[ ]:


norwayCases = np.zeros(np.size(norwayData))
nor = 0

for i in range(np.size(norwayData)):
    norCases = covidData.iloc[19558+nor,4]
    norwayCases[i] = norCases     
    nor += 1
    if nor == np.size(norwayData):
        break 

print(norwayCases[-1])


# # Data Visualization

# In[ ]:


fig = py.figure(figsize=(12,10))
fontsize = 10

axis1 = fig.add_subplot(1,1,1) #(rows,columns, plot position)
axis1.plot(arrayTime, usCases, 'y-', linewidth=2, label = "Total Confirmed Cases in the U.S.")
axis1.plot(arrayTime, chinaCases, 'r-', linewidth=2, label = "Total Confirmed Cases in China")
axis1.plot(arrayTime, ukCases, 'g-', linewidth=2, label = "Total Confirmed Cases in the United Kingdom")
axis1.plot(arrayTime, brazilCases, 'k-', linewidth=2, label = "Total Confirmed Cases in Brazil")
axis1.plot(arrayTime, norwayCases, 'c-', linewidth=2, label = "Total Confirmed Cases in Norway")

axis1.set_ylabel("Total Cases")
axis1.set_xlabel("Time (months and days)")
axis1.tick_params(labelsize=fontsize)
axis1.set_title("COVID-19 Cases vs. Time")
axis1.legend()


# In[ ]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=CasesByYear, y=usCases,name="U.S."))
fig.add_trace(go.Scatter(x=CasesByYear, y=chinaCases,name="China"))
fig.add_trace(go.Scatter(x=CasesByYear, y=ukCases,name=" United Kingdom"))
fig.add_trace(go.Scatter(x=CasesByYear, y=brazilCases,name="Brazil"))
fig.add_trace(go.Scatter(x=CasesByYear, y=norwayCases,name="Norway"))

fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(legend_title_text='Country',showlegend=True, 
                  title="Total COVID-19 Cases from Dec 31, 2020 to July 8, 2020", 
                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                  font=dict(family="Courier New, monospace",size=14, color="#7f7f7f"))
fig.show()


# # Now, Let's Take a Look at the Death Rate of these Countries

# In[ ]:


usDeaths = np.zeros(np.size(usData))
d = 0

for i in range(np.size(usData)):
    nDeaths = covidData.iloc[27333+d,6]
    usDeaths[i] = nDeaths     
    d += 1
    if d == np.size(usData):
        break 

print(usDeaths[-1])


# In[ ]:


chinaDeaths = np.zeros(np.size(chinaData))
d1 = 0

for i in range(np.size(chinaData)):
    d1Deaths = covidData.iloc[5535+d1,6]
    chinaDeaths[i] = d1Deaths     
    d1 += 1
    if d1 == np.size(chinaData):
        break 

print(chinaDeaths[-1])


# In[ ]:


ukDeaths = np.zeros(np.size(ukData))
d2 = 0

for i in range(np.size(ukData)):
    d2Deaths = covidData.iloc[27142+d2,6]
    ukDeaths[i] = d2Deaths     
    d2 += 1
    if d2 == np.size(ukData):
        break 

print(ukDeaths[-1])


# In[ ]:


brazilDeaths = np.zeros(np.size(brazilData))
d3 = 0

for i in range(np.size(brazilData)):
    d3Deaths = covidData.iloc[3718+d3,6]
    brazilDeaths[i] = d3Deaths     
    d3 += 1
    if d3 == np.size(brazilData):
        break 

print(brazilDeaths[-1])


# In[ ]:


norwayDeaths = np.zeros(np.size(norwayData))
d5 = 0

for i in range(np.size(norwayData)):
    d5Deaths = covidData.iloc[19558+d5,6]
    norwayDeaths[i] = d5Deaths     
    d5 += 1
    if d5 == np.size(norwayData):
        break 

print(norwayDeaths[-1])


# In[ ]:


fig = py.figure(figsize=(12,10))
fontsize = 10

axis1 = fig.add_subplot(1,1,1) #(rows,columns, plot position)
axis1.plot(CasesByYear, usDeaths, 'y-', linewidth=2, label = "Deaths in the U.S.")
axis1.plot(CasesByYear, chinaDeaths, 'r-', linewidth=2, label = "Deaths in China")
axis1.plot(CasesByYear, ukDeaths, 'g-', linewidth=2, label = "Deaths in the United Kingdom")
axis1.plot(CasesByYear, brazilDeaths, 'k-', linewidth=2, label = "Deaths in Brazil")
axis1.plot(CasesByYear, norwayDeaths, 'c-', linewidth=2, label = "Deaths in Norway")

axis1.set_ylabel("Total Deaths")
axis1.set_xlabel("Time (months and days)")
axis1.tick_params(labelsize=fontsize)
axis1.set_title("COVID-19 Deaths vs. Time")
axis1.legend()


# In[ ]:


fig = go.Figure()

fig.add_trace(go.Scatter(x=CasesByYear, y=usDeaths,name="U.S."))
fig.add_trace(go.Scatter(x=CasesByYear, y=chinaDeaths,name="China"))
fig.add_trace(go.Scatter(x=CasesByYear, y=ukDeaths,name="United Kingdom"))
fig.add_trace(go.Scatter(x=CasesByYear, y=brazilDeaths,name="Brazil"))
fig.add_trace(go.Scatter(x=CasesByYear, y=norwayDeaths,name="Norway"))

fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(legend_title_text='Country',showlegend=True, 
                  title="Total COVID-19 Deaths from Dec 31, 2020 to July 8, 2020", 
                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                  font=dict(family="Courier New, monospace",size=14, color="#7f7f7f"))
fig.show()


# # What is the Mortality Rate of these Countries and How Does it Compare to the United States?

# In[ ]:


#China
mortalityChina = (covidData.iloc[5725,6]/covidData.iloc[5725,4])*100

#Brazil
mortalityBrazil = (covidData.iloc[3908,6]/covidData.iloc[3908,4])*100

#United Kingdom
mortalityUnitedKingdom = (covidData.iloc[27332,6]/covidData.iloc[27332,4])*100

#Norway
mortalityNorway = (covidData.iloc[19748,6]/covidData.iloc[19748,4])*100


# In[ ]:


print('Reminder: The percentage of deaths in the United States due to COVID-19 has roughly a',
      colored('{0:.2f}%'.format(usPercentage),'blue',attrs=['bold']),'mortality rate.\n') 

print('1) The mortality rate in China is',colored('{0:.2f}%\n'.format(mortalityChina),'red',attrs=['bold']))

print('2) The mortaility rate in Brazil is',colored('{0:.2f}%\n'.format(mortalityBrazil),'green',attrs=['bold']))

print('3) The mortality rate in the United Kingdom is',colored('{0:.2f}%\n'.format(mortalityUnitedKingdom),'magenta',attrs=['bold']))

print('4) The mortality rate in Norway is',colored('{0:.2f}%'.format(mortalityNorway),'cyan',attrs=['bold']))


# In[ ]:


averageMortality = float((mortalityChina+mortalityBrazil+mortalityUnitedKingdom+mortalityNorway+usPercentage)/5)

print('The average mortality rate between these five countries is',
      colored('{0:.2f}%.'.format(averageMortality),'red',attrs=['bold']))


# # Part 4: Combining the Above Procedures and Developing an Algorithm to Find the Cases in a Chosen Country with User Decision Structures

# In[ ]:


#Designing the Algorithm:

# 1) Loop or ask for user input of a specific country or countries
# 2) Retireve their index separately
# 3) Plot each specfic index seprately 


# In[1]:


import numpy as np
import matplotlib.pyplot as py 
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
from termcolor import colored 
import wget
import os
from collections import OrderedDict


# In[ ]:


#Debugging: Time Series

covidData = pd.read_csv("owid-covid-data.csv", delimiter = ",") 

class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

userInput= str(input(color.CYAN+'Country 1: '))
index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))


location_i = np.reshape(index_location,(np.size(index_location),1))
date = covidData['date']
date_conversion = pd.to_datetime(date)

CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
arrayTime = CasesByYear.dt.to_pydatetime()

year = CasesByYear.dt.year
day = CasesByYear.dt.day
month = CasesByYear.dt.month


################################### Results ##############################################

format_date1 = ('{0}/{1}/{2}'.format(month.iloc[0],day.iloc[0],year.iloc[0]))
format_date2 = ('{0}/{1}/{2}'.format(month.iloc[-1],day.iloc[-1],year.iloc[-1]))

print('-------------------------------------')
print('Start date: '+format_date1,'\nEnd date:   '+format_date2,'\n-------------------------------------')
print(CasesByYear)


# In[ ]:


#Debugging: How did the cases changed daily in user chosen country?

print(covidData.iloc[9913,5],'\n')

userInput= str(input(color.CYAN+'Country 1: '))
index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))
reshape_location = np.reshape(index_location,(np.size(index_location),1))

new_cases = np.zeros(np.size(reshape_location))

for newcases in range (np.size(index_location)):
                index_new_case = covidData.iloc[reshape_location[newcases],5]   
                new_cases[newcases] = index_new_case    
            
figurecase = go.Figure()

figurecase.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='{name}'.format(name=userInput)))
figurecase.update_xaxes(rangeslider_visible=True)
figurecase.update_layout(legend_title_text='Country',showlegend=True, 
                     title="New COVID-19 Cases in {0}".format(userInput), 
                     xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                     font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
figurecase.show()


# In[ ]:


np.where(covidData['location']=='United States')


# In[ ]:


covidData = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", delimiter = ",")    #Read in the new data updated to the server
low_memory = False

date = covidData['date']
date_conversion = pd.to_datetime(date,format='%Y-%m-%d')  

string_location = covidData['location']
hold_data = []

for z in range(np.size(string_location)):
    country_name = covidData.iloc[z,2]
    hold_data.append(country_name)

hold_data = list(OrderedDict.fromkeys(hold_data))  #Remove duplicate countries and create a new size with the correct countries

hold_data2 = [] 

for p in range(np.size(hold_data)):
    index_location = np.where(covidData['location']=='{country_index}'.format(country_index=hold_data[p]))
    hold_data2.append(index_location) #At each index "hold_data2" holds an array of indicies where the country is located

reshape_hold_data2 = []
    
for s in range(np.size(hold_data2)):
    reshape_country = np.reshape(hold_data2[s],(np.size(hold_data2[s]),1))
    reshape_hold_data2.append(reshape_country)

array_case = []

for a in range (np.size(reshape_hold_data2)):    
    country_index = reshape_hold_data2[a]
    for b in range(np.size(country_index)):
        index_case = covidData.iloc[country_index[b],4]  
        array_case.append(index_case)

           
CasesByYear = date_conversion[31376:31856]
arrayTime = CasesByYear.dt.to_pydatetime()

# figure = go.Figure()

for t in range(len(array_case)):
    figure.add_trace(go.Scatter(x=arrayTime, y=array_case[t],name='Countries'))

figure.update_xaxes(rangeslider_visible=True)
figure.update_layout(legend_title_text='Country',showlegend=True, 
                     title=("Total COVID-19 Cases"), 
                     xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                     font=dict(family="Times New Roman",size=12, color="#7f7f7f"))


figure.show()

print(len(array_case))


# In[2]:


def covid19_tracker():

#Creating a class for colored text--------------------------------------------------------------------------------------
    
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'    
    
#Read in the data from server-------------------------------------------------------------------------------------------
   
    url_data = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'   #Create a url source for the data

    try:
        
        if os.path.exists('owid-covid-data.csv')==True:    #Find the path to the file if it exists and if it does exist,
            os.remove('owid-covid-data.csv')               #delete the file.

        print(color.UNDERLINE+color.BOLD+'Loading program and retrieving data from server:\n'+color.END)
        wget.download(url_data, '/Users/nguye/Desktop/Programming Projects/Python Projects')  #download the new file with url
        
        print('\n')
        
        covidData = pd.read_csv("owid-covid-data.csv", delimiter = ",")    #Read in the new data updated to the server
        
        low_memory = False
    
    except UnboundLocalError:
        print(color.RED+color.BOLD+"\nError. Data or progam did not load successfully."+color.END)

#Introduction and retrieving user input and index for the chosen countries------------------------------------------------------------------------------
    
    print('\nWelcome! This program was built by',color.BLUE+color.BOLD+'Michael Nguyen'+color.END,
          'and this will track total COVID-19 cases and death rates. Please note that some data for certain dates can be missing.\n\n*** Remember to',
          color.BOLD+color.UNDERLINE+color.RED+'protect yourself and others, please wear a mask'+color.END,
          'when going outside! ***\n\n')
   
    print(color.BOLD+color.UNDERLINE+'Resources:'+color.END,'\n\n- For feature recommendations or reporting bugs, please send them to',
          color.BOLD+color.CYAN+'nguyen.michael.26@gmail.com'+color.END)
    
    print('- For up-to-date guidlines for your health and COVID-19, please visit',color.CYAN+color.BOLD+'cdc.gov\n\n'+color.END)
    
    print(color.BOLD+color.UNDERLINE+'\nOperating the Program:'+color.END,
          '\n\nPlease enter the name of the two countries you would like to see COVID-19 data. The country name is',
          color.BOLD+color.RED+'CASE SENSITIVE'+color.END,'\ntherefore, please capitalize the first letter. If a country has two parts, please capitalize the first letter after\nthe space between the name of the country. Please remove spaces where they are not needed as well.\n\n')
    
    userInput= str(input(color.CYAN+'Country 1: '))
    userInput2= str(input(color.RED+'Country 2: '))

 #Retrieve time data from file------------------------------------------------------------------------------------------
    
    date = covidData['date']
    date_conversion = pd.to_datetime(date,format='%Y-%m-%d')   
    
                                    #format is really not needed here, but best to be safe than sorry!
        

        
        
###################### Data with the dates are different for some countries ignore section below ######################   
    
    #us_date_index = np.where(covidData['location'] == 'United States')
    #location_i = np.reshape(us_date_index,(np.size(us_date_index),1))
    
    #CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
    #arrayTime = CasesByYear.dt.to_pydatetime()      #.dt.to_pydatetime converts the time series into an array of time
    
    #year = CasesByYear.dt.year
    #day = CasesByYear.dt.day
    #month = CasesByYear.dt.month
    
    #format_date1 = ('{0}/{1}/{2}'.format(month.iloc[0],day.iloc[0],year.iloc[0]))
    #format_date2 = ('{0}/{1}/{2}'.format(month.iloc[-1],day.iloc[-1],year.iloc[-1]))  

#######################################################################################################################    




#Decision Structure, User-Based Algorithm, and Time Series Algorithm----------------------------------------------------

    lor = ['YES','Y','NO','N']

    print(color.RED+color.BOLD+'\n\nYou may enter three more countries. Would you like to input more? (Y/N)\n'+color.END)
    userDecision = str(input())
    convert_input = userDecision.upper()
    
    if convert_input == lor[0] or convert_input == lor[1]:
        
        try:
            
            userInput3 = str(input(color.GREEN+'\nCountry 3: '))
            userInput4 = str(input(color.BLUE+'Country 4: '))
            userInput5 = str(input(color.PURPLE+'Country 5: '))

            index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))
            index_location2 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput2))
            index_location3 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput3))
            index_location4 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput4))
            index_location5 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput5))

            reshape_location = np.reshape(index_location,(np.size(index_location),1))
            reshape_location2 = np.reshape(index_location2,(np.size(index_location2),1))
            reshape_location3 = np.reshape(index_location3,(np.size(index_location3),1))
            reshape_location4 = np.reshape(index_location4,(np.size(index_location4),1))
            reshape_location5 = np.reshape(index_location5,(np.size(index_location5),1))

######################################### Time Series Structure #######################################################     
            
            location_i = np.reshape(index_location,(np.size(index_location),1))
            location_i2 = np.reshape(index_location2,(np.size(index_location2),1))
            location_i3 = np.reshape(index_location3,(np.size(index_location3),1))
            location_i4 = np.reshape(index_location4,(np.size(index_location4),1))
            location_i5 = np.reshape(index_location5,(np.size(index_location5),1))
            
            CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
            CasesByYear2 = date_conversion[int(location_i2[0]):int(location_i2[-1])+1]
            CasesByYear3 = date_conversion[int(location_i3[0]):int(location_i3[-1])+1]
            CasesByYear4 = date_conversion[int(location_i4[0]):int(location_i4[-1])+1]
            CasesByYear5 = date_conversion[int(location_i5[0]):int(location_i5[-1])+1]
            
            arrayTime = CasesByYear.dt.to_pydatetime()
            arrayTime2 = CasesByYear2.dt.to_pydatetime()
            arrayTime3 = CasesByYear3.dt.to_pydatetime()
            arrayTime4 = CasesByYear4.dt.to_pydatetime()
            arrayTime5 = CasesByYear5.dt.to_pydatetime()
            
#######################################################################################################################           
            
            totalCases = np.zeros(np.size(reshape_location))
            totalCases2 = np.zeros(np.size(reshape_location2))
            totalCases3 = np.zeros(np.size(reshape_location3))
            totalCases4 = np.zeros(np.size(reshape_location4))
            totalCases5 = np.zeros(np.size(reshape_location5))

            for i in range (np.size(index_location)):
                index_case = covidData.iloc[reshape_location[i],4]   
                totalCases[i] = index_case                          

            for j in range (np.size(index_location2)):
                index_case2 = covidData.iloc[reshape_location2[j],4]  
                totalCases2[j] = index_case2                     

            for k in range (np.size(index_location3)):
                index_case3 = covidData.iloc[reshape_location3[k],4]  
                totalCases3[k] = index_case3                     

            for l in range (np.size(index_location4)):
                index_case4 = covidData.iloc[reshape_location4[l],4]  
                totalCases4[l] = index_case4                     

            for m in range (np.size(index_location5)):
                index_case5 = covidData.iloc[reshape_location5[m],4]  
                totalCases5[m] = index_case5    
            
            new_cases  = np.zeros(np.size(reshape_location))
            new_cases2 = np.zeros(np.size(reshape_location2))
            new_cases3 = np.zeros(np.size(reshape_location3))
            new_cases4 = np.zeros(np.size(reshape_location4))
            new_cases5 = np.zeros(np.size(reshape_location5))
            
            for newcases in range (np.size(index_location)):
                index_new_case = covidData.iloc[reshape_location[newcases],5]   
                new_cases[newcases] = index_new_case  
            
            for newcases2 in range (np.size(index_location2)):
                index_new_case2 = covidData.iloc[reshape_location2[newcases2],5]   
                new_cases2[newcases2] = index_new_case2 
            
            for newcases3 in range (np.size(index_location3)):
                index_new_case3 = covidData.iloc[reshape_location3[newcases3],5]   
                new_cases3[newcases3] = index_new_case3  
            
            for newcases4 in range (np.size(index_location4)):
                index_new_case4 = covidData.iloc[reshape_location4[newcases4],5]   
                new_cases4[newcases4] = index_new_case4  
            
            for newcases5 in range (np.size(index_location5)):
                index_new_case5 = covidData.iloc[reshape_location5[newcases5],5]   
                new_cases5[newcases5] = index_new_case5  
            
            
            total_deaths = np.zeros(np.size(reshape_location))
            total_deaths2 = np.zeros(np.size(reshape_location2))
            total_deaths3 = np.zeros(np.size(reshape_location3))
            total_deaths4 = np.zeros(np.size(reshape_location4))
            total_deaths5 = np.zeros(np.size(reshape_location5))

            for i in range (np.size(index_location)):
                index_death = covidData.iloc[reshape_location[i],6]   
                total_deaths[i] = index_death                         

            for j in range (np.size(index_location2)):
                index_death2 = covidData.iloc[reshape_location2[j],6]  
                total_deaths2[j] = index_death2                     

            for k in range (np.size(index_location3)):
                index_death3 = covidData.iloc[reshape_location3[k],6]  
                total_deaths3[k] = index_death3                     

            for l in range (np.size(index_location4)):
                index_death4 = covidData.iloc[reshape_location4[l],6]  
                total_deaths4[l] = index_death4                     

            for m in range (np.size(index_location5)):
                index_death5 = covidData.iloc[reshape_location5[m],6]  
                total_deaths5[m] = index_death5  
        
        
            final_deaths = covidData.iloc[reshape_location[i],6]
            final_deaths2 = covidData.iloc[reshape_location2[j],6]
            final_deaths3 = covidData.iloc[reshape_location3[k],6]
            final_deaths4 = covidData.iloc[reshape_location4[l],6]
            final_deaths5 = covidData.iloc[reshape_location5[m],6]

            mortality_rate = float((final_deaths/totalCases[-1]))*100
            mortality_rate2 = float((final_deaths2/totalCases2[-1]))*100
            mortality_rate3 = float((final_deaths3/totalCases3[-1]))*100
            mortality_rate4 = float((final_deaths4/totalCases4[-1]))*100
            mortality_rate5 = float((final_deaths5/totalCases5[-1]))*100

############################################ Data Visualization #######################################################
    
            figure = go.Figure()

            figure.add_trace(go.Scatter(x=arrayTime, y=totalCases,name='{name}'.format(name=userInput)))
            figure.add_trace(go.Scatter(x=arrayTime2, y=totalCases2,name='{name}'.format(name=userInput2)))
            figure.add_trace(go.Scatter(x=arrayTime3, y=totalCases3,name='{name}'.format(name=userInput3)))
            figure.add_trace(go.Scatter(x=arrayTime4, y=totalCases4,name='{name}'.format(name=userInput4)))
            figure.add_trace(go.Scatter(x=arrayTime5, y=totalCases5,name='{name}'.format(name=userInput5)))
            
            figure.update_xaxes(rangeslider_visible=True)
            figure.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Total COVID-19 Cases {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                 xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                                 font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
            
            figure_new_case = go.Figure()
            
            figure_new_case.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='{name}'.format(name=userInput)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='{name}'.format(name=userInput2)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime3, y=new_cases3,name='{name}'.format(name=userInput3)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime4, y=new_cases4,name='{name}'.format(name=userInput4)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime5, y=new_cases5,name='{name}'.format(name=userInput5)))

            figure_new_case.update_xaxes(rangeslider_visible=True)
            figure_new_case.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Daily Change in COVID-19 Cases in {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                 xaxis_title="Time (months and days)", yaxis_title="Daily COVID-19 Cases",
                                 font=dict(family="Overpass",size=12, color="#7f7f7f"))
            
            figure2 = go.Figure()

            figure2.add_trace(go.Scatter(x=arrayTime, y=total_deaths,name='{name}'.format(name=userInput)))
            figure2.add_trace(go.Scatter(x=arrayTime2, y=total_deaths2,name='{name}'.format(name=userInput2)))
            figure2.add_trace(go.Scatter(x=arrayTime3, y=total_deaths3,name='{name}'.format(name=userInput3)))
            figure2.add_trace(go.Scatter(x=arrayTime4, y=total_deaths4,name='{name}'.format(name=userInput4)))
            figure2.add_trace(go.Scatter(x=arrayTime5, y=total_deaths5,name='{name}'.format(name=userInput5)))

            figure2.update_xaxes(rangeslider_visible=True)
            figure2.update_layout(legend_title_text='Country',showlegend=True, 
                                  title="Total COVID-19 Deaths {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
            
            return print('\n\nResults:\n\n1) The mortality rate of',colored('{0}'.format(userInput),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput,mortality_rate),'blue',attrs=['bold'])),print('\n\n2) The mortality rate of',colored('{0}'.format(userInput2),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput2,mortality_rate2),'blue',attrs=['bold'])),print('\n\n3) The mortality rate of',colored('{0}'.format(userInput3),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput3,mortality_rate3),'blue',attrs=['bold'])),print('\n\n4) The mortality rate of',colored('{0}'.format(userInput4),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput4,mortality_rate4),'blue',attrs=['bold'])),print('\n\n5) The mortality rate of',colored('{0}'.format(userInput5),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.'.format(userInput5,mortality_rate5),'blue',attrs=['bold'])), figure.show(),figure_new_case.show(),figure2.show()
        
        except UnboundLocalError:
            print('\nSorry,',color.RED+color.BOLD+'ONE or MORE'+color.END,
              'of the countries you have chosen was either misspelled or is not listed in the records of data and cannot be displayed.')
        
    elif convert_input == lor[2] or convert_input == lor[3]:
        
        try:
            
            index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))
            index_location2 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput2))

            reshape_location = np.reshape(index_location,(np.size(index_location),1))
            reshape_location2 = np.reshape(index_location2,(np.size(index_location2),1))
            
######################################### Time Series Structure #######################################################       
            
            location_i = np.reshape(index_location,(np.size(index_location),1))
            location_i2 = np.reshape(index_location2,(np.size(index_location2),1))
            
            CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
            CasesByYear2 = date_conversion[int(location_i2[0]):int(location_i2[-1])+1]
            
            arrayTime = CasesByYear.dt.to_pydatetime()
            arrayTime2 = CasesByYear2.dt.to_pydatetime()
            
#######################################################################################################################           
            
            totalCases = np.zeros(np.size(reshape_location))
            totalCases2 = np.zeros(np.size(reshape_location2))

            for i in range (np.size(index_location)):
                index_case = covidData.iloc[reshape_location[i],4]   
                totalCases[i] = index_case                          

            for j in range (np.size(index_location2)):
                index_case2 = covidData.iloc[reshape_location2[j],4]  
                totalCases2[j] = index_case2 
            
            new_cases  = np.zeros(np.size(reshape_location))
            new_cases2 = np.zeros(np.size(reshape_location2))
            
            for newcases in range (np.size(index_location)):
                index_new_case = covidData.iloc[reshape_location[newcases],5]   
                new_cases[newcases] = index_new_case  
            
            for newcases2 in range (np.size(index_location2)):
                index_new_case2 = covidData.iloc[reshape_location2[newcases2],5]   
                new_cases2[newcases2] = index_new_case2 
            
            total_deaths = np.zeros(np.size(reshape_location))
            total_deaths2 = np.zeros(np.size(reshape_location2))

            for i in range (np.size(index_location)):
                index_death = covidData.iloc[reshape_location[i],6]   
                total_deaths[i] = index_death                         

            for j in range (np.size(index_location2)):
                index_death2 = covidData.iloc[reshape_location2[j],6]  
                total_deaths2[j] = index_death2  

            final_deaths = covidData.iloc[reshape_location[i],6]
            final_deaths2 = covidData.iloc[reshape_location2[j],6]

            mortality_rate = float((final_deaths/totalCases[-1]))*100
            mortality_rate2 = float((final_deaths2/totalCases2[-1]))*100
            
############################################ Data Visualization #######################################################
    
            figure4 = go.Figure()

            figure4.add_trace(go.Scatter(x=arrayTime, y=totalCases,name='{name}'.format(name=userInput)))
            figure4.add_trace(go.Scatter(x=arrayTime2, y=totalCases2,name='{name}'.format(name=userInput2)))
            
            figure4.update_xaxes(rangeslider_visible=True)
            figure4.update_layout(legend_title_text='Country',showlegend=True, 
                                  title='Total COVID-19 Cases in {0} and {1}'.format(userInput,userInput2), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases", 
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
            
            figure_new_case = go.Figure()
            
            figure_new_case.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='{name}'.format(name=userInput)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='{name}'.format(name=userInput2)))

            figure_new_case.update_xaxes(rangeslider_visible=True)
            figure_new_case.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Daily Change in COVID-19 Cases in {0} and {1}".format(userInput,userInput2), 
                                 xaxis_title="Time (months and days)", yaxis_title="Daily COVID-19 Cases",
                                 font=dict(family="Overpass",size=12, color="#7f7f7f"))
            
            figure5 = go.Figure()

            figure5.add_trace(go.Scatter(x=arrayTime, y=total_deaths,name='{name}'.format(name=userInput)))
            figure5.add_trace(go.Scatter(x=arrayTime2, y=total_deaths2,name='{name}'.format(name=userInput2)))

            figure5.update_xaxes(rangeslider_visible=True)
            figure5.update_layout(legend_title_text='Country',showlegend=True, 
                                  title="Total COVID-19 Deaths in {0} and {1}".format(userInput,userInput2), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))

            return print('\n\nResults:\n\n1) The mortality rate of',colored('{0}'.format(userInput),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput,mortality_rate),'blue',attrs=['bold'])),print('\n\n2) The mortality rate of',colored('{0}'.format(userInput2),'red',attrs=['bold']),'is',
                                                                                                              colored('{1:.2f}%.\n'.format(userInput2,mortality_rate2),'blue',attrs=['bold'])),figure4.show(),figure_new_case.show(),figure5.show()
        
        except UnboundLocalError:
            print('\nSorry,',color.RED+color.BOLD+'ONE or MORE'+color.END,'of the countries you have chosen was either misspelled or is not listed in the records of data and cannot be displayed. Please re-run the program and check for spelling errors.')
        
################################## IF USER MESSES WITH INPUT, RUN THE CODE BELOW ######################################
    
    try:  
        
        while convert_input != lor[0] and convert_input!=lor[1] and convert_input!=lor[2] and convert_input!=lor[3]:

            decision_path =str(input('\nPlease enter "YES"(Y) or "NO"(N) as a response.\n'))
            convert_decision = decision_path.upper()

            if convert_decision == lor[0] or convert_decision == lor[1] or convert_decision == lor[2] or convert_decision == lor[3]:
                break
    
    except UnboundLocalError:
        print('\nSorry,',color.RED+color.BOLD+'ONE or MORE'+color.END,'of the countries you have chosen was either misspelled or is not listed in the records of data and cannot be displayed. Please re-run the program and check for spelling errors.')
    
    if convert_decision == lor[0] or convert_decision == lor[1]:
            
        try:
            
            userInput3 = str(input(color.GREEN+'\nCountry 3: '))
            userInput4 = str(input(color.BLUE+'Country 4: '))
            userInput5 = str(input(color.PURPLE+'Country 5: '))

            index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))
            index_location2 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput2))
            index_location3 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput3))
            index_location4 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput4))
            index_location5 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput5))

            reshape_location = np.reshape(index_location,(np.size(index_location),1))
            reshape_location2 = np.reshape(index_location2,(np.size(index_location2),1))
            reshape_location3 = np.reshape(index_location3,(np.size(index_location3),1))
            reshape_location4 = np.reshape(index_location4,(np.size(index_location4),1))
            reshape_location5 = np.reshape(index_location5,(np.size(index_location5),1))
            
######################################### Time Series Structure #######################################################           
            
            location_i = np.reshape(index_location,(np.size(index_location),1))
            location_i2 = np.reshape(index_location2,(np.size(index_location2),1))
            location_i3 = np.reshape(index_location3,(np.size(index_location3),1))
            location_i4 = np.reshape(index_location4,(np.size(index_location4),1))
            location_i5 = np.reshape(index_location5,(np.size(index_location5),1))
            
            CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
            CasesByYear2 = date_conversion[int(location_i2[0]):int(location_i2[-1])+1]
            CasesByYear3 = date_conversion[int(location_i3[0]):int(location_i3[-1])+1]
            CasesByYear4 = date_conversion[int(location_i4[0]):int(location_i4[-1])+1]
            CasesByYear5 = date_conversion[int(location_i5[0]):int(location_i5[-1])+1]
            
            arrayTime = CasesByYear.dt.to_pydatetime()
            arrayTime2 = CasesByYear2.dt.to_pydatetime()
            arrayTime3 = CasesByYear3.dt.to_pydatetime()
            arrayTime4 = CasesByYear4.dt.to_pydatetime()
            arrayTime5 = CasesByYear5.dt.to_pydatetime()
            
#######################################################################################################################

            totalCases = np.zeros(np.size(reshape_location))
            totalCases2 = np.zeros(np.size(reshape_location2))
            totalCases3 = np.zeros(np.size(reshape_location3))
            totalCases4 = np.zeros(np.size(reshape_location4))
            totalCases5 = np.zeros(np.size(reshape_location5))

            for i in range (np.size(index_location)):
                index_case = covidData.iloc[reshape_location[i],4]   
                totalCases[i] = index_case                          

            for j in range (np.size(index_location2)):
                index_case2 = covidData.iloc[reshape_location2[j],4]  
                totalCases2[j] = index_case2                     

            for k in range (np.size(index_location3)):
                index_case3 = covidData.iloc[reshape_location3[k],4]  
                totalCases3[k] = index_case3                     

            for l in range (np.size(index_location4)):
                index_case4 = covidData.iloc[reshape_location4[l],4]  
                totalCases4[l] = index_case4                     

            for m in range (np.size(index_location5)):
                index_case5 = covidData.iloc[reshape_location5[m],4]  
                totalCases5[m] = index_case5    
            
            new_cases  = np.zeros(np.size(reshape_location))
            new_cases2 = np.zeros(np.size(reshape_location2))
            new_cases3 = np.zeros(np.size(reshape_location3))
            new_cases4 = np.zeros(np.size(reshape_location4))
            new_cases5 = np.zeros(np.size(reshape_location5))
            
            for newcases in range (np.size(index_location)):
                index_new_case = covidData.iloc[reshape_location[newcases],5]   
                new_cases[newcases] = index_new_case  
            
            for newcases2 in range (np.size(index_location2)):
                index_new_case2 = covidData.iloc[reshape_location2[newcases2],5]   
                new_cases2[newcases2] = index_new_case2 

            for newcases3 in range (np.size(index_location3)):
                index_new_case3 = covidData.iloc[reshape_location3[newcases3],5]   
                new_cases3[newcases3] = index_new_case3  

            for newcases4 in range (np.size(index_location4)):
                index_new_case4 = covidData.iloc[reshape_location4[newcases4],5]   
                new_cases4[newcases4] = index_new_case4  

            for newcases5 in range (np.size(index_location5)):
                index_new_case5 = covidData.iloc[reshape_location5[newcases5],5]   
                new_cases5[newcases5] = index_new_case5  

            total_deaths = np.zeros(np.size(reshape_location))
            total_deaths2 = np.zeros(np.size(reshape_location2))
            total_deaths3 = np.zeros(np.size(reshape_location3))
            total_deaths4 = np.zeros(np.size(reshape_location4))
            total_deaths5 = np.zeros(np.size(reshape_location5))

            for i in range (np.size(index_location)):
                index_death = covidData.iloc[reshape_location[i],6]   
                total_deaths[i] = index_death                         

            for j in range (np.size(index_location2)):
                index_death2 = covidData.iloc[reshape_location2[j],6]  
                total_deaths2[j] = index_death2                     

            for k in range (np.size(index_location3)):
                index_death3 = covidData.iloc[reshape_location3[k],6]  
                total_deaths3[k] = index_death3                     

            for l in range (np.size(index_location4)):
                index_death4 = covidData.iloc[reshape_location4[l],6]  
                total_deaths4[l] = index_death4                     

            for m in range (np.size(index_location5)):
                index_death5 = covidData.iloc[reshape_location5[m],6]  
                total_deaths5[m] = index_death5  
        
        
            final_deaths = covidData.iloc[reshape_location[i],6]
            final_deaths2 = covidData.iloc[reshape_location2[j],6]
            final_deaths3 = covidData.iloc[reshape_location3[k],6]
            final_deaths4 = covidData.iloc[reshape_location4[l],6]
            final_deaths5 = covidData.iloc[reshape_location5[m],6]

            mortality_rate = float((final_deaths/totalCases[-1]))*100
            mortality_rate2 = float((final_deaths2/totalCases2[-1]))*100
            mortality_rate3 = float((final_deaths3/totalCases3[-1]))*100
            mortality_rate4 = float((final_deaths4/totalCases4[-1]))*100
            mortality_rate5 = float((final_deaths5/totalCases5[-1]))*100
            
############################################ Data Visualization #######################################################
         
            figure = go.Figure()

            figure.add_trace(go.Scatter(x=arrayTime, y=totalCases,name='{name}'.format(name=userInput)))
            figure.add_trace(go.Scatter(x=arrayTime2, y=totalCases2,name='{name}'.format(name=userInput2)))
            figure.add_trace(go.Scatter(x=arrayTime3, y=totalCases3,name='{name}'.format(name=userInput3)))
            figure.add_trace(go.Scatter(x=arrayTime4, y=totalCases4,name='{name}'.format(name=userInput4)))
            figure.add_trace(go.Scatter(x=arrayTime5, y=totalCases5,name='{name}'.format(name=userInput5)))
            
            figure.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='Daily Change in Cases for {name}'.format(name=userInput)))
            figure.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='Daily Change in Cases for {name}'.format(name=userInput2)))
            figure.add_trace(go.Scatter(x=arrayTime3, y=new_cases3,name='Daily Change in Cases for {name}'.format(name=userInput3)))
            figure.add_trace(go.Scatter(x=arrayTime4, y=new_cases4,name='Daily Change in Cases for {name}'.format(name=userInput4)))
            figure.add_trace(go.Scatter(x=arrayTime5, y=new_cases5,name='Daily Change in Cases for {name}'.format(name=userInput5)))


            figure.update_xaxes(rangeslider_visible=True)
            figure.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Total COVID-19 Cases in {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                 xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                                 font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
            
            figure_new_case = go.Figure()
            
            figure_new_case.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='{name}'.format(name=userInput)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='{name}'.format(name=userInput2)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime3, y=new_cases3,name='{name}'.format(name=userInput3)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime4, y=new_cases4,name='{name}'.format(name=userInput4)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime5, y=new_cases5,name='{name}'.format(name=userInput5)))

            figure_new_case.update_xaxes(rangeslider_visible=True)
            figure_new_case.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Daily Change in COVID-19 Cases in {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                 xaxis_title="Time (months and days)", yaxis_title="Daily COVID-19 Cases",
                                 font=dict(family="Overpass",size=12, color="#7f7f7f"))
            

            figure2 = go.Figure()

            figure2.add_trace(go.Scatter(x=arrayTime, y=total_deaths,name='{name}'.format(name=userInput)))
            figure2.add_trace(go.Scatter(x=arrayTime2, y=total_deaths2,name='{name}'.format(name=userInput2)))
            figure2.add_trace(go.Scatter(x=arrayTime3, y=total_deaths3,name='{name}'.format(name=userInput3)))
            figure2.add_trace(go.Scatter(x=arrayTime4, y=total_deaths4,name='{name}'.format(name=userInput4)))
            figure2.add_trace(go.Scatter(x=arrayTime5, y=total_deaths5,name='{name}'.format(name=userInput5)))

            figure2.update_xaxes(rangeslider_visible=True)
            figure2.update_layout(legend_title_text='Country',showlegend=True, 
                                  title="Total COVID-19 Deaths in {0}, {1}, {2}, {3}, and {4}".format(userInput,userInput2,userInput3,userInput4,userInput5), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))

            return print('\n\nResults:\n\n1) The mortality rate of',colored('{0}'.format(userInput),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput,mortality_rate),'blue',attrs=['bold'])),print('\n\n2) The mortality rate of',colored('{0}'.format(userInput2),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput2,mortality_rate2),'blue',attrs=['bold'])),print('\n\n3) The mortality rate of',colored('{0}'.format(userInput3),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput3,mortality_rate3),'blue',attrs=['bold'])),print('\n\n4) The mortality rate of',colored('{0}'.format(userInput4),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.\n'.format(userInput4,mortality_rate4),'blue',attrs=['bold'])),print('\n\n5) The mortality rate of',colored('{0}'.format(userInput5),'red',attrs=['bold']),'is',
                         colored('{1:.2f}%.'.format(userInput5,mortality_rate5),'blue',attrs=['bold'])), figure.show(),figure_new_case.show(),figure2.show()
        
        except UnboundLocalError: 
            print('\nSorry,',color.RED+color.BOLD+'ONE or MORE'+color.END,
                  'of the countries you have chosen was either misspelled or is not listed in the records of data and cannot be displayed.')
         
    elif convert_decision == lor[2] or convert_decision == lor[3]:
        
        try:
            
            index_location = np.where(covidData['location']=='{country_index}'.format(country_index=userInput))
            index_location2 = np.where(covidData['location']=='{country_index}'.format(country_index=userInput2))

            reshape_location = np.reshape(index_location,(np.size(index_location),1))
            reshape_location2 = np.reshape(index_location2,(np.size(index_location2),1))
            
######################################### Time Series Structure #######################################################

            location_i = np.reshape(index_location,(np.size(index_location),1))
            location_i2 = np.reshape(index_location2,(np.size(index_location2),1))
            
            CasesByYear = date_conversion[int(location_i[0]):int(location_i[-1])+1]
            CasesByYear2 = date_conversion[int(location_i2[0]):int(location_i2[-1])+1]
            
            arrayTime = CasesByYear.dt.to_pydatetime()
            arrayTime2 = CasesByYear2.dt.to_pydatetime()
            
#######################################################################################################################

            totalCases = np.zeros(np.size(reshape_location))
            totalCases2 = np.zeros(np.size(reshape_location2))

            for i in range (np.size(index_location)):
                index_case = covidData.iloc[reshape_location[i],4]   
                totalCases[i] = index_case                          

            for j in range (np.size(index_location2)):
                index_case2 = covidData.iloc[reshape_location2[j],4]  
                totalCases2[j] = index_case2    
            
            new_cases  = np.zeros(np.size(reshape_location))
            new_cases2 = np.zeros(np.size(reshape_location2))
           
            for newcases in range (np.size(index_location)):
                index_new_case = covidData.iloc[reshape_location[newcases],5]   
                new_cases[newcases] = index_new_case  
            
            for newcases2 in range (np.size(index_location2)):
                index_new_case2 = covidData.iloc[reshape_location2[newcases2],5]   
                new_cases2[newcases2] = index_new_case2 

            total_deaths = np.zeros(np.size(reshape_location))
            total_deaths2 = np.zeros(np.size(reshape_location2))

            for i in range (np.size(index_location)):
                index_death = covidData.iloc[reshape_location[i],6]   
                total_deaths[i] = index_death                         

            for j in range (np.size(index_location2)):
                index_death2 = covidData.iloc[reshape_location2[j],6]  
                total_deaths2[j] = index_death2  

           
            final_deaths = covidData.iloc[reshape_location[i],6]
            final_deaths2 = covidData.iloc[reshape_location2[j],6]

            mortality_rate = float((final_deaths/totalCases[-1]))*100
            mortality_rate2 = float((final_deaths2/totalCases2[-1]))*100
            
############################################ Data Visualization #######################################################
              
            figure4 = go.Figure()

            figure4.add_trace(go.Scatter(x=arrayTime, y=totalCases,name='{name}'.format(name=userInput)))
            figure4.add_trace(go.Scatter(x=arrayTime2, y=totalCases2,name='{name}'.format(name=userInput2)))
            
            figure.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='Daily Change in Cases for {name}'.format(name=userInput)))
            figure.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='Daily Change in Cases for {name}'.format(name=userInput2)))
            
            
            figure4.update_xaxes(rangeslider_visible=True)
            figure4.update_layout(legend_title_text='Country',showlegend=True, 
                                  title="Total COVID-19 Cases in {0} and {1}".format(userInput,userInput2), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Cases",
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))
            
            figure_new_case = go.Figure()
            
            figure_new_case.add_trace(go.Scatter(x=arrayTime, y=new_cases,name='{name}'.format(name=userInput)))
            figure_new_case.add_trace(go.Scatter(x=arrayTime2, y=new_cases2,name='{name}'.format(name=userInput2)))

            figure_new_case.update_xaxes(rangeslider_visible=True)
            figure_new_case.update_layout(legend_title_text='Country',showlegend=True, 
                                 title="Daily Change in COVID-19 Cases in {0} and {1}".format(userInput,userInput2), 
                                 xaxis_title="Time (months and days)", yaxis_title="Daily COVID-19 Cases",
                                 font=dict(family="Overpass",size=12, color="#7f7f7f"))
            
            figure5 = go.Figure()

            figure5.add_trace(go.Scatter(x=arrayTime, y=total_deaths,name='{name}'.format(name=userInput)))
            figure5.add_trace(go.Scatter(x=arrayTime2, y=total_deaths2,name='{name}'.format(name=userInput2)))

            figure5.update_xaxes(rangeslider_visible=True)
            figure5.update_layout(legend_title_text='Country',showlegend=True, 
                                  title="Total COVID-19 Deaths in {0} and {1}".format(userInput,userInput2), 
                                  xaxis_title="Time (months and days)", yaxis_title="COVID-19 Deaths",
                                  font=dict(family="Times New Roman",size=12, color="#7f7f7f"))

            return print('\n\nResults:\n\n1) The mortality rate of',colored('{0}'.format(userInput),'red',attrs=['bold']),'is',
                     colored('{1:.2f}%.\n'.format(userInput,mortality_rate),'blue',attrs=['bold'])),print('\n\n2) The mortality rate of',colored('{0}'.format(userInput2),'red',attrs=['bold']),'is',
                                                                                                          colored('{1:.2f}%.\n'.format(userInput2,mortality_rate2),'blue',attrs=['bold'])),figure4.show(),figure_new_case.show(),figure5.show()
        except UnboundLocalError:
            print('\nSorry,',color.RED+color.BOLD+'ONE or MORE'+color.END,
                  'of the countries you have chosen was either misspelled or is not listed in the records of data and cannot be displayed. Please re-run the program and check for spelling errors.')


# In[3]:


covid19_tracker()

