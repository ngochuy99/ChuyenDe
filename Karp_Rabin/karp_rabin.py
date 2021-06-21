def Hash(hashArray, hashArrayLength):
    result = 0
    pos = 0
    for i in hashArray:
        result += ord(i) * pow(2, hashArrayLength - pos - 1)
        pos += 1
    return result % 99959


def reHash(firstChar, lastChar, hashValue, hashArrayLength):
    result = 2 * (hashValue - ord(firstChar) * pow(2, hashArrayLength - 1)) + ord(lastChar)
    return result % 99959


def Karp_Rabin(searchPattern, searchString):
    hsp = Hash(searchPattern, len(searchPattern))
    init = searchString[0:len(searchPattern)]
    hss = Hash(init, len(init))
    if hsp == hss:
        print("Trùng tại vị trí 0")
    pos = 1
    while pos < len(searchString) - len(searchPattern):
        hss = reHash(searchString[pos - 1], searchString[pos + len(searchPattern) - 1], hss, len(searchPattern))
        if hsp == hss and searchString[pos:pos + len(searchPattern)] == searchPattern:
            print("Trùng tại vị trí " + str(pos))
            print(searchString[pos:pos + len(searchPattern)])
        pos += 1


import testData

Karp_Rabin(testData.Search_pattern, testData.Search_String)
