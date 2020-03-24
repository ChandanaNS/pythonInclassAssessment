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

prices = fileDictionary("itemFile")


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
chan = Shopping({'milk': 2})
chan.addItem('bread', 4)
chan.addItem('bread', 2)
