import random

#NO TERMINADO
class makeToHanoi():
    items = [random.randint(1, 90) for _ in range(10)]
    def Display(self):
        print("[ ")
        
        for self.item in range(0,11):
            print(self.item,end="")
        
        print(" ]")
        
    def bubbleSort(self):
        swapped = False
        for otheitem in range(self.item, 1):
            print(otheitem) 
            

MK = makeToHanoi() 
MK.Display()