import math
import random

def getRandomNumberShuffle():
    array = [1,2,3,4,5,6,7,8,9,0]
    random.shuffle(array)
    return int(''.join([str(e) for e in array[0:random.randrange(1, 10)]]))

def getRandomNumber():
    return math.floor(random.random() * 10000)
    
def getRandomColumn(length):
    columnStr = ""
    for i in range(0, length):
        # columnStr += str(getRandomNumber()) + "\n"
        columnStr += str(getRandomNumberShuffle()) + "\n"
    return columnStr

def writeFile(fileName, inputStr):
    inputFile = open(fileName, "w+")
    inputFile.write(inputStr)
    inputFile.close()

def readFile(fileName):
    outputStr = ""
    try:
        outputFile = open(fileName, "r")
        outputStr = outputFile.read()
        outputFile.close()
    except:
        print("File not exist!!!")
    return outputStr

def writeRandomToFile():
    writeFile("./solieu.txt", getRandomColumn(100))

def calculateNumberLine(number):
    result = 0
    numberLength = len(number)
    if (numberLength > 0):
        for i in range(0, numberLength):
            result += int(number[i])
    return result

def readNumberColumn():
    numberData = readFile("./solieu.txt")
    dataToWrite = ""
    sumAll = 0
    if len(numberData) != 0:
        numberList = numberData.split('\n')
        print("List:\n", numberList, "\n\nCount:", len(numberList))

        for i in range(0, len(numberList)):
            number = numberList[i]
            if (len(number) > 0):
                dataToWrite += number + " ---> Sum = " + str(calculateNumberLine(number)) + "\n"
                sumAll += int(number)
    
    # print(dataToWrite)
    # print("Sum all =", sumAll)
    writeFile("./linetotal.txt", dataToWrite)

if __name__ == '__main__':
    writeRandomToFile()
    readNumberColumn()
    # print(getRandomNumberShuffle())