import re

def readFile(fileName):
    outputStr = ""
    try:
        outputFile = open(fileName, "r")
        outputStr = outputFile.read()
        outputFile.close()
    except:
        print("File not exist!!!")
    return outputStr

def parseStringToOneLine(stringData):
    return str(stringData).strip().replace("\n", " ")

def createPattern(keywords):
    wordList = keywords.split(" ")
    pattern = ""
    for word in wordList:
        pattern += f"({word}|({word}\s+))"
    if pattern[::-1] == '|':
        pattern = pattern[0:-1]
    return pattern

def findWord(keywords, data):
    pattern = createPattern(keywords)
    print("Pattern:", pattern)
    foundIterator = re.finditer(pattern, data)
    return foundIterator

def findWordAndReplace(keywords, data, replace):
    pattern = createPattern(keywords)
    print("Pattern:", pattern)
    return re.sub(rf"{pattern}", replace, data)

def run(mode = 1):
    dataSrc = readFile("./vanban.txt")
    dataParse = parseStringToOneLine(dataSrc)
    keywords = input('Nhap tu khoa: ')
    if mode == 1:
        foundIterator = findWord(keywords, dataParse)
        print("Ket qua tim kiem:")
        for found in foundIterator:
            print(found)
    elif mode == 2:
        replace = input('Nhap cum tu de thay doi: ')
        result = findWordAndReplace(keywords, dataParse, replace)
        print(result)

run(2)