# All the test cases provided were downloaded and tested. Every test case passed with the following code.

# overview of calculating the max number of inputPatients that can receive blood given the number of blood units:
    # For O- inputPatients, the max number is the min of available O- blood units and the number of O- inputPatients.
    # For O+ inputPatients, the max number is the # of available O- units and the remaining O+ blood units.
    # For A- inputPatients, the max number is the # of available A- blood units and remaining O- blood units.
    # For A+ inputPatients, the max number is the # of available A+ blood units, plus remaining A- and O- blood units.

    # and so on the pattern continues...

    # B- takes blood units from B-, and remaining blood units from O-
    # B+ takes blood units from B+ and remaining blood units from B-, O+, and O-
    # AB- takes blood units from AB+ and remaining blood units from A-, B-, and O-
    # AB+ takes blood units from AB- and remaining blood units from all other remaining units

def maxOMinus(inputUnits, inputPatients):
    value = min(inputUnits[0], inputPatients[0])
    inputUnits[0] -= value
    inputPatients[0] -= value

def maxOPlus(inputUnits, inputPatients):
    value = min(inputUnits[1], inputPatients[1])
    inputUnits[1] -= value
    inputPatients[1] -= value
    if inputPatients[1] > 0 and inputUnits[0] > 0:
        value = min(inputUnits[0], inputPatients[1])
        inputUnits[0] -= value
        inputPatients[1] -= value

def maxAMinus(inputUnits, inputPatients):
    value = min(inputUnits[2], inputPatients[2])
    inputUnits[2] -= value
    inputPatients[2] -= value
    if inputPatients[2] > 0 and inputUnits[0] > 0:
        value = min(inputUnits[0], inputPatients[2])
        inputUnits[0] -= value
        inputPatients[2] -= value

def maxAPlus(inputUnits, inputPatients):
    value = min(inputUnits[3], inputPatients[3])
    inputUnits[3] -= value
    inputPatients[3] -= value
    while inputPatients[3] > 0 and (inputUnits[2] > 0 or inputUnits[1] > 0 or inputUnits[0] > 0):
        if inputUnits[2] > 0:
            val1 = min(inputUnits[2], inputPatients[3])
            inputUnits[2] -= val1
            inputPatients[3] -= val1
        elif inputUnits[1] > 0:
            val2 = min(inputUnits[1], inputPatients[3])
            inputUnits[1] -= val2
            inputPatients[3] -= val2
        elif inputUnits[0] > 0:
            val3 = min(inputUnits[0], inputPatients[3])
            inputUnits[0] -= val3
            inputPatients[3] -= val3

def maxBMinus(inputUnits, inputPatients):
    value = min(inputUnits[4], inputPatients[4])
    inputUnits[4] -= value
    inputPatients[4] -= value
    if inputPatients[4] > 0 and inputUnits[0] > 0:
        value = min(inputUnits[0], inputPatients[4])
        inputUnits[0] -= value
        inputPatients[4] -= value

def maxBPlus(inputUnits, inputPatients):
    value = min(inputUnits[5], inputPatients[5])
    inputUnits[5] -= value
    inputPatients[5] -= value
    while inputPatients[5] > 0 and (inputUnits[4] > 0  or inputUnits[1] > 0 or inputUnits[0] > 0):
        if inputUnits[4] > 0:
            val1 = min(inputUnits[4], inputPatients[5])
            inputUnits[4] -= val1
            inputPatients[5] -= val1
        elif inputUnits[1] > 0:
            val2 = min(inputUnits[1], inputPatients[5])
            inputUnits[1] -= val2
            inputPatients[5] -= val2
        elif inputUnits[0] > 0:
            val3 = min(inputUnits[0], inputPatients[5])
            inputUnits[0] -= val3
            inputPatients[5] -= val3

def maxABMinus(inputUnits, inputPatients):
    value = min(inputUnits[6], inputPatients[6])
    inputUnits[6] -= value
    inputPatients[6] -= value
    while inputPatients[6] > 0 and (inputUnits[4] > 0 or inputUnits[2] > 0 or inputUnits[0] > 0):
        if inputUnits[4] > 0:
            val1 = min(inputUnits[4], inputPatients[6])
            inputUnits[4] -= val1
            inputPatients[6] -= val1
        elif inputUnits[2] > 0:
            val2 = min(inputUnits[2], inputPatients[6])
            inputUnits[2] -= val2
            inputPatients[6] -= val2
        elif inputUnits[0] > 0:
            val3 = min(inputUnits[0], inputPatients[6])
            inputUnits[0] -= val3
            inputPatients[6] -= val3

def maxABPlus(inputUnits, inputPatients):
    value = min(inputUnits[7], inputPatients[7])
    inputUnits[7] -= value
    inputPatients[7] -= value
    while inputPatients[7] > 0 and (inputUnits[6] > 0 or inputUnits[5] > 0 or inputUnits[4] > 0 or
                                    inputUnits[3] > 0 or inputUnits[2] > 0 or inputUnits[1] > 0 or
                                    inputUnits[0] > 0):
        if inputUnits[6] > 0:
            val1 = min(inputUnits[6], inputPatients[7])
            inputUnits[6] -= val1
            inputPatients[7] -= val1
        elif inputUnits[5] > 0:
            val2 = min(inputUnits[5], inputPatients[7])
            inputUnits[5] -= val2
            inputPatients[7] -= val2
        elif inputUnits[4] > 0:
            val3 = min(inputUnits[4], inputPatients[7])
            inputUnits[4] -= val3
            inputPatients[7] -= val3
        elif inputUnits[3] > 0:
            val4 = min(inputUnits[3], inputPatients[7])
            inputUnits[3] -= val4
            inputPatients[7] -= val4
        elif inputUnits[2] > 0:
            val5 = min(inputUnits[2], inputPatients[7])
            inputUnits[2] -= val5
            inputPatients[7] -= val5
        elif inputUnits[1] > 0:
            val6 = min(inputUnits[1], inputPatients[7])
            inputUnits[1] -= val6
            inputPatients[7] -= val6
        elif inputUnits[0] > 0:
            val7 = min(inputUnits[0], inputPatients[7])
            inputUnits[0] -= val7
            inputPatients[7] -= val7

# run the program and give the two lines of input of 8 numbers for each line
def maxNumberOfinputPatients():
    # get first and second line of input of 8 integers each
    inputUnits = list(map(int, input().split()))
    inputPatients = list(map(int, input().split()))

    previousTotal = sum(inputPatients)

    # for O-
    maxOMinus(inputUnits, inputPatients)

    # for O+
    maxOPlus(inputUnits, inputPatients)

    # for A-
    maxAMinus(inputUnits, inputPatients)

    # for A+
    maxAPlus(inputUnits, inputPatients)

    # for B-
    maxBMinus(inputUnits, inputPatients)

    # for B+
    maxBPlus(inputUnits, inputPatients)

    # for AB-
    maxABMinus(inputUnits, inputPatients)

    # for AB+
    maxABPlus(inputUnits, inputPatients)

    newTotal = sum(inputPatients)
    maxNumber = previousTotal - newTotal

    return maxNumber

result = maxNumberOfinputPatients()
print(result)


