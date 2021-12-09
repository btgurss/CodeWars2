# Changing letters in a string to letters 13 after in the alphabet - Code breaking

def rot13(message):
    # Setting variable for new string
    new_message = ""
    # Looping through letters of the string
    for i in message:
        # Changing letters to corresponding numbers
        x = ord(i)
        # Checking for upper or lower case
        if x >= 65 and x <= 90:
            # Adding 13 to number
            x = x + 13
            # Checking and calculating if number goes beyond z value
            if x > 90:
                x = x - 90 + 64
        elif x >= 97 and x <= 122:
            x = x + 13
            if x > 122:
                x = x - 122 + 96
        # Changing number back to letter
        new = chr(x)
        # Concatenating the new messages
        new_message = new_message + new
    return(new_message)
test = "Test3&"
print(rot13(test))