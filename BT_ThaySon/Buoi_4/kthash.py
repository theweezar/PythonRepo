import hashlib
import sys
import os
import sqlite3

def createTable():
    con = sqlite3.connect('kthash.db')
    cur = con.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS kthash
    (
        _path TEXT,
        _file TEXT
    )
    """
    cur.execute(sql)
    con.commit()
    con.close()

def insert(path, file):
    sql = f"""
    INSERT INTO kthash VALUES ('{path}','{file}')
    """

def queryAll():
    con = sqlite3.connect('kthash.db')
    cur = con.cursor()
    sql = """
    SELECT * FROM kthash
    """
    cur.execute(sql)
    con.commit()
    con.close()

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

def dirWalk(path):
    _all = next(os.walk(path), (None, None, []))
    _dirPath = _all[0]
    if _dirPath is not None:
        _dirs = _all[1]
        _files = _all[2]

        for _file in _files:
            print(path, ': ', _file)
        for _dir in _dirs:
            _pathCdDir = path + "/" + _dir
            dirWalk(_pathCdDir)
    else:
        print("Can not find path")

def main():
    argv = sys.argv
    mode = argv[1]

    if mode == "-d" or mode == "--directory" and argv[2] is not None:
        dirWalk(argv[2])
        
if __name__ == "__main__":
    main()
