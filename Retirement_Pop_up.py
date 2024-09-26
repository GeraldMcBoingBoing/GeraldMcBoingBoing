import datetime
import ctypes

def calculate_workdays_until_retirement(start_date, retirement_date):
    today = datetime.date.today()
    remaining_days = (retirement_date - today).days
    
    # Calculate weekends
    weekends = remaining_days // 7 * 2
    
    # Adjust for weekdays
    remaining_days -= weekends
    
    # Adjust for public holidays if necessary
    
    return remaining_days

def show_reminder(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Retirement Countdown", 0x40)

def main():
    # Set date of birth and retirement age
    date_of_birth = datetime.date(1973, 5, 20)  # Change this to your date of birth
    retirement_age = 65  # Change this to your desired retirement age
    
    # Calculate retirement date
    retirement_date = date_of_birth.replace(year=date_of_birth.year + retirement_age)
    
    # Calculate remaining workdays until retirement
    remaining_days = calculate_workdays_until_retirement(datetime.date.today(), retirement_date)
    
    if remaining_days > 0:
        message = f"You have {remaining_days} work days left before retirement!"
        show_reminder(message)
    else:
        message = "Congratulations! You've reached retirement!"
        show_reminder(message)

if __name__ == "__main__":
    main()
