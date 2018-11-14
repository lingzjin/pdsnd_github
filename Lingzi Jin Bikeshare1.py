import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/king/Documents/Workhard/bikeshare-2/chicago.csv',
              'new york city': '/Users/king/Documents/Workhard/bikeshare-2/new_york_city.csv',
              'washington': '/Users/king/Documents/Workhard/bikeshare-2/washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
def load_data(city, month, day):

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True: 
        city = input('Which city do you want to explore Chicago, New York City or Washington? \n> ').lower()
        if city in CITIES: 
            break
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York City, or Washington.')
        
       # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input('All right now it\'s time to provide us a month name or just say \'all\' to apply no month filter \n>').lower()
        if month in MONTHS:
            break
        else:
            print('Sorry, I do not understand your input.')
        
    while True:        
        day = input('Please enter the day of the week or just say \'all\' again to apply no day filter \n>').lower()
        if day in DAYS:
            break
        else:
            print('Sorry, I do not understand your input.')

    print('-'*40)
    return city, month, day


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
    file_name = CITY_DATA[city]
    print("Accessing data from: " + file_name)
    df = pd.read_csv(file_name)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
   # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
   # filter by day of week if applicable
    if day != 'all':
       #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]   
  
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is: ", most_common_month)
    
    # Display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is: ", most_common_day_of_week)
    
    # Display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: ", most_common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station: {}, {}"\
          .format(most_common_start_end_station[0], most_common_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    print('\nDifferent types of users are: ', user_counts)
    
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("The earliest birth year: ", int(earliest_birth_year))   
        print("The most recent birth year:", int(most_recent_birth_year))
        print("The most common birth year: ", int(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df, line_no):
    """Display filtered data."""
    while True:        
        view_data = input('Do you want to see raw data? Enter yes or no. \n>').lower()
        count = df['Start Time'].count()
        if view_data.lower() == 'yes':
            if count <= line_no:
                print('\nFinished printing all filtered data')
                break
            else:
                print(df.iloc[line_no: line_no+5])
                line_no += 5
        elif view_data.lower() == 'no':
            break
        else:
            print('\nInvalid option. Please try again.')
            return raw_data(df, line_no)

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
     
        
        
