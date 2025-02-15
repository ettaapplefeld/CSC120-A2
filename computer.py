class Computer:

    # What attributes will it need? 
    # all attributes copied from main.py
    description: str 
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    #i will set up my constructor initializing all of the attributes
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    # What methods will you need?
    #methods that are specific to the computer and not the resale shop, updating the OS, updating the price, and refurbishing the computer(which also changes the price)
    def UpdateOS(self, newOS:str):
        self.operating_system = newOS
        print ("Operating system updated to", newOS)

    def UpdatePrice(self, NewPrice:int):
        self.price = NewPrice
        print ("The price of this computer is", NewPrice)

    def refurbish(self):
        if self.year_made < 2015:
            self.price = 500
        else:
            self.price = 1000
        print ("Computer has been refurbished. The price of this computer is now $", self.price)

def main():
    myComputer : Computer = Computer("MacBook Air", "3.5 GHc 6Core Intel", 1024, 64,"macOS Big Sir", 2015, 1500)
    print(myComputer) 
    print("This computer is a", myComputer.description, ". It's price is $", myComputer.price)
    myComputer.refurbish()

if __name__ == "__main__":
    main()