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
# # Fetch price list from file
# def fileDictionary(fileName):
#     resultDict = {}
#     try:
#         fileOpen = open(fileName, 'r')
#         for lines in fileOpen.readlines():
#             line = lines.strip().split(" ")
#             resultDict[line[0]] = line[1]
#         print(resultDict)
#         return resultDict
#
#     except IOError:
#         print("Exception occurred: File Name not found!")
#
# prices = fileDictionary("itemFile") #please refer github repository for the file
#
# disCountRates={'fresh30':['milk','bread'],'corona50':['rice']}

prices = {'milk': '1.49', 'bread': '0.79', 'onion': '0.59', 'rice': '1.0', 'biscuits': '2.0', 'muffins': '1.7'}

disCountRates = {
    'fresh30': {
        'discount': 30,
        'items': ['milk', 'bread']
    }, 'corona50': {
        'discount': 50,
        'items': ['rice']
    }
}

class Shopping():
    def __init__(self, cart={}):
        self.__cart = cart

    # def getCart(self,item):
    #     if item not in self.__cart:
    #         return 0
    #     return self.__cart[item]
    #
    # def addItem(self, item, q):
    #     if q <= 0:
    #         raise ValueError("enter a valid quantity")
    #     self.__cart[item] = q + self.getCart(item)
    #
    # def delItem(self,item,q):
    #     if q <= 0:
    #         raise ValueError("Negative quantity not allowed")
    #     elif q > self.getCart(item):
    #         raise ValueError("insufficient quantity")
    #     self.__cart[item] = self.getCart(item) - q
    #     if self.__cart[item] == 0:
    #         del self.__cart[item]

    def CartValue(self, code=''):
            totalValue = 0
            priceList = {}
            discList ={}

            if code != '':
                for key, val in disCountRates.items():
                    if code == key:
                        discList = val
                        break
                if not discList:
                    print("Invalid discount code")
                    return

            # discCode = code
            # for key, val in disCountRates.items():
            #     if discCode == key:
            #         discList = val
            #
            # for k, v in self.__cart.items():
            #     priceList[k] = (v * float(prices[k]))
            #     if k in discList:
            #         if discCode == 'fresh30':
            #             print("Fresh30 Discount applied for ",k)
            #             priceList[k] -= priceList[k] * 0.3
            #         elif discCode == 'corona50':
            #             print("corona50 Discount applied for ",k)
            #             priceList[k] -= priceList[k] * 0.5
            #         else:
            #             priceList[k] = priceList[k]
            #         print('Amount after discount::::', priceList[k])
            #     totalValue += v * float(priceList[k])
            # sortedList = sorted(priceList.items(), key=operator.itemgetter(1), reverse =True)
            # print('Total cart value is ::::', totalValue)
            # print('Discounted price list of your items ::::', priceList)
            # print('Lowest priced paid ::::', sortedList[-1])
            # print('Hishest priced Paid ::::', sortedList[0])
            # print("Your Cart list based on price ::::", sortedList)
            # return totalValue

chan = Shopping({'milk': 5, 'bread': 1, 'onion': 2})
chan.CartValue('fresh30')
