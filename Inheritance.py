# Inheritance in Python


# Base Class 
class Mobile:
    model_name=None
    mfg_year=None
    camera_pixel=None

    def __init__(self,model_name,mfg_year,camera_pixel):
        self.model_name=model_name
        self.mfg_year=mfg_year
        self.camera_pixel=camera_pixel

    def display_detail(self):
        print("This is your phone details\n")

    def display(self):
        
        print("Model_name: "+self.model_name)
        print(f"Manufacturing Year: {self.mfg_year}")
        print(f"Pixel in this model: {self.camera_pixel}")



# Child Class

class Laptop(Mobile):
    
    
    ram_size=None

    def __init__(self,model_name,mfg_year,camera_pixel,ram_size):
        
        # Using super() to inherit all the declared variables from the Base class to the Child class
        #super().__init__(model_name,mfg_year,camera_pixel)
        Mobile.__init__(self,model_name,mfg_year,camera_pixel)

        self.ram_size=ram_size

    def display_detail(self):
        print("This is your laptop details\n")

    def display(self):
        self.display_detail()
        
        # Calling the display from the Mobile class
        # super().display()
        Mobile.display(self)

        print(f"The RAM in this model is {self.ram_size}"+"GB")



laptop_1 = Laptop("Acer Swift 5",2019,24,16)



laptop_1.display()
