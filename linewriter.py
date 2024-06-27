STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
fileName = "result.txt"


def writeTextToFile(argument):
    final_string = STATICKY_TEXT + str(argument)
    file = open(fileName, "w")
    file.write(final_string)
    file.close()
    return fileName
 