def sum_for_list(lst):
    tempSums = []
    tempPrimes = []
    divisorList = []
    total = []
    count = 2
    while count < max(lst) / 2:   
        for part in lst:
            if part % count == 0 and part not in tempPrimes:
                tempPrimes.append(count)
            
                tempSums.append(part)



                



test = [12, 15]
test2 = [15, 21, 24, 30, 45]
sum_for_list(test)