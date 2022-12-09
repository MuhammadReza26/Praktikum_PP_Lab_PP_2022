class Human:
    def __init__(self,name,pos_x):
        self.name = name
        self.__position =  pos_x 
    
    #Setter
    def movement(self,move):
        if move == "L":
            self.__position-= self._speed
        elif move == "R":
            self.__position += self._speed

    #Getter
    def getPosition(self):
        return self.__position

class Hero(Human):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 15 
        self._health = 400
        self._armor = 15
        self._speed = 3

    def setSpeed(self,speed):
        self._speed = speed
        
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 26
        self._armor = 30
    
    def attack(self,target):
        target._health -= self._power 
    
    def special(self,target): 
        self._power = 32   
        self._armor = 45
        target._health -= self._power
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self.speed 

class Assassin(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)            
        self._power = 35
        self.speed = 4
    
    def attack(self,target):
        target._health -= self._power
    

    def special(self,target): 
        self._speed = 7   
        self._armor = 42
        target._health -= self._power
    
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self.speed    

class Support(Hero):
    def __init__(self,nama,pos_x):
        super().__init__(nama,pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def attack(self,target):
        target._health -= self._power

    def setSpeed(self,speed):
        self._speed = speed    
    
    def special(self,target): 
        self._speed = 6   
        target._health += 150
    
    def getPower(self):
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def getSpeed(self):
        return self._speed 

warrior = Warrior("Balmond", pos_x=10)
assassin = Assassin("Lancelot", pos_x=25)
support = Support("Estes",pos_x=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
print('Posisi Awal',warrior.getPosition())
warrior.movement('L')
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
print('Posisi Akhir',warrior.getPosition())
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())
#sebelum
print("posisiawal",assassin.getPosition())
assassin.movement('R')
assassin.movement('R')
print("posisi akhir",assassin.getPosition())
print("posisiawal",support.getPosition())
support.setSpeed(8)
support.movement('L')
print("posisiakhir",support.getPosition())
print("posisiakhir",support.getSpeed())




