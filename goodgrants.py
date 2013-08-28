### Program to standardize NIH Grant numbers
### For use in reports
### Removes Application Type, Support Year, Extension, & Supplement Digits
### Leaves Activity Code, Center Code, and Serial Number
### As per NIH Policy for acknowledging federal funding

def goodgrant():
    outlist = []
    cheese1 = raw_input("Name the file for finding the good grants:")
    cheese = open(cheese1, "r")
    for line in cheese:
        guff = line
        if line[:1].isdigit() == True:
            guff = line[1:]
        guff = guff.lstrip()
        while guff.count("-") > 0:
            mark = guff.find("-")
            guff = guff[:mark]+guff[mark+1:]
        while guff.count(" ") > 0:
            mark = guff.find(" ")
            guff = guff[:mark]+guff[mark+1:]
        guff = guff[:11]
        ##if guff.find("-") == 0:
            ##guff = guff[1:]
       ## if guff.find("-") != -1:
           ## guff = guff[:guff.find("-")]    
        ##if guff.find(" ") != -1:
           ## guff = guff[:guff.find(" ")] + guff[guff.find(" ")+1:]
        ##if guff.find(" ") != -1:
          ##  guff = guff[:guff.find(" ")] + guff[guff.find(" ")+1:]
        outlist.append(guff)
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    for each in outlist:
        raisin.write(each)
        raisin.write("\n")
            
