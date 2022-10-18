class Items():
    def __init__(self, code, price, quantity):
        self.code = code
        self.price = price
        self.quantity = quantity
        
    def total_cost(self):
        self.cost = self.price * self.quantity 
        return   self.cost

    def discount(self) -> float:
        if (self.price * self.quantity) > 20000:
            discount = 0.14 * self.cost
        elif (self.price * self.quantity) >= 10000:
            discount = 0.1 * self.cost
        else:
            discount = 0
        return discount

    def net_cost(self, total_cost, discount):
        return total_cost - discount
    

n = int(input("Enter the number of items: "))
all_items = []

for i in range(n):
    print("Item {}".format(i + 1))
    a = input("Enter item's product code: ")
    b = int(input("Enter item's price: "))
    c = int(input("Enter item's quantity: "))
    print()  
    item = Items(a, b, c)
    all_items.append(item)  

total_discount = 0
total_cost_sum = 0
total_net = 0
for item in all_items:
    total_cost_sum += item.total_cost()
    total_discount += item.discount()
    total_net += item.net_cost(item.total_cost(), item.discount())

print("+"+"-" * 11 + "+" + "-"*10 + "+"+ "-"*11 + "+" + "-"*13 + "+" + "-" *13 + "+" + "-" * 13 + "+")
print("| Item Code |   Price  |  Quantity |  Total Cost |   Discount  |   Net Cost  |")
print("+"+"-" * 11 + "+" + "-"*10 + "+"+ "-"*11 + "+" + "-"*13 + "+" + "-" *13 + "+" + "-" * 13 + "+")
for item in all_items:
    print("|  {:7.6}  |{:9} | {:9} |{:12} |{:12.2f} |{:12.2f} |".format(item.code, item.price, item.quantity, item.total_cost(), item.discount(), item.net_cost(item.total_cost(), item.discount())))
print("+"+"-" * 11 + "+" + "-"*10 + "+"+ "-"*11 + "+" + "-"*13 + "+" + "-" *13 + "+" + "-" * 13 + "+")
print("| Total Cost: " + " "* 49 +  "{:12.2f}".format(total_cost_sum)+ " "*2 + "|")
print("| Discount: "+ " "* 51 +  "{:12.2f}".format(total_discount) + " "*2 + "|")
print("| Net Cost: "+ " "* 51 +  "{:12.2f}".format(total_net) + " "*2 + "|")
print("+"+"-" * 11 + "+" + "-"*10 + "+"+ "-"*11 + "+" + "-"*13 + "+" + "-" *13 + "+" + "-" * 13 + "+")
