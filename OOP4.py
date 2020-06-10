import random

class Article:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.price = 0

    def setPrice(self, price):
        self.price = price

class Supermarket:
    def __init__(self, name):
        self.name = name
        self.articles = {}

    def addArticle(self, article, amount):
        self.articles[article] = amount

    def discountAktion(self, discount, category):
        for k,v in self.articles.items():
            if category == k.category:
                d = k.price * discount
                k.price -= d
    
    def sellArticle(self, article, amount):
        for k, v in self.articles.items():
            if k == article:
                if amount <= v:
                    self.articles[article] -= amount
                    print(f"Article {article.name}, amount: {amount} article(s) have been sold. Amount: {self.articles[article]} article(s) is left.")
                else:
                    print(f"There is not enough articles in {self.name}. Amount: {self.articles[article]} article(s) is left.")


    def __repr__(self):
        list = []
        for k,v in self.articles.items():
            list.append({k.name : k.price})
        return f"{self.name} offer these articles:\n{[x for x in list]}"

a1 = Article ("Fresh Soap 200g", "hygiene")
a2 = Article ("Rose Shampoo 200 ml", "hygiene")
a3 = Article ("Coal Toothpaste 50g", "hygiene")
a4 = Article ("Mango 1 Pc", "fruits")
a5 = Article ("Orange 1 Kg", "fruits")
a6 = Article ("Apple 1 Kg", "fruits")
mk = Supermarket("Happymarket")

for a in (a1, a2, a3, a4, a5, a6):
    a.setPrice(random.randint(1,320))
    mk.addArticle(a, random.randint(1,40))

print(mk) # prints all items in supermarket
mk.discountAktion(0.25, "fruits" ) # 25% discount on fruits
print(mk) # prints all items in supermarket

mk.sellArticle(a1, 4)