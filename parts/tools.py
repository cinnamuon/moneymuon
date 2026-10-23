import datetime
import sys

money_path = "store/money.txt"

def Fround(num: float):
    # "financial round" that ensures a number is rounded to two digits and that those digits show

    new = round(num, 2)
    if new - round(new, 1) == 0:
        return str(new) + "0"

    return str(new)

    pass

def GetMoney():
    # get current week money

    with open(money_path, "r") as money:
        return float(money.readlines()[0])

    pass

def GetDay():
    # get current day, easier than doing all that datetime bs

    day = datetime.datetime.now().weekday()
    if day == 0: return "Monday"
    if day == 1: return "Tuesday"
    if day == 2: return "Wednesday"
    if day == 3: return "Thursday"
    if day == 4: return "Friday"
    if day == 5: return "Saturday"
    if day == 6: return "Sunday"

    pass

def GetRuntimeStatus():
    # returns true if running from startup

    is_startup = "--startup" in sys.argv
    if is_startup: 
        return True

    return False

    pass

def SetWeeklyMoney(base: float, extra: float):
    # set weekly money

    day = datetime.datetime.now().weekday()

    # Add a command line parameter to the startup shortcut (in its Properties box), e.g. --startup
    is_startup = "--startup" in sys.argv

    if is_startup and day == 0:
        with open(money_path, "w") as money:
            money.write(str(base + extra))

    pass

def SetWeeklyMoneyOverride(base: float, extra: float):
    # bypass day and startup requirement to test money functionality

    with open(money_path, "w") as money:
        money.write(str(base + extra))

    pass

def RemoveMoney(deduct: float):
    # remove money

    current = GetMoney()
    with open(money_path, "w") as money:
        money.write(str(current - deduct))

    pass