import time
import datetime
print("hellow world")

class  Customlib:
    ROBOT_LIBRARY_SCOPE= "TESTCASE"

def time_date():
    print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
    return datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

