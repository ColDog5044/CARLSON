import os
import subprocess as sb

paths = {

    "notepad" : "c:\\Windows\\System32\\notepad.exe",
    "calculator" : "c:\\Windows\\System32\\calc.exe",
}

def startNotepad():
    os.startfile(paths["notepad"])

def startCalc():
    os.startfile(paths["calculator"])

def startCMD():
    os.system("start cmd")

def startPWSH():
    os.startfile()