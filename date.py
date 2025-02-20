from datetime import datetime, timedelta

def date():
    # Get the current date
    current_date = datetime.now()

    # Calculate the first day of the current month
    first_day_of_month = current_date.replace(day=1)

    # Calculate the start and end of the previous week
    start_of_previous_week = (current_date - timedelta(days=current_date.weekday() + 7))  # Previous Monday
    end_of_previous_week = start_of_previous_week + timedelta(days=6)  # Previous Sunday

    # Ensure the start of the week doesn't precede the first day of the month
    if start_of_previous_week < first_day_of_month:
        start_of_previous_week = first_day_of_month

    # Calculate the week number within the month
    previous_week_number = ((start_of_previous_week - first_day_of_month).days // 7) + 1

    # Get the month name of the previous week
    previous_week_month_name = start_of_previous_week.strftime("%B")

    # Output variables
    date_from = start_of_previous_week.strftime("%Y-%m-%d")
    date_to = end_of_previous_week.strftime("%Y-%m-%d")
    
    return date_from,date_to,previous_week_number,previous_week_month_name

