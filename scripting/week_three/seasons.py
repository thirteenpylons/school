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
    if month not in {'January', 'February', 'March', 'April', 'May', 'June', 
                     'July', 'August', 'September', 'October', 'November', 'December'}:
        return 'Invalid'
        
    if day not in range(1, 32):  # No month has more than 31 days, so this is a simple check
        return 'Invalid'
    
    # Define the seasons with date ranges
    seasons = {
        'Spring': [('March', 20, 31), ('April', 1, 30), ('May', 1, 31), ('June', 1, 20)],
        'Summer': [('June', 21, 30), ('July', 1, 31), ('August', 1, 31), ('September', 1, 21)],
        'Autumn': [('September', 22, 30), ('October', 1, 31), ('November', 1, 30), ('December', 1, 20)],
        'Winter': [('December', 21, 31), ('January', 1, 31), ('February', 1, 29), ('March', 1, 19)]
    }
    
    # Check for February in non-leap years
    if month == 'February' and day > 28:
        return 'Invalid'
    
    for season, ranges in seasons.items():
        for start_month, start_day, end_day in ranges:
            if month == start_month and start_day <= day <= end_day:
                return season
    
    return 'Invalid'

def main():
    month = input("Enter the month: ")
    day = int(input("Enter the day: "))

    print(determine_season(month, day))

if __name__ == "__main__":
    main()
