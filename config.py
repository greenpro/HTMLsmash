#!/usr/bin/env python3.6
import pathlib
import os

# Assemble the text of the file
def getParams():
    text  = "basePath:"    + input("Where is the base directory? ~/") + "\n"
    text += "contentPath:" + input("Where is the directory for your HTML parts? ~/") + "\n"
    text += "tagFile:"   + input("What is the name of the tag file for assembly? ") + "\n"
    text += "outputName:"  + input("What is the name of your output file? ")
    return text

# Write the config file in the home dir
def writeConfig(text):
    f = open(str(pathlib.Path.home()) + os.sep + ".smashrc", "w+")
    f.write(text)
    f.close()

def main():
    text = getParams()
    writeConfig(text)

if __name__ == "__main__":
    main()
