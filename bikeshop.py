class Bike(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Shop(object):
    def __init__(self,name, inventory):
        self.name = name
        self.inventory = inventory
        
    def sell(self):
        #sell bike at 20% margin
        pass
    
    def profit(self):
        #displays profit for bike sold
        #print(sold)
        pass
    
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def buy(self):
        #buy bicycle
        pass
       
    
    
    
#Bikes

Huff = Bike("Huff", "20", 130)
BMX = Bike("BMX", "10", 300)
Trak = Bike("Trak", "8", 800)

bike_prices = {
    "Huff": Huff.cost,
    "BMX": BMX.cost,
    "Trak":Trak.cost,
    }
        

#Store

store_costs = {
    "Huff": (Huff.cost + (Huff.cost*.20)),
    "BMX": (BMX.cost + BMX.cost + (BMX.cost*20)),
    "Trak":(Trak.cost + (Trak.cost *.20)),
    }



bike_shop = Shop("Biffs Bikes", store_costs)


print(Huff.weight, Huff.cost)


#customers

Tom = Customer("Tom", 200)
Jo= Customer("Jo", 500)
Sue= Customer("Sue", 1000)
customers = [Tom, Jo, Sue]

budgets = {
    "Tom":Tom.budget,
    "Jo": Jo.budget,
    "Sue": Sue.budget,
    }



print(bike_prices)
print(budgets)
print(budgets["Tom"] - bike_prices["Huff"])

def buy_bike(x, y):
    if budgets[x] >= bike_prices[y]:
        return budgets[x] - bike_prices[y]
    else:
        print ("You don't have enough")


    
    
        