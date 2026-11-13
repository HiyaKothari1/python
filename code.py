# first program 
print('hello world')
#classes
# instance methods- can access both class and instance attributes 
class Laptop:
    storage_type = "ssd" #class attribute
    def __init__(self,RAM, storage):#instance attribute
        self.RAM = RAM
        self.storage=storage
    #class methods - yeh sirf class attributes ko access kr sakte hai not instance attributes
    @classmethod # this method changes the behaviour and it is making the method below a class method
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage}{self.storage_type}")

    #static methods - do not belong to class , or instance they are stand along functions inside a class( logic is tied up with class/object)
    # it is not using class/instance parameters but because the logic is related to the class we use static methods
    @staticmethod
    def calc_discount(price,discount):
        final_price= price-(discount *price/100)
        print(f"final price={final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb","256gb")

l1.get_storage_type()
l2.calc_discount(40000,10)
 #problem 
class Store:
    count = 0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Store.count+=1

    def get_info(self):
        print(f"price of {self.name} is{self.price}") 

    @classmethod
    def get_count(cls):
        print(f"total objects created {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        discount=price*discount/100
        print(f"discount on this product is {discount}")

#encapsulation

class BankAccount:
    def __init__(self,name,balance):
        self.name = name #public
        self.__balance = balance #private - data mangling

    def get_balance(self): #getter
        return self.__balance

    def set_balance(self,newBalance):#setter
        self.__balance = newBalance

acc1 = BankAccount("Rahul Kumar", 10000)

acc1.set_balance(20000)
print(acc1.name, acc1._BankAccount__balance)

