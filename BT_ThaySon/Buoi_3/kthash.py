import hashlib
import sys

def readFile(fileName):
    outputStr = ""
    try:
        outputFile = open(fileName, "r")
        outputStr = outputFile.read()
        outputFile.close()
    except:
        print(f"File {fileName} doesn't exist!!!")
    return outputStr

def writeFile(fileName, inputStr):
    inputFile = open(fileName, "w+")
    inputFile.write(inputStr)
    inputFile.close()

def parseStringToOneLine(stringData):
    return str(stringData).strip().replace("\n", " ")
    
def hashMD5(dataStr):
    result = hashlib.md5(dataStr.encode())
    return result.hexdigest()

def main():
    argv = sys.argv
    mode = argv[1]
    textFile = argv[2]
    hashFile = argv[3]

    if mode == "-g" or mode == "--gen":
        _text = readFile(textFile)
        _hash = readFile(hashFile)
        if _text != "":
            _textHash = hashMD5(_text)
            if _hash == "":
                _hash = _textHash
            else:
                _hashArray = _hash.split("\n")
                if _textHash not in _hashArray:
                    _hash += f"\n{_textHash}"
            writeFile(hashFile, _hash)
        else:
            print("File is empty or not exist")
    elif mode == "-c" or mode == "--check":
        _text = readFile(textFile)
        _hash = readFile(hashFile)
        _textHash = hashMD5(_text)
        _hashArray = _hash.split("\n")
        if _textHash in _hashArray:
            print("\nFile is good.")
        else:
            print("\nFile has been changed.")
    else:
        print("use -g or --gen to save hash file\nUse -c or --check to check hash file")

if __name__ == '__main__':
    main()
