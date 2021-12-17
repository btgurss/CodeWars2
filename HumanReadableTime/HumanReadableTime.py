# Function to change number of seconds in hours, minutes, and seconds written in form 00:00:00

def make_readable(seconds):
    # Holder variable for string
    human = ""

    # Checking number if number of seconds will result in any hours
    if seconds >= 3600:

        # Declaring holder variable to find number of hours
        temp = int(seconds/3600)

        # Using if statement to determine how to write in new amounts
        if temp > 9:
            human = human + str(temp) + ":"
        else:
            human = human + "0" + str(temp) + ":"
        # Subtracting hours from seconds to get new amount for minutes and seconds
        seconds = seconds - temp * 3600
    else:
        human = human + "00:"

    if seconds >= 60:
        temp = int(seconds/60)
        if temp > 9:
            human = human + str(temp) + ":"
        else:
            human = human + "0" + str(temp) + ":"
        seconds = seconds - temp * 60
    else:
        human = human + "00:"


    if seconds == 0:
        human = human + "00"
    elif seconds < 10:
        human = human + "0" + str(seconds)
    else:
        human = human + str(seconds)
    
    return human

make_readable(0)
make_readable(359999)