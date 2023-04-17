import datetime

# Define a list of available dates for the appointments
available_dates = ["April 19", "April 20", "April 21", "April 22", "April 23"]

# Define a dictionary of available time slots for each date
available_times = {
    "April 19": ["10:00 AM", "11:00 AM", "12:00 PM", "2:00 PM", "3:00 PM"],
    "April 20": ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM"],
    "April 21": ["11:00 AM", "12:00 PM", "1:00 PM", "3:00 PM", "4:00 PM"],
    "April 22": ["10:00 AM", "11:00 AM", "12:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"],
    "April 23": ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM"],
}

# Define a function to check if a given date is available
def is_available_date(date):
    if date in available_dates:
        return True
    else:
        return False

# Define a function to check if a given time slot is available on a given date
def is_available_time(date, time):
    if time in available_times[date]:
        return True
    else:
        return False

# Define a function to book an appointment
def book_appointment(name, date, time):
    if is_available_date(date) and is_available_time(date, time):
        print("Appointment booked for {} on {} at {}.".format(name, date, time))
        available_times[date].remove(time)
    else:
        print("Sorry, that appointment time is not available.")

# Define a function to show the available dates and times
def show_available_dates():
    print("Available dates:")
    for date in available_dates:
        print(date)
        print("Available times:")
        for time in available_times[date]:
            print(time)
        print()

# Define a function to ask the user for input
def get_user_input():
    name = input("What is your name? ")
    date = input("What date would you like to book an appointment? ")
    time = input("What time would you like to book an appointment? ")
    return name, date, time

# Define the main function to run the chatbot
def run_chatbot():
    print("Welcome to the appointment chatbot!")
    show_available_dates()
    name, date, time = get_user_input()
    book_appointment(name, date, time)
    print("Thank you for using the appointment chatbot!")

# Run the chatbot
run_chatbot()


