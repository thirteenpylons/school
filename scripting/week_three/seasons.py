"""

Write a program that takes a date as input and outputs the date's season. 
The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11
the output is:

Spring
In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65
the output is:

Invalid 
The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

"""

def determine_season(month: str, day: int) -> str:
    """
    Determine the season based on month and day.
    """
    # Define a dictionary with month as key and (start day, end day, season) as values
    seasons = {
        'January': (1, 31, 'Winter'),
        'February': (1, 29, 'Winter'),  # 29 to account for leap years, but additional check needed
        'March': (1, 19, 'Winter'),
        'March': (20, 31, 'Spring'),
        'April': (1, 30, 'Spring'),
        'May': (1, 31, 'Spring'),
        'June': (1, 20, 'Spring'),
        'June': (21, 30, 'Summer'),
        'July': (1, 31, 'Summer'),
        'August': (1, 31, 'Summer'),
        'September': (1, 21, 'Summer'),
        'September': (22, 30, 'Autumn'),
        'October': (1, 31, 'Autumn'),
        'November': (1, 30, 'Autumn'),
        'December': (1, 20, 'Autumn'),
        'December': (21, 31, 'Winter')
    }
    
    # Check for February in leap years
    if month == 'February' and day == 29:
        if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return 'Invalid'

    # Check if month is valid
    if month in seasons:
        start_day, end_day, season = seasons[month]
        if start_day <= day <= end_day:
            return season

    return 'Invalid'

def main():
    month = input()
    day = int(input())

    print(determine_season(month, day))

if __name__ == "__main__":
    main()
