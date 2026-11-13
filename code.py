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

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb","256gb")

l1.get_storage_type()


