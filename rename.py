# Python 3 code to shunt multiple 
# files in a directory or folder
# 1-example.txt --> 1-example.txt
# 1a-example.jpeg --> 1b-example.jpeg
# for all matching

import os
import sys
import re

def main():
    #Check argument count
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Usage: python", sys.argv[0], "<pushStart> <directory = .>")
        sys.exit(1)

    #A string for the type of position being updated e.g 1 or 1b
    position = sys.argv[1]
    folder = "."

    #Change path if provided
    if(sys.argv == 3):
        folder = sys.argv[2]

    
    pureNum = False

    #Check that provided pattern matches what is needed
    pattern = re.compile("^[0-9]+[a-z]?$")
    result = pattern.match(position)
    if result:

        #To store the files that need changing, keys will be sorted later to rename in reverse order
        #This will prevent accidental overwriting of files
        oldNameNewName = dict()

        try:
            #If position can be cast, then it is purely a number, without a letter
            int(position)
            pattern = re.compile("^[0-9]+")
            pureNum = True
        except:
            pattern = re.compile("^[0-9]+[a-z]")

        for filename in os.listdir(folder):

            result = pattern.match(filename)

            #If the current file matches the format for renaming
            if result:
                end = result.end()

                toChange = filename[:end]

                if(pureNum):
                    pos = int(toChange)
                    if pos >= int(position):
                        #This is a file that needs to be changed - increment the number
                        oldName = filename

                        newStart = str(pos + 1)
                        newName = newStart + oldName[end:]

                        oldNameNewName[oldName] = newName

                else:
                    intPos = int(toChange[:-1])
                    charPos = toChange[-1]
                    if intPos == int(position[:-1]) and charPos >= position[-1]:
                        #This is a file that needs to be changed - increment the letter
                        oldName = filename

                        newStart = toChange[:-1] + chr(ord(charPos) + 1)
                        newName = newStart + oldName[end:]

                        oldNameNewName[oldName] = newName
            
        #Sort keys to avoid overwriting - later files renamed first
        keys = list(oldNameNewName.keys())
        keys.sort(reverse=True)

        for k in keys:
            src = k
            dst = oldNameNewName[k]
            os.rename(src, dst)
        
            
                # rename() function will rename the file
                #os.rename(src, dst)

    else:
        print("Invalid input format")

# Driver Code
if __name__ == '__main__':
    
    # Calling main() function
    main()