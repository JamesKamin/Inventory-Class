#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:15:22 2020

@author: jkenglish
"""

from operator import itemgetter

class InventoryItem:
    """ Class with Inventory attributes """
    def __init__(self):
        """ inv_info holds the inventory item in a dictionary """
        self.upcNum = 0
        self.price = 0
        self.cost = 0
        self.quantity = 0
        self.inv_info = {}


    def setUpcNum(self, upcNum):
        self.upcNum = upcNum

    def getUpcNum(self):
        return (self.upcNum)

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return (self.price)

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return (self.cost)

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return (self.quantity)

    def addItem(self):
        """ Adds the inventory item to the dictionary """
        upcNum_val = input("Enter the UPC Number: ")
        price_val  = input("Enter the price: ")
        cost_val = input("Enter the Cost: ")
        quantity_val = input("Enter the quantity: ")

        # validates input to make sure only digits are entered
        if chkAddInput(upcNum_val, price_val, cost_val, quantity_val):

            self.inv_info['upcNum'] = int(upcNum_val)
            self.inv_info['price'] = float(price_val)
            self.inv_info['cost'] = float(cost_val)
            self.inv_info['quantity'] = int(quantity_val)
            print(f"Added Item {self.inv_info} to Inventory.")
            return (self.inv_info)


#These methods are outside the InventoryItem Class       

def delItem(my_list):
    """ deletes an item from the inventory """
    #if len(my_list) == 0:
    if not my_list:
        print("Inventory is Empty. Nothing to Delete.\n")
        return
    upcNum = input("Enter UPC Number to Delete: ")

    # Checks if upc Number is valid
    if isValidUpc(my_list, upcNum):

        for item in range(len(my_list)):
            if my_list[item]['upcNum'] == int(upcNum):
                del my_list[item]
                print(f"Deleted item for UPC Number: {upcNum}")
                break   
        return (my_list)

def modItem(my_list):
    """ Modifies an inventory attribute like price, cost, quantity """
    #if len(my_list) == 0:
    if not my_list:
        print("Inventory is Empty. Nothing to Update.\n")
        return

    upcNum = input("Enter UPC Number to Modify: ")

    # Checks if upc Number is valid   
    if isValidUpc(my_list, upcNum):

        key = input("Enter Key to modify (price, cost, quantity): ")

        key = key.lower()
        if key in ('price', 'cost', 'quantity'):     
            value = input(f"Enter new value for {key}: ")
        else:
            print(f"Only Valid Keys are 'price', 'cost', and 'quantity'. Try Again.")
            return
        # Check the input value for price, cost, quantity to make sure all digits
        if chkModInput(value):
            pass
        else:
            return
    else:
        return

    if key in ('price', 'cost'):
        value = float(value)
    elif key == 'quantity':
        value = int(value)

    for item in range(len(my_list)):
        if my_list[item]['upcNum'] == int(upcNum):
            my_list[item][key] = value
            print(f"Updated {key} with new value: {value} for UPC Number: {upcNum}")
            break

    return (my_list)


def dispItem(my_list):
    """ Display the dictionary items as columns """
    #use itemgetter() from the operator module to sort the UPC Numbers
    # use list comprehension to print the dictionay items as columns

    my_list2 = sorted(my_list, key=itemgetter('upcNum'))
    print(f"\n\n---------------------------------------------------------")
    print (f"|{'UPCNumber':<13}|{'Price':<13}|{'Cost':<13}|{'Quantity':<13}|")
    print(f"---------------------------------------------------------")
    [print(f"|{item['upcNum']:<13}|{item['price']:<13}|{item['cost']:<13}|{item['quantity']:<13}|") for item in my_list2]
    print(f"---------------------------------------------------------")


def isValidUpc(my_list, upcNum):
    """ check if UPC number is valid for Delete and Modify actions """
    if upcNum.isdigit() and len(upcNum) == 12:
        pass
    else:
        print(f"UPC Number must be 12 digits only. Try Again. ")
        return (False)

    for item in range(len(my_list)):
        if my_list[item]['upcNum'] == int(upcNum):
            return (True)
    print(f"\nUPC Number Not Found. Try Again")
    return (False)

def chkAddInput(upcNum, price, cost, quantity):
    """ Check input for Add action is valid """
    if upcNum.isdigit() and len(upcNum) == 12:
        pass
    else:
        print(f"UPC Number must be 12 digits only. Try Again. ")
        return (False)
    if price.isdigit():
        pass
    else:
        print(f"Price must be all digits only. Try Again. ")
        return (False)
    if cost.isdigit():
        pass
    else:
        print(f"Cost must be all digits only. Try Again. ")
        return (False)
    if quantity.isdigit():
        pass
    else:
        print(f"Quantity must be all digits only. Try Again. ")
        return (False)
    return (True)


def chkModInput(value):
    """ Check if input for Modify Action is valid """
    if value.isdigit():
        return (True)
    else:
        print(f"Cost, Price, and Quantity must be all digits only. Try Again. ")
        return (False)



def main():
    # Create a list to hold all the dictionary Inventory items
    # my_list will store all the dict items returned by addItem()

    my_list = []
    print(f"\n\nWelcome to the Inventory Management System")
    while True:
      print(f"\n\n\n\n------------------------------------------\n")
      print(f"Menu\n")
      print(f"------------------------------------------\n")
      print(f"1) Add an item to the inventory")
      print(f"2) Delete an item from the inventory")
      print(f"3) Modify an item from the inventory")
      print(f"4) Display the inventory")
      print(f"5) Exit")
      print(f"------------------------------------------\n")

      resp = input("Enter your choice: ")

      if resp == "1":
          my_inv = InventoryItem()
          result = my_inv.addItem()
          #check to make sure addItem() does not return None
          if result:
              my_list.append(result)
      elif resp == "2":
          delItem(my_list)
      elif resp == "3":
          modItem(my_list)
      elif resp == "4":
          dispItem(my_list)   
      elif resp == "5":
          break
      else:
          print("Valid Choices are 1-5 only. Try Again. \n")

main() 

