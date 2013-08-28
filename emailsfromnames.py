### Utilizing a reference csv of names matched with emails,
### opens a csv of names and adds the matching emails
### any names not found on reference list will request an email value
### to add to the reference list

import csv
startlist = []
emaillist =[]
refDict = dict()
namesReference = ""


###create reference list###
def createRef():
    global namesReference
    namesReference = raw_input("Please enter the path for the csv email reference list: ")
    with open(namesReference, 'rb') as csvfile:
        namesrefreader = csv.reader(csvfile)
        for row in namesrefreader:
            temp = row[0].upper()
            valtemp = [row[1], row[2]]
            refDict.update({temp: valtemp})


###create list of improper names###
def createStart():
    namesInput = raw_input("Please enter the path for the csv list of names to find emails for: ")
    with open(namesInput, 'rb') as csvfile:
        namesreader = csv.reader(csvfile)
        for row in namesreader:
            startlist.append(row[0])

    
##look up the key in the reference dictionary###
def getval(thing):
    if thing not in refDict:
        addtoRef1(thing)
    return refDict[thing]


##writes output file###
def createEnd():
    namesOutput = raw_input("Please enter the path for the csv list of names to be output: ")
    with open(namesOutput, 'wb') as csvfile:
        nameswriter = csv.writer(csvfile)
        for each in range(len(startlist)):
            emailadd = []
            emailadd.append(startlist[each])
            emailadd.extend(emaillist[each])
            nameswriter.writerow(emailadd)

def addtoRef1(newkey):
    newval1 = raw_input(newkey + " is not in the csv reference list. Please enter its value: ")
    newval2 = []
    newval2.extend(newval1.split(", "))
    refDict.update({newkey: newval2})

def addtoRef2():
    global namesReference
    with open(namesReference, 'wb') as csvfile:
        namesrefwriter = csv.writer(csvfile)
        for each in refDict:
            refadd = []
            refadd.append(each.title())
            refadd.extend(refDict[each])
            namesrefwriter.writerow(refadd)

                                 
def goodstart():
    createRef()
    createStart()
    startkeyed = ""
    for each in range(0, len(startlist)):
        startkeyed = startlist[each].upper()
        emaillist.extend([getval(startkeyed)])
    createEnd()
    addtoRef2()
