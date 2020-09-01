
f = open("demo.txt","w")
mugsNames = []
mugsLinks = []
#load mugs defs and mug names into memory
with open("mugs.txt") as mugs:
    line = mugs.readline()
    while line:
        mug = line.split(",")
        mugsNames.append(mug[0])
        mugsLinks.append(mug[1].rstrip("\n"))
        line = mugs.readline()
info = dict(zip(mugsNames,mugsLinks))
#go through update text and do replaces
with open("update.txt") as update:
    line2 = update.readline()
    #until EOF
    while line2:
        #setting newContent here. If line starts with [ than we'll change this later, otherwise we write it to the output file
        newContent = line2
        if line2[0] == "[":
            #assuming ": " character combination only comes up on bits to be replaced.
            content = line2.split(": ")
            #reducing [Char] to just the character name to do matches
            char = content[0][1:-1]
            #replaces name with url and readds ": " back
            if char in info:
                char = "[img]" + info[char] + "[/img]" 
                content[0] = char
                newContent = char + ": " + content[1]
        f.write(newContent)
        line2 = update.readline()
f.close()