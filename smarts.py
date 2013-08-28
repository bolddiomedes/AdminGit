### To translate a SMARTS Funding Email (as txt)
### Into html tagged tabular format for the
### Penn CFAR Webpage (http://www.med.upenn.edu/cfar/funding_hotrfas.shtml)

smartlist =[]

def makeitsmart():
    cheese1 = raw_input("Name the file for converting the smart list:")
    cheese = open(cheese1, "r")
    for line in cheese:
        if line.find("Sponsor") != -1:
            sponsor = line[9:].strip()
        elif line.find("Title") != -1:
            title = line[7:].strip()
        elif line.find("E-mail") != -1:
            email = line[8:].strip()
        elif line.find("Program URL") != -1:
            purl = line[13:].strip()
        elif line.find("Deadline") != -1:
            str1 = '<tr valign=\"top\">' + '\n' + '<td height=\"54\" valign=\"top\">' + sponsor + \
                   '</td>' +'\n' + '<td valign="top"><a href="' + purl + '" target="_blank">' + title + '</a></td>' + \
                   '\n'+'<td valign="top"><a href="mailto:' + email + '">' + email + '</a></td>' + '\n'+'</tr>'
            smartlist.append(str1)
    writeit()

def writeit():
    raisin1 = raw_input("Name the file for output sake:")
    raisin = open(raisin1, "w")
    for each in smartlist:
        raisin.write(each)
        raisin.write("\n\n")
