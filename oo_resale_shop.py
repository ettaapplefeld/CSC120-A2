from typing import List
from computer import Computer

class ResaleShop: 

    # What attributes will it need?
    inventory = []
    

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory: List[Computer] = [] #creates empty list for computers
        

    # What methods will you need?
    #this method adds a computer to the inventory of the store
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print ("Computer added to inventory. Item ID", len(self.inventory) - 1) 

    #this method removes an item from the inventory of the store using the computer ID
    def sell(self, computerID: int):
        if 0 <= computerID < len(self.inventory):
            removed_computer = self.inventory.pop(computerID)
            print("Computer", removed_computer.description, ". Computer ID:", computerID, "has been sold.")
        else: 
            print("This computer is not available.")

    #this method prints the list containing all computers
    def print_inventory(self):
        print(self.inventory)



    