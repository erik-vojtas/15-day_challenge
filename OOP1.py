# Write a Python Class called ShoppingCart, which contains
# • a method “addItem (item)” to add new items to the shopping cart.
# • If the item already exists in the ShoppingCart increase its quantity
# • a method “pour (cart)” to pour items from another shopping cart to this shopping cart
# • Override the + operator of the shopping cart to enable merging the contents of
# two shopping carts and creating a new shopping cart object with the contents of those two
# • Each item in the ShoppingCart has a name, price and quantity
# • Create a new method in ShoppingCart to calculate the total price
# • Create a new method called “limitPrice(n)” in the ShoppingCart to automatically remove
# minimum number of items from the cart so that the total price is below the given limit.


class ShoppingCart():
    def __init__(self):
        self.dict_of_items = {}

    def addItem(self, item):
        if item in self.dict_of_items:
            self.dict_of_items[item] += 1
        else:
            self.dict_of_items[item] = 1

    def pour(self, cart):
        for k, v in cart.dict_of_items.items():
            if k in self.dict_of_items:
                self.dict_of_items[k] += 1
            else:
                self.dict_of_items[k] = 1

    def __add__(self, other):
        for k, v in other.dict_of_items.items():
            if k in self.dict_of_items:
                self.dict_of_items[k] += 1
            else:
                self.dict_of_items[k] = 1

    def getTotalPrice(self):
        sum = 0
        for k, v in self.dict_of_items.items():
            sum += k.price * v
        print(f"$ {sum}")
        return sum

    def printItemsFromCart(self):
        for k, v in self.dict_of_items.items():
            print({k.name: v}, end= " ")
        print("\n")

    def limitPrice(self, limit):
        new_dict = {}
        sum = 0
        if self.getTotalPrice() <= limit:
            print("You have enough money to buy all items in your shopping cart!")
        else:
            for k, v in self.dict_of_items.items():
                if k.price <= limit:
                    sum += k.price * v
                    if sum <= limit:
                        new_dict[k] = v
            value = {k: self.dict_of_items[k] for k in set(self.dict_of_items) - set(new_dict)}
            for k,v in value.items():
                print(f"The item {k.name} has been removed from the shopping cart.")
            self.dict_of_items = new_dict
        return self.dict_of_items


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


sc1 = ShoppingCart()
sc2 = ShoppingCart()
ball = Item("ball", 5.00)
shoes = Item("sports shoes - Nike", 50.00)
watch = Item("Casio watch", 120.25)

sc1.addItem(ball)
sc1.addItem(shoes)
sc1.addItem(shoes)
print(sc1.getTotalPrice())

sc2.addItem(watch)
# sc1.pour(sc2)
sc1+sc2
sc1.getTotalPrice()

sc1.printItemsFromCart()
sc1.limitPrice(100)
sc1.printItemsFromCart()
sc1.getTotalPrice()
