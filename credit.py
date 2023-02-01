def initialize():
    global owed, INTEREST, country_holder, d, m, disabled
    owed = [0,0]
    INTEREST = 1.05
    country_holder = []
    d = 0
    m = 0
    disabled = False

def date_same_or_later(day1, month1, day2, month2):
    if (day1>=day2 and month1 == month2) or (month1>month2):
        return True
    return False


def all_three_different(c1, c2, c3):
    if c1 == c2 or c2 == c3 or c1 == c3:
        return False
    return True

def month_Change(month):
    global owed, m, INTEREST
    for i in range(month-m):
        owed[1]*=INTEREST
        owed[1]+=owed[0]
        owed[0] = 0
        
def purchase(amount, day, month, country):
    global d, m, owed, country_holder, disabled
    if disabled == True:
        return "error"
    if len(country_holder)<3:
        country_holder.append(country)
    else:
        country_holder.append(country)
        del country_holder[0]
    if len(country_holder) == 3:
        if all_three_different(country_holder[0], country_holder[1],country_holder[2]):
            disabled = True
            return "error"
    if date_same_or_later(day, month, d, m) == False:
        return "error"
    month_Change(month)
    owed[0] += amount
    d = day
    m = month

def amount_owed(day, month):
    global d, m, owed 
    if date_same_or_later(day, month, d, m) == False:
        return "error"
    month_Change(month)
    d = day
    m = month
    return owed[0] + owed[1]

def pay_bill(amount, day, month):
    global d, m, owed
    if date_same_or_later(day, month, d, m) == False:
        return "error"
    month_Change(month)
    owed[1]-= amount
    if owed[1]<0:
        owed[0]+=owed[1]
        owed[1] = 0
    d = day
    m = month

if __name__ == "__main__":
    print("Create tests that utilize functions to test code.")
