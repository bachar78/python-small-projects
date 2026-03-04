


def calculate_minutes(age):
    days_in_year = 365.25
    hours_in_day = 24
    minutes_in_hour = 60

    total_days = age * days_in_year
    total_hours = total_days * hours_in_day
    total_minutes = total_hours * minutes_in_hour
    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        user_age = float(input("Enter your age in years: "))
        days, hours, minutes = calculate_minutes(user_age)
        print(f"You have been alive for approximately {days} days, {hours} hours, and {minutes} minutes.")
        
        again = input("Would you like to calculate for another age? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")