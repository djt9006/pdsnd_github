import time
import pandas as pd
import numpy as np

"""
Import modules to handle the time, and data needs of the project
""" 


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city are you interested in, Chicago, New York City, or Washington?\n").title()
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("We are not familiar with that city. Please select again.")
        continue
      else:
        break

    """
    While loop asks the user to enter in the month they are interested in specifically
    Variable called city is created for string text
    If the entry input does not meet the selected input they receive a prompt to try again.
    """

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month are you interested in? January, February, March, April, May, June or type 'all' for all months?\n").title()
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Something went wrong. Please try again.")
        continue
      else:
        break
    """
    User is asked to enter in the month the are interested in 
    Variable called month is created for string text
    Or all if they want to see information for all the months
    If they enter in information that does not meet the expected string they will be prompted to try again
    """     
        
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day are you interested in? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' for all the days of the week.\n").title()
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    """
    Customer is asked to enter the day of the week they are interested in
    Variable called day is created for string text
    Or they can type all for all the days of the week
    If they enter in any unexpected strings they will be prompted to try again
    """    
        
    print('-'*40)
    return city, month, day

    """
    Line with 40 * printed out
    Returns the results of the user input for City, Month and Day which are variables 
    The names city, month and day are the names of the 3 previously created functions
    """

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    """  
    Data is put into a dataframe created using Pandas.
    read_csv function used to read csv file in python or import data in python. 
    city_choice
    """
   
    """
    #Show raw data, 5 rows at a time
    see_data = "1"
    i = 0
    while(see_data != "2"):
        print(df[i:i+5])
        i += 5
        print("1 for more 5 rows")
        print("2 for break")
        see_data = input("enter the number")
    
    created a var and set it to 1
    established and var to increment
    While loop will run unless 2 is entered and that will break the loop
    While loop prints 5 lines of raw data 
    i increments the raw data by 5 rows if 1 is selected
    """

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    """
    Create a df for the time of start
    The datetime method converts string Date time into Python Date time object.
    The datetime method converts the Start Time df to a string Date time
    """  

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    """
    Create a new df named month created from
    The df of Start Time and using the dt.month method which gets the month from date in Pandas
    Create a new df for the day of the week created from
    The df of Start Time using the dt.weekday which gets the name of the day in a week
    """  
    

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
    """
    To take care of the all option use the inverse of the month variable which is the exclamation mark
    If the selection was not all and is valid use one of the elements in the months list
    The month variable indexes the months list
    """   
        
    # filter by month to create the new dataframe
    df = df[df['month'] == month]
    """
    Create a new data frame so the month of the year can be filtered
    """
        
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

    """
    To take care of the all option use the inverse of the day of the week variable which is the exclamation mark
    If the day of the week selection was not all
    Create and filter a df for day of the week to the day and
    Use the title case method to capitalize the first letter of the day
    """

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    """
    time.time is a method for obtaining a floating point number expressed in seconds
    star_time is assigned this
    time and star are numerical floats like 2.0 or 44.6 
    """

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    """
    var created from the df of the moth that occurs most frequently
    .mode The mode() is used to locate the central tendency of numeric or nominal data.
    [0] begins searching the days of the month list at the first entry
    Print produces on the screen the most popular month
    """ 
    
    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)

    """
    var created from the df of the day of the week that occurs most frequently
    .mode The mode() is used to locate the central tendency of numeric or nominal data.
    [0] begins searching the days of the week list at the first entry
    Print produces on the screen the most popular month
    """

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    """
    df for hour is created from the df 
    dt.hour  access the values of the series
    var created from df that displays the most frequent hour starting at the first value denoted by zero
    """  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    """
    Output is a result of the 
    Print statement outputs a line of stars as a separator
    """ 
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nThe Most Popular Stations and Trip are...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe most commonly used start station is:', common_start_station)

    """
    Variable Start Station is created from a dataframe that counts the unique values
    Idxmax gets the row label of the maximum value
    Print shows the string with the start station with the max value
    The output will show the station the customer started at most frequently 
    """ 
    
    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly visited end station is:', common_end_station)

    """
    Variable End Station is created from a dataframe that counts the unique values
    Idxmax gets the row label of the maximum value
    Print shows the string with the end station with the max value
    """

    # TO DO: display most frequent combination of start station and end station trip

    combo_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', common_start_station, " & ", common_end_station)


    print("\nThe number of seconds taken between the most common end and start stations was %s seconds." % (time.time() - start_time))
    print('-'*40)


    """
    Print string text along with the time minus the start time
    Print statement outputs a line of stars as a separator
    """ 

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    travel_time_total = sum(df['Trip Duration'])
    print('Total travel time:', travel_time_total/86400, " Days")

    """
    Variable created by summing the df of Trip Duration
    Print string text that also shows the total travel time divided by the total number of seconds in the Day
    """ 

    # TO DO: display mean travel time

    avg_travel_time = df['Trip Duration'].mean()
    print('Average time of travel:', avg_travel_time/60, "Minutes")

    """
    Variable created by averaging the trip duration
    Print string text that also shows the average/mean divided by the number of minutes in an hour
    The output will be a float result
    """  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_type_count = df['User Type'].value_counts()
    #print(user_type_count)
    print('User Types:\n', user_type_count)
    
    """
    Var created from df from the unique values of the user types
    """ 

    # TO DO: Display counts of gender

    try:
      gender_counts = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_counts)
    except KeyError:
      print("\nGender Types:\nData not available.")
    
    """
    Using a try to run this block of code
    Var for gender count created from df that counts unique values and prints it
    The except error accounts for anything outside of the data in our df based on the month
    """

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      earliest_year = df['Birth Year'].min()
      print('\nEarliest Year:', earliest_year)
    except KeyError:
      print("\nEarliest Year:\nData not available for this month.")

    """
    Using a try to run this block of code
    Var for the earliest year minimum created from df that gets the earliest year of birth
    The except error accounts for anything outside of the data in our df based on the month
    """  
    
    try:
      recent_year = df['Birth Year'].max()
      print('\nMost Recent Year:', recent_year)
    except KeyError:
      print("\nMost Recent Year:\nData not available for this year.")
        
    """
    Using a try to run this block of code
    Var for the max/most recent year
    The except error accounts for anything outside of the data in our df based on the month
    """

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    """
    Using a try to run this block of code
    Var for the most common birth year
    The except error accounts for anything outside of the data in our df 
    The result will be an error if the customer does not select the correct result
    """   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no to see raw data.\n')
        if restart.lower() != 'yes':
            break

#Show raw data, 5 rows at a time
    see_data = "1"
    i = 0
    while(see_data != "2"):
        print(df[i:i+5])
        i += 5
        print("enter 1 for more 5 rows")
        print("enter 2 to exit")
        see_data = input("enter the number")
        
    """
    created a var and set it to 1
    established and var to increment
    While loop will run unless 2 is entered and that will break the loop
    While loop prints 5 lines of raw data 
    Incrementing by 5 rows will be shut down at any time
    i increments the raw data by 5 rows if 1 is selected
    """
            
            
            
if __name__ == "__main__":
    main()

   