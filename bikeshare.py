import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).

    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("\n enter a city:Chicago, New york city, Washington \n").lower()

        if city in cities:
            break
        else:
            print("\n Sorry, we do not have information about this city")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['January', 'February', 'March', 'April', 'June', 'May', 'None']
        month = input("\n Which month would you like to explore? "
                      "(January, February, March, April, May, June)? Type 'None' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a different month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'None']
        day = input("\n choose your day:Monday, Tuesday, Wednesday, Thursday, "
                    "Friday, Saturday, Sunday)? Type 'None' for no day filter \n").title()
        if day in days:
            break
        else:
            print("\n Please choose a different day")

    print('-' * 20)

    if month == '' and day == '':
        return city, months, days
    elif month == '' and day != '':
        return city, months, day
    elif month != '' and day == '':
        return city, month, day
    else:
        return city, month, day

    city, month, day = get_filters()

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
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    month=month.lower()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common Month (1 = January,...,6 = June): {common_month}")

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print(f"\nMost common Day: {common_day}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour

    hr = df['Hour'].mode()[0]

    if hr <= 12:
        print('\nMost common start hour is: {} AM'.format(hr))
    else:
        print('\nMost common start hour is: {} PM'.format(hr % 12))

    print('-' * 20)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {commonly_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + "to" + " " + df['End Station']
    mused_com = df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(mused_com))

    print('-' * 20)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ', sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print('mean travel time: ', df['Trip Duration'].mean())

    print('-' * 20)


def display_data(df):
    while True:
        response = ['yes', 'no']
        choice = input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice == 'yes':
                start = 0
                end = 5
                data = df.iloc[start:end, :9]
                print(data)
                break
            break
        else:
            print("Please enter a valid response")
    if choice == 'yes':
        while True:
            choice_2 = input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
            if choice_2 in response:
                if choice_2 == 'yes':
                    start += 5
                    end += 5
                    data = df.iloc[start:end, :9]
                    print(data)
                    break
                else:
                    break
            else:
                print("Please enter a valid response")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('counts of gender: ', df['Gender'].value_counts())
    except:
        print('chicago has no "Gender" informations')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('earliest year of birth: ', min(df['Birth Year']))
        print('most recent year of birth: ', max(df['Birth Year']))
        print('most common year of birth: ', df['Birth Year'].mode())
    except:
        print('washington has no "year of birth" info')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
