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

prices = {'milk': '1.49', 'bread': '0.79', 'onion': '0.59', 'rice': '1.0', 'biscuits': '2.0', 'muffins': '1.7',
          'eggs': '3.2'}

disCountRates = {
    'fresh30': {
        'discount': 30,
        'items': ['milk', 'bread']
    }, 'corona50': {
        'discount': 50,
        'items': ['rice']
    }, 'festive15': {
        'discount': 15,
        'items': ['muffins', 'eggs']
    }
}


class Shopping():
    def __init__(self, cart={}):
        self.__cart = cart

    def CartValue(self, code=''):
        try:
            totalValue = 0
            priceList = {}
            discList = {}

            if code != '':
                for key, val in disCountRates.items():
                    if code == key:
                        discList = val
                        break
                if not discList:
                    print("Invalid discount code")
                    return

            for k, v in self.__cart.items():
                if k in prices:
                    priceList[k] = (v * float(prices[k]))
                    if discList and k in discList['items']:
                        priceList[k] -= priceList[k] * (discList['discount'] / 100)
                    totalValue += priceList[k]
                    print("Added " + str(v) + ' ' + str(k) + ' to the cart.')
                else:
                    print(k, "item not available!")
            totalValue = round(totalValue, 2)
            sortedList = sorted(priceList.items(), key=lambda item: item[1], reverse=True)

            print('\nTotal cart value is ::::', totalValue)
            print('Lowest priced item::::', sortedList[-1])
            print('Highest priced item::::', sortedList[0])
            print("Your Cart list based on price in descending order :::: ", sortedList)
            return sortedList
        except:
            print("Exception occurred: Invalid Input!")


chan = Shopping({'milk': 5, 'bread': 1, "hih": 3, 'onion': 2, 'fjh': 5})
chan.CartValue('corona50')
