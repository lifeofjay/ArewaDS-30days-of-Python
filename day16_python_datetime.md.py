from datetime import datetime, timedelta

#Get the current day, month, year, hour, minute, and timestamp
current_datetime = datetime.now()
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_timestamp = current_datetime.timestamp()

print(f"Current Day: {current_day}")
print(f"Current Month: {current_month}")
print(f"Current Year: {current_year}")
print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Current Timestamp: {current_timestamp}")

#Format the current date
formatted_current_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Current Date: {formatted_current_date}")

#Change the time string to time
time_string = "5 December, 2019"
parsed_time = datetime.strptime(time_string, "%d %B, %Y")
print(f"Parsed Time: {parsed_time}")

# Calculate the time difference between now and new year
new_year = datetime(current_year + 1, 1, 1)
time_difference_to_new_year = new_year - current_datetime
print(f"Time difference to New Year: {time_difference_to_new_year}")

#Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
time_difference_to_epoch = current_datetime - epoch
print(f"Time difference to Epoch: {time_difference_to_epoch}")

  #Examples of using the datetime module
# - Time series analysis: Analyzing data over time, making predictions based on historical data.
# - Timestamp for activities: Logging activities in an application to track when they occurred.
# - Adding posts on a blog: Recording and displaying the timestamp of when a blog post was published.


