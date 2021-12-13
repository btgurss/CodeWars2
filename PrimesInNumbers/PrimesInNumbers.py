# Writing ou prime factorizations of numbers
def prime_factors(n):
    
    # Variable to divide by each factor
    temp = n

    # Array to hold all prime factors
    factors = []

    # Number to try to divide by - will increase as move along
    count = 2

    # Loop to find all prime factors
    while temp > 1:

        # Using if statement to determine remainders or not
        if temp % count == 0:
            factors.append(count)
            temp = temp // count
            print(temp)
        else:
            count = count + 1
    print(factors)
    prime = ""

    # Using for loop to set up written factor list
    for i in range(len(factors)):

        # Using if/else to write in different factors
        if i == 0:
            newCount = 1
        elif factors[i] == factors [i-1]:
            newCount += 1
        elif newCount > 1:
            prime = prime + "(" + str(factors[i-1]) + "**" + str(newCount) + ")"
            newCount = 1
        elif newCount == 1 and (i < len(factors)):
            prime = prime + "(" + str(factors[i-1]) + ")"
    
    # Using if/else to put in last factor
    if newCount > 1:
        prime = prime + "(" + str(factors[len(factors) - 1]) + "**" + str(newCount) + ")"
    else:
        prime = prime + "(" + str(factors[len(factors) - 1]) + ")"
    return (prime)

test = 68
test2 = 7775460
test3 = 86240
prime_factors(test3)