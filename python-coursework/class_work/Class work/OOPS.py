class shopping:
    
    discount = 10 
    def __init__(self,name):
        self.name = name
        self.orders = []
    
    
    def myorder(self,order):
        self.orders.append(order)
        print(f"{self.name}!\nYour {self.orders} order is succesfully placed")
        
    @classmethod    
    def updateDiscount(cls,newdiscount):
        cls.discount = newdiscount
        print(f"Updated discount: {cls.discount}")
        
    @staticmethod
    def Welcome():
        print("Welcome to E-cart.")
    
        

keerthana  = shopping('keerthana')
nihitha = shopping('nihitha')
leorah = shopping('leorah')

keerthana.myorder('phone')
nihitha.myorder('jeans')
leorah.myorder('handbag')
nihitha.myorder('chain')


shopping.updateDiscount(15)
shopping.Welcome()


'''
keerthana!
Your ['phone'] order is succesfully placed
nihitha!
Your ['jeans'] order is succesfully placed
leorah!
Your ['handbag'] order is succesfully placed
nihitha!
Your ['jeans', 'chain'] order is succesfully placed
Updated discount: 15
Welcome to E-cart.
'''

# CONSTRUCTORS

class shopping:
    def __init__(self,username,phonenumber,password):
        self.username = username
        self.phonenumber = phonenumber
        self.password = password
        self.fav = []
        self.order = []
        self.mycart = []
        print("Welcome to Flipkart {self.username}.Enjoy the shoppping")
        
        
leorah = shopping('leorah',"34544363","leo12#")        

'''
Welcome to Flipkart leorah.Enjoy the shoppping

=== Code Execution Successful ===
'''        
