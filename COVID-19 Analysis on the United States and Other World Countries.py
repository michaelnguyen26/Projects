#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Analysis: Open Source Data Provided by Our World in Data
# # The data has been designed to update from the server host 
# # Program and analysis was completed by Michael Nguyen on June 26, 2020


# Part 1: Developing an Algorithm to Find the Cases in a Chosen Country with User Decision Structures

# Designing the Algorithm:

# 1) Loop or ask for user input of a specific country or countries
# 2) Retireve their index separately
# 3) Plot each specfic index seprately 


import numpy as np
import matplotlib.pyplot as py 
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
from termcolor import colored 
import wget
import os
from collections import OrderedDict

def covid19_tracker():

#Creating a class for colored text
    
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
    
#Read in the data from server
   
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

#Introduction and retrieving user input and index for the chosen countries
    
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

 #Retrieve time data from file
    
    date = covidData['date']
    date_conversion = pd.to_datetime(date,format='%Y-%m-%d')   
    
                            
#Decision Structure, User-Based Algorithm, and Time Series Algorithm

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

