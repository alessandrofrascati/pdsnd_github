# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:10:44 2019
@author: Alessandro.Frascati
"""

import time
import pandas as pd
import numpy as np

# Visualization options (on terminal)
pd.set_option('display.max_columns', None,'expand_frame_repr', False)

# Dictionary initialization
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

# lists initialization 
city_list = [element.title() for element in list(CITY_DATA.keys())]
month_list = ['January','February', 'March','April','May','June']
day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
time_filter_list = ['day','month','none']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
     """
    print('-'*80)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*80)
    
    # Get user input for city (with restart if applicable)
    restart = True    
    while restart:
        print('\33[32m'+ 'Data selection...' + '\x1b[0m')
        city = input ('\33[31m' + 'Which data-set would you like to analize? \n'
                      'Please enter the name of the city: {}\n'.format(city_list))
        while city.title() not in city_list:
            city = input('Oops, looks like you mispelled the city name!\n'
                          'Please re-enter a valid city name: {}\n'.format(city_list))    
        # Checking if the correct data is going to be analyzed    
        r_input = input('You are going to analyze data from {}! Is that correct?\n'
                        'Enter yes (Y) to continue or any key to restart!\n'.format(city.title()) + '\33[0m')    
        if r_input.lower() == 'y':
            restart = False  
        else:
            print('-'*80)
            print('Analysis Restarted')
            print('-'*80)
    city = city.lower()
    
    # Get user input for time-filtering (filtering by day, month or no data filtering)
    time_filter = input('\33[31m' + 'Which time-filter would you like to apply to the data? \n'
                        'Please enter the filter mode: {}\n'.format(time_filter_list))
    while time_filter.lower() not in time_filter_list:
         time_filter = input('Oops, looks like you mispelled the input for time-filtering!\n'
                          'Please re-enter a valid filter mode: {}\n'.format(time_filter_list))  
    time_filter = time_filter.lower()     
    
    # Filterign by month (all, january, february, ... , june)
    if time_filter == 'month':
        month = input('Which month do you want to analyse?\n'
                      'Please enter the full month name: {}\n'.format(month_list)) 
        while month.title() not in month_list:
            month = input('Oops, looks like you mispelled the month!\n'
                          'Please re-enter a valid full month name: {}\n'.format(month_list))  
        month = month.title()    
        day = 'all'
        print('\33[0m' + '-'*80)
        print('Data from {} will be filtered by "{}"= {}'.format(city.title(),time_filter,month))
        
    # Filtering by day of week (all, monday, tuesday, ... sunday)
    if time_filter == 'day':
        day = input('Which day of the week do you want to analyse?\n' 
                     'Please enter the day: {}\n'.format(day_list)) 
        while day.title() not in day_list:
            day = input('Oops, looks like you mispelled the day!\n'
                          'Please re-enter a valid full day name: {}\n'.format(day_list))        
        day = day.title()
        month = 'all'
        print('\33[0m' + '-'*80)
        print('Data from {} will be filtered by "{}"= {}'.format(city.title(),time_filter,day))
        
    # No time-filtering (i.e. all available data are considered) 
    if time_filter == 'none':
        day = 'all';
        month = 'all';
        print('\33[0m' + '-'*80)
        print('' + 'The entire data-set from {} will be analyzed'.format(city.title()))
        
        
    print('-'*80)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day (if applicable).
    Asks user to displays raw data for the specified city and filters by month and day (if applicable).

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data eventually filtered by month and day
    """
    # load data-set for the specified city
    df = pd.read_csv(CITY_DATA[city])
        
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract info from the Start Time column to create other columns to be analyzed 
    df['Start Hour'] = df['Start Time'].dt.hour
    df['Week Day'] = df['Start Time'].dt.weekday_name
    df['Month'] = df['Start Time'].dt.month_name()
    
    # Filter by month if time_filter = month
    if month != 'all':
        df = df[df['Month'] == month]

    # Filter by day of week if time_filter = day
    if day != 'all':
        df = df[df['Week Day'] == day]
                
    # Displaying the data-frame that will be analized (if applicable)
    print('\33[32m' + 'Displaying the data-set...' + '\x1b[0m')
    disp_data_flag = input('\33[31m' + 'Do you want to have a look at the first 10 trips?\n'
                           'Enter yes (Y) to display them or press any key to continue with the analysis!\n' + '\33[0m')
    number_of_display = 0
    count = 10;
    while disp_data_flag.lower() == 'y':
        number_of_display = 1
        print(df[count-10:count])
        count += 10
        disp_data_flag = input('\33[31m' + 'Do you want to have a look at the next 5 individual trips?\n'
                               'Enter yes (Y) to display them or press any key to continue with the analysis!\n' + '\33[0m')
    
    if number_of_display == 0:
        print('-'*80) 
        print('Individual trips details will not be displayed!')
    print('-'*80)  
    print('Analyzing the data set...')
    print('-'*80) 
    
    return df


def most_popular_element(df,col_name):
    """
    Args:
        (df) - Pandas DataFrame containing city data eventually filtered by month and day 
        (str) col_name - name of DataFrame column to be analyzed
    Returns:
        (str) mp_element - most popular element in the column
        (int) counts - counts of the most popular element 
    """
    u,c = np.unique(df[col_name], return_counts=True)
    counts = c.max()
    mp_element = u[np.where(c == counts)][0] 
    
    return mp_element,counts

def time_stats(df,month,day):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (df) - Pandas DataFrame containing city data eventually filtered by month and day  
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter     
    """
    
    # Start computing 
    print('\33[32m' + 'Calculating The Most Frequent Times of Travel...\n' + '\x1b[0m')
    
    start_time = time.time()

    # Display the most common month
    popular_month,counts_month = most_popular_element(df,'Month')
    if month == 'all':
        print('Most Popular Month: {}, Counts = {}'
              .format(popular_month,counts_month))
    else:
        print('Data Filtered by "Month": {}, Number of Trips Analyzed = {}'
              .format(popular_month,counts_month))       
            
    # Display the most common day of week  
    popular_week_day,counts_pwd = most_popular_element(df,'Week Day')
    if day == 'all':
        print('Most Popular Day of the Week: {}, Counts = {}'
              .format(popular_week_day,counts_pwd))
    else:
        print('Data Filterd by "Day of the Week": {}, Number of Trips Analyzed = {}'
              .format(popular_week_day,counts_month))  
   
    # Display the most common start hour
    popular_start_hour,counts_psh = most_popular_element(df,'Start Hour')
    print('Most Popular Start Hour: {}, Counts = {}'
          .format(popular_start_hour,counts_psh))

    # Computing time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (df) - Pandas DataFrame containing city data eventually filtered by month and day   
    """
 
    print('\33[32m' + 'Calculating The Most Popular Stations and Trip...\n' + '\x1b[0m')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station,counts_pss = most_popular_element(df,'Start Station')
    print('Most Commonly Used Start Station: {}, Counts = {}'
          .format(popular_start_station,counts_pss))      

    # Display most commonly used end station
    popular_end_station,counts_pes = most_popular_element(df,'End Station')    
    print('Most Commonly Used End Station: {}, Counts = {}'
          .format(popular_end_station,counts_pes)) 
    
    # Display most frequent combination of start station and end station trip
    aux ={}
    aux['Start-End'] = df['Start Station'] + ' - ' + df['End Station']
    popular_start_end_combo,counts_sec = most_popular_element(aux,'Start-End') 
    print('Most Frequent Start - End Station Combination: {}, Counts = {}'
          .format(popular_start_end_combo,counts_sec))         
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        (df) - Pandas DataFrame containing city data eventually filtered by month and day      
    """

    print('\33[32m' + 'Calculating Trip Duration...\n' + '\x1b[0m')
    start_time = time.time()

    # Display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {} hours'.format(np.round(tot_travel_time/3600,1)))  
      
    # Display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {} minutes'.format(np.round(avg_travel_time/60,1)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def user_stats(df): 
    """
    Displays statistics on bikeshare users.
    
    Args:
        (df) - Pandas DataFrame containing city data eventually filtered by month and day      
    """
    
    print('\33[32m' + 'Calculating User Stats...\n' + '\x1b[0m')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Type\n{}'.format(user_type.to_string()))
    
    # Display counts of gender    
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('\nUser Gender\n{}'.format(user_gender.to_string()))
    else:
        print('\nUser Gender Information not available')    

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_year_oldest = df['Birth Year'].min()
        birth_year_youngest  = df['Birth Year'].max()
        birth_year_common,counts_byc = most_popular_element(df,'Birth Year')  
        print('\nYear of Birth')
        print('Earliest: {}'.format(int(birth_year_oldest)))
        print('Most Recent: {}'.format(int(birth_year_youngest)))
        print('Most Common: {}, Counts = {}'
              .format(int(birth_year_common),counts_byc))
    else:
        print('\nUser Year of Birth Information not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def main():
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)   

                                  
if __name__ == "__main__":
	main()






