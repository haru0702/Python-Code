from datetime import datetime

def months_calc():
    start_date_str = input("Start Date of your relationship (YYYY-MM-DD): ")  # Month - Day - Year
    s_date = datetime.strptime(start_date_str, '%Y-%m-%d') # convert string input into datetime format

    curr_date = datetime.now() # getting the current date

    months_difference = (curr_date.year - s_date.year) * 12 + curr_date.month - s_date.month # getting the difference of the months
    print(f"You've had {months_difference} monthsaries since {start_date_str}.") # display the result

# Call the function
months_calc()
