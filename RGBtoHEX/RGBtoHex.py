# Function to convert numbers to hexidecimal system for colors

def rgb(r, g, b):
    # Setting hex for inputs
    hex = ""
    # Creating list from inputs
    list = [r, g, b]

    # Looping through inputs in the list
    for number in list:

        # Using if/else for special instances
        if number > 255:
            number = 255
        elif number < 0:
            number = 0

        # Using if to determine if calculations need to be done
        if number > 16:

            # Dividing number by 16
            temp = number / 16

            # Looping through twice
            for i in range(2):
                print(temp)
                print(hex)
                # Using if/elifs to change number to hecidimal equivalent
                if temp < 10:
                    hex = hex + str(int(temp))
                elif temp >= 15:
                    hex = hex + "F"
                elif temp >= 14:
                    hex = hex + "E"
                elif temp >= 13:
                    hex = hex + "D"
                elif temp >= 12:
                    hex = hex + "C"
                elif temp >= 11:
                    hex = hex + "B"
                elif temp >= 10:
                    hex = hex + "A"
                temp = number % 16
        else:
            hex = hex + "0"
            if number < 10:
                hex = hex + str(number)
            elif number >= 15:
                hex = hex + "F"
            elif number >= 14:
                hex = hex + "E"
            elif number >= 13:
                hex = hex + "D"
            elif number >= 12:
                hex = hex + "C"
            elif number >= 11:
                hex = hex + "B"
            elif number >= 10:
                hex = hex + "A"
    return hex

rgb(0, 0, 0)
rgb(1, 2, 3)
rgb(254, 253, 252)
print(rgb(-20, 275, 125))