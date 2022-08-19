#ForeignCurrency written by Amadou

import locale

rEUR = GBP = rJPY = rCAD = rRUB = 0.0

def getRates():
    global rEUR,rGBP,rJPY, rCAD, rRUB
    print("Please enter the currency rate per US $\n")
    rEUR = getOneRate("EUR")
    rGBP = getOneRate("GBP")
    rJPY = getOneRate("JPY")
    rCAD = getOneRate("CAD")
    rRUB = getOneRate("RUB")

def getOneRate(prompt):
    a = -1
    while a <= 0:
        try:
            a = float(input(prompt + ": "))
            if (a <=0):
                print("Positive values only.")
        except ValueError:
            print("Illegal entry: Positive numerics only please.")
    return a

def getChoice():
    c= -1
    while c < 0 or c > 5 and c != 9:
        try:
            c = int(input("Currency? (1=EUR, 2=GBP, 3=JPY, 4=CAD, 5=RUB, 9= New Rates, 0=Quit): "))
            if (c < 0 or c > 5 and c != 9):
                print(" Currency within 1-3 or 9 only please. 0 quit ")

        except ValueError:
            print("Illegl input: integers 0-5 or 9 only.")
    return c
                         
                         

def doValuation():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    qty = 0
    cval = 0.0
    grandtotal =0.0
    totcunits = [ 0, 0, 0, 0, 0]
    totcval = [ 0.0, 0.0, 0.0, 0.0, 0.0 ]
    totcnames = [ "EUR", "GBP", "JPY", "CAD", "RUB" ]
    totcnmfull = [ "Euros", "Pounds Sterling", "Yen", "Canadian Dollars", "Rubbles"]
    crates = [ rEUR, rGBP, rJPY, rCAD, rRUB ]

    choice = getChoice()
    while choice != 0:
        if choice <= 5:
            qty = getQty(totcnmfull [choice-1])
            cval = qty * crates[choice-1]
            print(str(qty) + " " + totcnmfull[choice-1] + " has of value of %s "
                  %locale.currency(cval,grouping=True))
            totcunits[choice-1] = totcval[choice-1] + qty
            totcval[choice-1] = totcval[choice-1] + cval
                    
            
        elif choice == 9:
            getRates()
            crates = [ rEUR, rGBP, rJPY, rCAD, rRUB ]
            
        else:
            print("Unknown currency or operation")

        print()
        choice = getChoice()
    print("Purchase Summary: ")
    grandtot = 0.0
    for i in range(0,5):
        print(totcnames[i]+ ": " + str(totcunits[i]) + " units for a value of: %s "
                                %locale.currency(totcval[i],grouping=True))
        grandtot = grandtot + totcval[i]
    print("The total value of the proposed currency purchase was %s " %locale.currency(grandtot,grouping=True))


def getQty(prompt):
    q = -1
    while q < 0:
        try:
            q = int(input("How many " + prompt + " are you buying? "))
            if ( q < 0):
                    print("Quantity must be a positive number please")
        except ValueError:
            print("illegal Input. Positive numbers Only please")
            q = -1
    return q
        
        
          
def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')

    print("Welcome to the Foreign Currency Calculator.")
    

    getRates()
    doValuation()

    print("Thanks for Using Amadou's Foreign Currency Calculator")


    
    









if __name__== "__main__":
    main()

