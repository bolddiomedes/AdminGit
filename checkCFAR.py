###Program to find the number of CFAR members in a list of names. Returns X members out of Y names.


reflist = []
testlist = []

def reflistit():
    cheese = open("cfarref.txt", "r")
    for line in cheese:
        line = line.strip()
        reflist.append(line.upper())

def isCFAR(name):
    for each in reflist:
        if name == each:
            return 1
        else:
            return 0


def testlistit():
    cheese2 = raw_input("Name the file for checking names of CFAR: ")
    cheese3 = open(cheese2, "r")
    for line in cheese3:
        line = line.strip()
        testlist.append(line[:line.find(",")+3].upper())


def checkCFAR():
    reflistit()
    testlistit()
    count = 0
    for every in testlist:
        for each in reflist:
            if each == every:
                count += 1
    countstr = str(count)
    lenstr = str(len(testlist))
    print countstr + " CFAR Members out of " + lenstr


def checkCFAR2():
    reflistit2()
    testlistit2()
    count = 0
    for every in testlist:
        for each in reflist:
            if each == every:
                count += 1
    countstr = str(count)
    lenstr = str(len(testlist))
    print countstr + " CFAR Members out of " + lenstr

def testlistit2():
    cheese2 = raw_input("Name the file for checking names of CFAR: ")
    cheese3 = open(cheese2, "r")
    for line in cheese3:
        line = line.strip()
        testlist.append(line.upper())

def reflistit2():
    cheese = open("cfarref.txt", "r")
    for line in cheese:
        line = line.strip()
        line = line[:line.find(",")]
        reflist.append(line.upper())
