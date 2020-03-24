'''
description: Inclass assessment
Date: 24-03-20
Authour: Chandana
@gitHub url: https://github.com/ChandanaNS/pythonInclassAssessment
'''
'''

Please code a solution to the following problem, tracking your progress by commiting to GitHub, and submitting your progress after half an hour and after an hour to Moodle, as well as the final submission. 

A shopping basket contains a number of line items, for example: eggs, rice, flour; each with a specific quantity. A basket may also have one discount code, for example eggs20. 

The shop has a standard price list, as well as a set of currently valid discount codes, each of which confers a certain percentage discount for a list of eligible products.

Produce a method which accepts a list of baskets, and outputs their values from highest to lowest.

'''
import operator
# Fetch price list from file
def fileDictionary(fileName):
    resultDict = {}
    try:
        fileOpen = open(fileName, 'r')
        for lines in fileOpen.readlines():
            line = lines.strip().split(" ")
            resultDict[line[0]] = line[1]
        print(resultDict)
        return resultDict

    except IOError:
        print("Exception occurred: File Name not found!")

prices = fileDictionary("itemFile") #please refer github repository for the file

disCountRates={'fresh30':['milk','bread'],'corona50':['rice']}

class Shopping():
    def __init__(self, cart={}):
        self.__cart = cart

    def getCart(self,item):
        if item not in self.__cart:
            return 0
        return self.__cart[item]

    def addItem(self, item, q):
        if q <= 0:
            raise ValueError("enter a valid quantity")
        self.__cart[item] = q + self.getCart(item)

    def delItem(self,item,q):
        if q <= 0:
            raise ValueError("Negative quantity not allowed")
        elif q > self.getCart(item):
            raise ValueError("insufficient quantity")
        self.__cart[item] = self.getCart(item) - q
        if self.__cart[item] == 0:
            del self.__cart[item]

    def CartValue(self,code=''):
            totalValue = 0
            priceList = {}
            discList =[]
            discCode = code
            for key, val in disCountRates.items():
                if discCode == key:
                    discList = val

            for k, v in self.__cart.items():
                priceList[k] = (v * float(prices[k]))
                if k in discList:
                    if discCode == 'fresh30':
                        print("Fresh30 Discount applied for ",k)
                        priceList[k] -= priceList[k] * 0.3
                    elif discCode == 'corona50':
                        print("corona50 Discount applied for ",k)
                        priceList[k] -= priceList[k] * 0.5
                    else:
                        priceList[k] = priceList[k]
                    print('Amount after discount::::', priceList[k])
                totalValue += v * float(priceList[k])
            sortedList = sorted(priceList.items(), key=operator.itemgetter(1), reverse =True)
            print('Total cart value is ::::', totalValue)
            print('Discounted price list of your items ::::', priceList)
            print('Highest priced paid ::::', sortedList[-1])
            print('Lowest priced Paid ::::', sortedList[0])
            print("Your Cart list based on price ::::", sortedList)
            return totalValue

chan = Shopping({'milk': 5})

chan.addItem('bread', 1)

chan.addItem('onion', 2)

chan.CartValue('fresh30')
