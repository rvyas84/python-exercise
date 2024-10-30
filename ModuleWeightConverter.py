def lbs_to_kilo(weight):
    return weight*0.45

def kilo_to_lbs(weight):
    return weight/0.45

def printStr():
    print("Thank You!")

def findMaxNumber(listOfNumber):
    maxNum = 0

    for num in listOfNumber:
        if num > maxNum:
            maxNum = num

    return maxNum