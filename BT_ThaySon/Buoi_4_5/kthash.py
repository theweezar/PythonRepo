import hashlib
import sys
import os
import json
from db import KTHashDb

ok = True

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
    
def hashMD5(dataStr: str):
    result = hashlib.md5(dataStr.encode())
    return result.hexdigest()

def dirWalk(dirPathInput, store_list = [], unique = False, database = None):
    _all = next(os.walk(dirPathInput), (None, None, []))
    _dirPathWalk = _all[0]
    if _dirPathWalk is not None:
        _dirs = _all[1]
        _files = _all[2]

        for _file in _files:
            # print(dirPathInput, ': ', _file)
            hash_object = {
                "dir_path": dirPathInput,
                "file_name": _file,
                "hash": hashMD5(dirPathInput + "/" + _file)
            }
            store_list.append(hash_object)
            if unique is True:
                hash_object_db = database.query_where_hash(hash_object["hash"])
                # print(hash_object_db)
                if len(hash_object_db) == 0:
                    print("File has been change at ", dirPathInput + "/" + _file)
                    ok = False
                    return
        for _dir in _dirs:
            _pathCdDir = dirPathInput + "/" + _dir
            dirWalk(_pathCdDir, store_list, unique=unique, database=database)
    else:
        print("Can not find path")
    return store_list

def main():
    argv = sys.argv
    mode = argv[1]
    hash_list = []

    if mode == "-d" or mode == "--directory" and argv[2] is not None:
        kthashDb = KTHashDb(reset=True)
        hash_list = dirWalk(argv[2])
        print(*hash_list, sep="\n")
        print("Hash list length: ", len(hash_list))
        kthashDb.insert(hash_list)
    elif mode == "-c":
        kthashDb = KTHashDb(reset=False)
        query = kthashDb.query_all()
        dirWalk(
            argv[2],
            unique=True,
            database=kthashDb
        )
    elif mode == "-s":
        kthashDb = KTHashDb(reset=False)
        query = kthashDb.query_all()
        print(*query, sep="\n")
        print("Hash list length: ", len(query))

    kthashDb.close()
        
if __name__ == "__main__":
    main()
