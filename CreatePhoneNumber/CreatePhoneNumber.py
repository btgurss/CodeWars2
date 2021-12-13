def create_phone_number(n):
    
    # Creating counter to loop through digits
    count = 0

    # String to hold number
    phone = ""

    # Looping through digits
    for digit in n:

        # If statements to put in needed numbers and symbols
        if count == 0:
            phone = phone + "(" 
        if count == 3:
            phone = phone + ") " 
        if count == 6:
            phone = phone + "-"
        phone = phone + str(digit)
        count += 1
    return (phone)

test = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number(test)

