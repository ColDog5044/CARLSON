import os
import subprocess as sb

paths = {

    "example" : "c:\\Windows\\System32\\app.exe",
}

def startFileExplorer():
    os.system("start explorer")

def startRegedit():
    os.system("start regedit")

def startNotepad():
    os.system("start notepad")

def startCalculator():
    os.system("start calc")

def startControlPanel():
    os.system("start control")

def startCMD():
    os.system("start cmd")

def startPowerShell():
    os.system("start powershell")

def startDiskDefragment():
    os.system("start dfgui")

def startDiskManagement():
    os.system("start diskmgmt")

def startEventViewer():
    os.system("start eventvwr")

def startGroupPolicy():
    os.system("start gpedit")

def startSystemInfo():
    os.system("start msinfo32")

def startRemoteDesktop():
    os.system("start mstsc")

def startPerformanceMonitor():
    os.system("start perfmon")

def startResourceMonitor():
    os.system("start resmon")

def startStepsRecorder():
    os.system("start psr")

def startSystemRestore():
    os.system("start rstui")

def startSecurityPolicy():
    os.system("start secpol")

def startServicesViewer():
    os.system("start services.msc")

def startSystemProperties():
    os.system("start SystemPropertiesComputerName")

def startTaskManager():
    os.system("start taskmgr")

def startHyperV():
    os.system("start virtmgmt")

def startWindowsFirewall():
    os.system("start wf")

def startWindowsSandbox():
    os.system("start WindowsSandbox")
