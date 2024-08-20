import os
from datetime import datetime

try:
    print("Start")
    click("1691086555518.png")
except:
    App.open("C:\\TSC\\Data\\rpa_autocomments\\SSmail.exe")
    exc_type, exc_val, exc_tb = sys.exc_info()
    ErrorText = "***** ERROR IN SCRIPTNAME = " + sys.argv[0] + " *****\n"
    ErrorText += "Date/Time : " + str(datetime.now()) + "\n"
    ErrorText += "Line Number: " + str(exc_tb.tb_lineno) + "\n"
    ErrorText += "Error Type : " + exc_type.__name__ + "\n"
    ErrorText += "Error Value: " + exc_val.message + "\n"
    ErrorText += "***************************************************************\n\r"
    print ErrorText