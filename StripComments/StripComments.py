# Function to delete words on each line after a comment character

def solution(string, markers):
    test = ""
    count = 0
    spaceCounter = 0
    for letter in string:
        if letter not in markers and count == 0:
            test = test + letter
        elif letter in markers:
            count += 1        
        elif letter == " " and count == 1 and spaceCounter > 0:
            count = 0
        elif letter == " ":
            spaceCounter += 1
        elif count == 1:
            spaceCounter = 0
    print(test)

            


test = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ['#', '!']
solution(test, markers)