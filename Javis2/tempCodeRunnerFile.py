import datetime

def get_current_date():
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return current_date

def get_current_day():
    # Get current day
    current_day = datetime.datetime.now().strftime("%A")
    return current_day

def get_current_time():
    # Get current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

def print_current_date_and_time():
    # Get current date, day, and time
    date = get_current_date()
    day = get_current_day()
    time = get_current_time()

    # Print date, day, and time in a single line
    print("Today's date is", date, "current time is", time, "and today's is", day)

