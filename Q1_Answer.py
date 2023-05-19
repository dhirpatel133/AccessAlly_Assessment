# All the test cases provided were downloaded and tested. Every test case passed with the following code.

# change the input here to test the program
input = 9514

# hashmap to store all the possible number of arithmetic sequence for each of the 12 hours.
# format -> {1: # of sequences, 2: # of sequences, ... , 12: # of sequences}
hoursHashMap = {}

# populate hashmap for the total number arithmetic sequence for each of the 12 hours
def populateHashMap():
    for i in range(1, 13, 1):
        if i < 10:
            hoursHashMap[i] = arithmeticeSequences_SingleHour(i, 6, 10)
        else:
            hoursHashMap[i] = arithmeticeSequences_DoubleHour(i // 10, i % 10, 6, 10)

# helper function to calculate the number of arithmetic sequences in a one hour digit with certain minutes.
# input format -> 0x:yy means x'th hour and yy minutes
def arithmeticeSequences_SingleHour(hour, minute1, minute2):
    count = 0
    for second_digit in range(minute1):
        for third_digit in range(minute2):
            if third_digit - second_digit == second_digit - hour:
                count += 1
    return count

# helper function to calculate the number of arithmetic sequences in two hour digits with certain minutes.
# input format -> xx:yy means xx'th hour and yy minutes
def arithmeticeSequences_DoubleHour(hour1, hour2, minute1, minute2):
    count = 0
    for second_digit in range(minute1):
        for third_digit in range(minute2):
            if third_digit - second_digit == second_digit - hour2 and hour2 - hour1 == second_digit - hour2:
                count += 1
    return count

# main function to find the total number of arithmetic sequence between 12:00 and the the given number of
# input minutes. Takes input as minutes.
def arithmeticSequence(input):
    populateHashMap()

    # variable to keep track of all the possible arithmetic instances
    instances = 0
    # this is the start hour 12:00 (remember that it's a 12 hour clock)
    currentHour = 12
    # split the minutes into hours and remaining minutes
    hours = input // 60
    minutes = input % 60

    # loop over the number of whole hours and use the values in the hashmap to add onto the instance
    if hours > 1:
        count = 0
        while count < hours:
            instances += hoursHashMap[currentHour]
            if currentHour == 12:
                currentHour = 1
            else:
                currentHour += 1       
            count += 1
    
    # if there are remaining minutes after looping over all the hours, then add the possible arithmetic
    # sequences up until that minute of the current hour. i.e. format -> currentHour:remainingMinutes
    if minutes > 1:
        strMinutes = str(minutes)
        strHour = str(currentHour)

        # call double hour loop if hours is of format xx:yy
        if len(strHour) > 1:
            # pass in values for minute1 and minute2 if format of minutes is xx:yy
            if len(strMinutes) > 1:
                instances += arithmeticeSequences_DoubleHour(int(strHour[0]), int(strHour[1]),
                                                             int(strMinutes[0]) + 1, int(strMinutes[1]) + 1)
            # pass in 1 for minute 1 if format is xx:0y
            else:
                instances += arithmeticeSequences_DoubleHour(int(strHour[0]), int(strHour[1]),
                                                             1, int(strMinutes[0]) + 1)
        # call single hour loop if format of hour is 0x:yy
        else:
            # pass in values for minute1 and minute2 if format is 0x:yy
            if len(strMinutes) > 1:
                instances += arithmeticeSequences_SingleHour(currentHour, int(strMinutes[0]) + 1,
                                                             int(strMinutes[1]) + 1)
            # pass in 1 for minute 1 if format is 0x:0y
            else:
                instances += arithmeticeSequences_SingleHour(currentHour, 1, int(strMinutes[0]) + 1)
    return instances

numberOfArithmeticSequences = arithmeticSequence(input)
print(numberOfArithmeticSequences) # should print 412 as the answer

