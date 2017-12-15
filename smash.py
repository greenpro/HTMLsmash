#!/usr/bin/env python3.5

import pathlib
import os

# Add the parts of a file to a dictionary
def toDict(content):
    # Parse the file to a list of lists
    content = content.split("\n")
    content = [item.split(":") for item in content if item != ""]

    # create a dictionary from the list
    return {item[0] : item[1] for item in content}



# Get the contents of the main HTML part
def getFile(contentPath):
    fd = open(str(pathlib.Path.home()) + os.sep + contentPath, "r")
    content = fd.read()
    fd.close()

    return content



# Get the list of tags and replacements for the HTML
def getParts(tagFilePath):
    # Get the tag given tag file contentes
    content = getFile(tagFilePath)

    # Get rid of the extra characters in the file for parsing
    content = content.replace("\t", "")
    content = content.replace(" ", "")
    content = content.replace("\n\n", "\n")

    # Sepparate the different tag parts
    content = content.split("\n}\n{\n")
    content[ 0] = content[ 0].replace("{\n", "")
    content[-1] = content[-1].replace("\n}", "")

    # Parse each part to a dictionary
    return [toDict(part) for part in content]



def main():
    # Setup
    config = toDict(getFile(".smashrc"))
    main = getFile(config["contentPath"] + os.sep + "main.pt")
    parts = getParts(config["basePath"] + os.sep + config["tagFile"])

    # Find and replace
    for tags in parts:
        part     = tags["part"]
        template = tags["template"]
        tag      = "{{" + tags["tag"] + "}}"

        template = getFile(config["basePath"] + os.sep + template)
        content = None if part == "None" else getFile(config["basePath"] + os.sep + part)

        del tags["template"]
        del tags["part"]
        del tags["tag"]

        if content != None:
            template = template.replace("{{content}}", content)

        # Replace all of the content tags with their text value
        for key in tags:
            if "{{" + key + "}}" in template:
                template = template.replace("{{" + key + "}}", tags[key])
            else:
                print("Tag {{" + key + "}} not found in part " + part + " using template " + template)

        if tag in main:
            main = main.replace(tag, template)
        else:
            print("Tag {{" + tag + "}} not found.")

    # Write the final file
    path = str(pathlib.Path.home()) + os.sep + config["basePath"] + os.sep + config["outputName"]
    fd = open(path, "w+")
    fd.write(main)
    fd.close()



if __name__ == "__main__":
    main()
