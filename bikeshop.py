class Bike(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Shop(object):
    def __init__(self,name, inventory):
        self.name = name
        self.inventory = inventory
        self.revenue = 0
    
        
    def sell(x):
        #sell bike at 20% margin
        revenue = self.revenue + [x + (x *.20)]
        return revenue
        
        
        
    
    def profit(self):
        #displays profit for bike sold
        profit = revenue - x
        return profit
       
    
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def buy(self): #not sure how to set this up
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

inventory = [Huff, BMX, Trak]
print(inventory)

# this adds 20% mark up to costs
store_costs = {
    "Huff": (Huff.cost + (Huff.cost*.20)), 
    "BMX": (BMX.cost + BMX.cost + (BMX.cost*20)),
    "Trak":(Trak.cost + (Trak.cost *.20)),
    }



bike_shop = Shop("Biffs Bikes", inventory)




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

def buy_bike(x, y): #should this go in customer class?
    if budgets[x] >= bike_prices[y]:
        return budgets[x] - bike_prices[y]
    else:
        print ("You don't have enough")


    
    
        