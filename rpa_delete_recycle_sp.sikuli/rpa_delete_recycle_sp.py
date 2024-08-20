import os
from datetime import datetime

recycle = "https://tscsacperu.sharepoint.com/sites/TI_BK/_layouts/15/RecycleBin.aspx?view=5"

print("CERRAR PROCESOS")
os.system('taskkill /f /im firefox.exe')
sleep(2)

try:
    print("ABRIR FIREFOX")
    App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    sleep(15)
    type("l",KEY_CTRL)
    sleep(2)
    paste(recycle)
    sleep(2)
    type(Key.ENTER)
    sleep(30)
    click(Pattern("1707430623634.png").targetOffset(-83,1))
    sleep(5)
    click(Pattern("1707431014395.png").targetOffset(-49,-1))
    sleep(10)
    click(Pattern("1707431112529.png").targetOffset(103,3))
    sleep(10)
    click(Pattern("1707430623634.png").targetOffset(-84,1))
    sleep(5)
    click(Pattern("1707431170515.png").targetOffset(-50,-4))
    sleep(15)
    type("w",KEY_CTRL)
    print("FIN")
    
except:
    type("w",KEY_CTRL)
    exc_type, exc_val, exc_tb = sys.exc_info()
    ErrorText = "***** ERROR IN SCRIPTNAME = " + sys.argv[0] + " *****\n"
    ErrorText += "Date/Time : " + str(datetime.now()) + "\n"
    ErrorText += "Line Number: " + str(exc_tb.tb_lineno) + "\n"
    ErrorText += "Error Type : " + exc_type.__name__ + "\n"
    ErrorText += "Error Value: " + exc_val.message + "\n"
    ErrorText += "***************************************************************\n\r"
    print ErrorText