# first program 
print('hello world')
#classes
# instance methods
class Laptop:
    storage_type = "ssd" #class attribute
    def __init__(self,RAM, storage):#instance attribute
        self.RAM = RAM
        self.storage=storage

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage}{self.storage_type}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb","256gb")

l1.get_info()

