def formatPrice(price):
    #price = str(price)
    print(type(price))
    price = price[:-1]
    #price = price.replace('€','')
    price = price.replace('.','')
    price = price.replace(',','.')
    print("-",price)
    price = float(price)
    print("+",price)
    return price

def tracker(current,threshold):
    flag = False
    while True:
        if current <= threshold:
            print("Price is dropped")
            flag = True
            break;

        time.sleep(2)
        print("TRACKER IS TRACKING")
        #get data from db
        #Get link
        #already tracked yes or no
        #If yes amazonn hit link
        #if latest price < threshold value : print message Price dropped
        #set flag to already tracked to yes
    return flag

def isValidLink(link):
    if (link[:22] == "https://www.amazon.de/"):
        print("Valid amazon url")
        return True
    else:
        return False