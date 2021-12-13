# This function takes numbers and converts them to roman numerals - To make it shorter, I would create a dictionary
# to hold different letters as the numbers get smaller

def solution(n):
    # Variable to hold new string
    roman = ""
    # Variable to count digits
    count = 0
    # For statement to count number of digits
    for digit in str(n):
        count += 1
    # Looping through digits
    for digit in str(n):
        # Checking value of each individual digit and placing new value into string as needed.
        if count == 4:
            for i in range(int(digit)):
                roman = roman + "M"
        elif count == 3:
            if int(digit) > 8:
                for i in range(10 - int(digit)):
                    roman = roman + "C"
                roman = roman + "M"
            elif (int(digit) > 5):
                roman = roman + "D"
                for i in range(int(digit) - 5):
                    roman = roman + "C"
            elif (int(digit) == 5):
                roman = roman + "D"
            elif (int(digit) > 3):
                for i in range(5 - int(digit)):
                    roman = roman + "C"
                roman = roman + "D"
            elif (int(digit) > 0):
                for i in range(int(digit)):
                    roman = roman + "C"

        elif count == 2:
            if int(digit) > 8:
                for i in range(10 - int(digit)):
                    roman = roman + "X"
                roman = roman + "C"
            elif (int(digit) > 5):
                roman = roman + "L"
                for i in range(int(digit) - 5):
                    roman = roman + "X"
            elif (int(digit) == 5):
                roman = roman + "L"
            elif (int(digit) > 3):
                for i in range(5 - int(digit)):
                    roman = roman + "X"
                roman = roman + "L"
            elif (int(digit) > 0):
                for i in range(int(digit)):
                    roman = roman + "X"

        else:
            if int(digit) > 8:
                for i in range(10 - int(digit)):
                    roman = roman + "I"
                roman = roman + "X"
            elif (int(digit) > 5):
                roman = roman + "V"
                for i in range(int(digit) - 5):
                    roman = roman + "I"
            elif (int(digit) == 5):
                roman = roman + "V"
            elif (int(digit) > 3):
                for i in range(5 - int(digit)):
                    roman = roman + "I"
                roman = roman + "V"
            elif (int(digit) > 0):
                for i in range(int(digit)):
                    roman = roman + "I"
        count = count - 1         
    return roman

test = 1
test2 = 354
test3 = 2352
solution(984)