#######################################
# FRCScouter2018 Main Script          #
# (C)2018 - Benjamin Sykes, Team 5980 #
#######################################



# <<< WELCOME >>>

print("MSG~: FRCScouter2018 (ScoutShell)")
print("MSG~: (C)2018 - Ben Sykes")



# <<< SET VARIABLES >>>

print("")
print("INFO: Setting variables . . . ", end='')
currentfile = ""
fileopen = False
print("Done.")



# <<< IMPORT LIBRARIES AND MODULES >>>

print("INFO: Please wait, importing libraries: ")
print("+CONT - Cmd . . . ", end='')
import cmd

print("Done.")
print("+CONT - Prettytable . . . ", end='')
import prettytable

print("Done.")
print("+CONT - Math . . . ", end='')
import math

print("Done.")
print("+CONT - PathLib . . . ", end='')
import pathlib

print("Done.")
print("+CONT - OS . . . ", end='')
import os

print("Done.")



# <<< LOAD SCOUTSHELL CLASS >>>

print("")
print("INFO: Loading ScoutShell . . . ")



class ScoutShell(cmd.Cmd):

    # --- Parameters ---

    intro = "Welcome to ScoutShell.\n"
    prompt = "FRC#> "
    file = None

    # --- Invalid error ---

    def default(self, line):
        print("ERR!: Invalid command, " + line)

    # --- File management commands ---

    def do_fileopen(self, arg):
        if arg == "":
            print("WARN: No file specified")
        elif fileopen:
            print("WARN: Cannot open a file if there is already one open.")
        else:
            testfile = arg
            if os.path.exists(testfile) and not (os.path.isdir(testfile)):
                print("INFO: Checking if the file is valid . . . ", end='')
                loadedtestfile = os.open(testfile, 'r')
                try:
                    if os.read(loadedtestfile, 1) == "!FRCSCOUTER2018FORMAT":
                        print("OK.")
                        currentfile = testfile
                        fileopen = True
                    else:
                        print("Invalid format.")
                except:
                    print("An error occurred.")
                os.close(testfile)
    def help_fileopen(self):
        print("Opens a FRCScouter2018 formatted data file.")
        print("SYNTAX: fileopen \"[path]\"")

    def do_fileclose(self, arg):
        if arg != "":
            print("WARN: Too many arguments.")
        elif not(fileopen):
            print("WARN: Cannot close a file if there is not one open.")
        else:
            currentfile = ""
            fileopen = False
    def help_fileclose(self):
        print("Closes a FRCScouter2018 formatted data file.")
        print("SYNTAX: fileclose")

