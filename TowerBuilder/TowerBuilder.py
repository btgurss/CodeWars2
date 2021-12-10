def tower_builder(n_floors):
    # Counter while loop
    count = 0
    # Counter for spaces
    count2 = n_floors
    # Array set up to hold final answer
    builder = []
    # Using while loop to count through number of floors
    while count < n_floors:
        # Setting temporary variable to hold string before putting into list
        temp = ""
        # Using for loops to put spaces and * values
        for i in range (count2 - 1):
            temp = temp + " "
        for i in range(2 * count + 1):
            temp = temp + "*"
        for i in range (count2 - 1):
            temp = temp + " "
        # Adding temporary string to list
        builder.append(temp)
        # Counting
        count += 1
        count2 = count2 - 1
    return(builder)
test = 3
tower_builder(test)