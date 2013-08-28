### Multipurpose program for manipulating publication lists for NIH Reports

### The input is a list of citations in standard PubMed format
### (Author. Title. Journal & Info. Pub Date. PMID. PMCID.)

### findpmid(), findpmc(), findtitle(), and authorlist()
### create lists of those elements from the citation list
### this is especially useful for PMIDs that can be plugged back into PubMed

### batchcitelist() creates a citation list in NIH Batch Citation format
### which can then be entered back into the PubMed Batch Cite program
### to do PMID lookups.

pmidlist = []
def findpmid():
    cheese1 = raw_input("Name the file for finding the PMID:")
    cheese = open(cheese1, "r")
    for line in cheese:
        if line.find("PMID: ") != -1:
            beginp = line.find("PMID:") + 6
            endp = beginp + 8
            pmidlist.append(line[beginp:endp])
        elif line.find("PMID:") == -1:
            pmidlist.append(line)
        else:
            beginp = line.find("PMID:") + 5
            endp = beginp + 8
            pmidlist.append(line[beginp:endp])
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    pmidlist.sort()
    for each in pmidlist:
        raisin.write(each)
        raisin.write("\n")

def findpmc():
    cheese1 = raw_input("Name the file for finding the PMC:")
    cheese = open(cheese1, "r")
    for line in cheese:
        if line.find("PMCID") != -1:
            beginp = line.find("PMCID") + 7
            endp = beginp + 10
            pmidlist.append(line[beginp:endp])
        elif line.find("PMC") == -1:
            pmidlist.append(line)
        else:
            beginp = line.find("PMC")
            endp = beginp + 9
            pmidlist.append(line[beginp:endp])
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    pmidlist.sort()
    for each in pmidlist:
        raisin.write(each)
        raisin.write("\n")
            
def findtitle():
    cheese1 = raw_input("Name the file for finding the title:")
    cheese = open(cheese1, "r")
    for line in cheese:
            begint = line.find(".") + 2
            endt = line.find(".", begint)
            pmidlist.append(line[begint:endt])
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    pmidlist.sort()
    for each in pmidlist:
        raisin.write(each)
        raisin.write("\n\n")

def journal(thing):
    first = thing.find(".") + 1
    second = thing.find(".", first) + 2
    third = thing.find(".", second)
    return thing[second:third]

def year(thing):
    first = thing.find(".") + 1
    second = thing.find(".", first) + 2
    third = thing.find(".", second) + 2
    fourth = third + 4
    return thing[third:fourth]

def volume(thing):
    first = thing.find(".") + 1
    second = thing.find(".", first) + 2
    third = thing.find(".", second) + 1
    fourth = thing.find(";", third)+1
    fifth = thing.find("(", fourth)
    return thing[fourth:fifth]

def firstpage(thing):
    first = thing.find(".") + 1
    second = thing.find(".", first) + 2
    third = thing.find(".", second)
    fourth = thing.find(":", third)+1
    five = thing.find("-", fourth)
    return thing[fourth:five]

def author(thing):
    if thing.find(",") > thing.find("."):
        first = thing.find(".")
    else:
        first = thing.find(",")
    return thing[:first]

citelist = []

def batchcitelist():
    cheese1 = raw_input("Name the file for converting to batchcite:")
    cheese = open(cheese1, "r")
    for line in cheese:
        citelist.append(line)
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    for each in citelist:
        batchcite = ""
        batchcite = journal(each) + "|" + year(each) + "|" + volume(each) + "|" + firstpage(each) + "|" + author(each) + "|" +"|"
        raisin.write(batchcite)
        raisin.write("\n\n")
        
def authorlist():
    cheese1 = raw_input("Name the file for finding the authorlists:")
    cheese = open(cheese1, "r")
    for line in cheese:
            begint = 0
            endt = line.find(".")
            pmidlist.append(line[begint:endt])
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    pmidlist.sort()
    for each in pmidlist:
        raisin.write(each)
        raisin.write("\n\n")

