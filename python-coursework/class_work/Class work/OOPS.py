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

class Profile:
    
    def __init__(self,username,password):
        self._followers = {} #protected
        self._following = {} #protected
        self.post = []
        self.username = username
        self.__password = password # private
        self.bio = " "
        self.highlights = []
        print(f"{self.username} Your account is created. Have fun with Instagram!")
        
    def getPassword(self):
        return self.__password
        
    @property
    def NRfollowers(self):
        return self._followers
        
    @property
    def NRfollowing(self):
        return self._following    
        
        
        
keerthana = Profile('Keerthana','ker123')    
nihitha = Profile('Nihitha','Nih786')

print('Keerthana Details'.center(40,'-'))
print(f'Username: {keerthana.username}')
print(f'Password: {keerthana.getPassword()}')
print(f'Bio: {keerthana.bio}')
print(f'Highlights: {keerthana.highlights}')
print(f'Posts: {keerthana.post}')
print(f'Followers: {keerthana.NRfollowers}')
print(f'Following: {keerthana.NRfollowing}')


print('Nihitha Details'.center(40,'-'))
print(f'Username: {nihitha.username}')
print(f'Password: {nihitha.getPassword()}')
print(f'Bio: {nihitha.bio}')
print(f'Highlights: {nihitha.highlights}')
print(f'Posts: {nihitha.post}')
print(f'Followers: {nihitha.NRfollowers}')
print(f'Following: {nihitha.NRfollowing}')

'''
Keerthana Your account is created. Have fun with Instagram!
Nihitha Your account is created. Have fun with Instagram!
-----------Keerthana Details------------
Username: Keerthana
Password: ker123
Bio:  
Highlights: []
Posts: []
Followers: {}
Following: {}
------------Nihitha Details-------------
Username: Nihitha
Password: Nih786
Bio:  
Highlights: []
Posts: []
Followers: {}
Following: {}

=== Code Execution Successful ===
'''



class Profile:
    def __init__(self,username,password):
        self._followers=set()
        self._following=set()
        self.posts=[]
        self.username=username
        self.__password=password
        self.bio=''
        print(f'\n{self.username}, Your account is created. Have fun with Instagram')

    def getPassword(self):
        return self.__password

    def setPassword(self,new_password):
        self.__password=new_password

    @property
    def NRfollowers(self):
        return self._followers

    @NRfollowers.setter
    def NRfollowers(self,req_uname):
        self._followers.add(req_uname)
        

    @property
    def NRfollowing(self):
        return self._following

    @NRfollowing.setter
    def NRfollowing(self,rai_uname):
        self._following.add(rai_uname)

keerthana= Profile('Keerthana','ker123')

print('Keerthana Details'.center(40,'-'))

print('\nBefore Changing')
print(f'Before Username: {keerthana.username}')
print(f'Before Password: {keerthana.getPassword()}')
print(f'Before Bio: {keerthana.bio}')
print(f'Before Posts: {keerthana.posts}')
print(f'Before Followers: {keerthana.NRfollowers}')
print(f'Before Following: {keerthana.NRfollowing}')

print('\nAfter Changing')
keerthana.username='skeerthana'
print(f'After Username: {keerthana.username}')

keerthana.setPassword('Keerthan@123')
print(f'After Password: {keerthana.getPassword()}')

keerthana.bio='Blogger'
print(f'After Bio: {keerthana.bio}')

keerthana.posts.extend(['Graduation.png','Fest.png','Travalling.mp4'])
print(f'After Posts: {keerthana.posts}')

keerthana.NRfollowers='nihitha'
keerthana.NRfollowers='leorah'
keerthana.NRfollowers='sowmya'
print(f'After Followers: {keerthana.NRfollowers}')

keerthana.NRfollowing='meghana'
keerthana.NRfollowing='maheswari'
keerthana.NRfollowing='revathi'
keerthana.NRfollowing='sunitha'
keerthana.NRfollowing='priyanka'
print(f'After Following: {keerthana.NRfollowing}')


nihitha= Profile('Nihitha','Nih876')
print('Nihitha Details'.center(40,'-'))
print(f'Username: {nihitha.username}')
print(f'Password: {nihitha.getPassword()}')
print(f'Bio: {nihitha.bio}')
print(f'Posts: {nihitha.posts}')
print(f'Followers: {nihitha.NRfollowers}')
print(f'Following: {nihitha.NRfollowing}')

'''

Keerthana, Your account is created. Have fun with Instagram
-----------Keerthana Details------------

Before Changing
Before Username: Keerthana
Before Password: ker123
Before Bio: 
Before Posts: []
Before Followers: set()
Before Following: set()

After Changing
After Username: skeerthana
After Password: Keerthan@123
After Bio: Blogger
After Posts: ['Graduation.png', 'Fest.png', 'Travalling.mp4']
After Followers: {'sowmya', 'leorah', 'nihitha'}
After Following: {'sunitha', 'revathi', 'priyanka', 'meghana', 'maheswari'}

Nihitha, Your account is created. Have fun with Instagram
------------Nihitha Details-------------
Username: Nihitha
Password: Nih876
Bio: 
Posts: []
Followers: set()
Following: set()

=== Code Execution Successful ===
'''



        
        
        
            
        
        
        
    
