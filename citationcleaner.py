### Cleans up citation list from PubMed standard output
### Into the format we utilize for Penn CFAR Publication Lists

citelist =[]
def cleanit():
    cheese1 = raw_input("Name the file for cleaning:")
    cheese = open(cheese1, "r")
    for line in cheese:
        citelist.append(line)
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    for each in citelist:
        if each.find("doi:") == -1:
            citation = each
        else:
            tempeach = riddoi(each)
            tempeach = pmc(tempeach)
            tempeach = pmid(tempeach)
            citation = tempeach
        raisin.write(citation)
        raisin.write("\n\n")

def riddoi(thing):
    st = thing.find("doi:") - 1
    if thing.find("Epub") != -1:
        ed = thing.find("Epub") - 1
    else:
        ed = thing.find("PubMed") - 1
    newthing = thing[:st] + thing[ed:len(thing)]
    return newthing

def pmc(thing):
    st = thing.find("PubMed Central")
    if st == -1:
        return thing
    else:
        return thing[:st] + thing[st + 14:]
    
def pmid(thing):
    st = thing.find("PubMed")
    if st == -1:
        return thing
    else:
        return thing[:st] + thing[st + 7:]
    

    
