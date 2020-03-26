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


class Shopping:
    def __init__(self, cart={}):
        self.__cart = cart

    def CartValue(self, code=''):
        try:
            total_value = 0
            price_list = {}
            disc_list = {}

            if code != '':
                for key, val in disCountRates.items():
                    if code == key:
                        disc_list = val
                        break
                if not disc_list:
                    print("Invalid discount code")
                    return

            for k, v in self.__cart.items():
                if k in prices:
                    if v > 0:
                        price_list[k] = (v * float(prices[k]))
                        if disc_list and k in disc_list['items']:
                            price_list[k] -= price_list[k] * (disc_list['discount'] / 100)
                        total_value += price_list[k]
                        print("Added " + str(v) + ' ' + str(k) + ' to the cart.')
                    else:
                        print("Item quantity is invalid for", k)
                else:
                    print(k, "item not available!")
            total_value = round(total_value, 2)
            sorted_list = sorted(price_list.items(), key=lambda item: item[1], reverse=True)

            print('\nTotal cart value is ::::', total_value)
            print('Lowest priced item::::', sorted_list[-1])
            print('Highest priced item::::', sorted_list[0])
            print("Your Cart list based on price in descending order :::: ", sorted_list)
            return sorted_list
        except:
            print("Add items to the cart!")


chan = Shopping({'milk': 5, 'bread': 3, "hih": 3, 'onion': 2, 'eggs': 0})
chan.CartValue('corona50')
