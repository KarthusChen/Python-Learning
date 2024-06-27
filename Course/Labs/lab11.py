def writingFunction(Filename):
    outfile=open(Filename,"w")
    name="Yuzhong Chen\n"
    major="Computer Engineering\n"
    hobby="Video Games\n"
    print(name,major,hobby,file=outfile)
    outfile.close()

def readingFunction(Filename):
    with open(Filename, "r") as infile:
        content = infile.read()
    return content

writingFunction("YuzhongChen.txt")
content = readingFunction("YuzhongChen.txt")
print(content)
