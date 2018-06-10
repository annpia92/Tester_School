"""Implementation of the class Stock"""
import copy
import json
class Stock:
    def __init__(self, initial):
        self.products = dict(initial)


    def resupply(self, product, count):
        """Adds new products to the stock."""
        if count <= 0:
            raise ValueError('Can only resupply with positive count.')
        self.products[product]=self.products.get(product, 0) + count
        return self.products

    def withdraw(self, product, count):
        """Withdraws products from the stock."""
        if count <= 0:
            raise ValueError('Can only withdraw with positive count.')
        if product not in self.products:
            raise ValueError("unknown product: "+product)
        if self.products[product] < count:
            raise ValueError("insufficient amount of the product in stock.")
        self.products[product] -= count
        return self.products



    def available_items(self):
        """Returns the items available in the stock."""
        items = {}
        for product, count in self.products.items():
            if count > 0:
                items[product] = count
        return items

    def save(self, file_obj):
        for product, count in self.products.items():

            file_obj.write(product+','+str(count)+'\n')

    def to_json(self):
       return json.dumps(self.products)


    @staticmethod
    def from_json(json_str):
        return Stock(json.loads(json_str))

    def to_json_file(self, output_file):
        json.dump(self.products, output_file)

    @staticmethod
    def from_json_file(json_file):
        return Stock(json.load(json_file))


    @staticmethod
    def load(file_obj):
        data = {}
        for line in file_obj:
            record = line.rstrip('\r\n').split(',')
            data[record[0]] = int(record[1])
        return Stock(data)


    @staticmethod
    def foo(a):
        print("Static method called!", a)

stock = Stock({'orange': 2, "lemon": 5})
stock.resupply("lemon", 5)
print("Stan po dodaniu ", stock.products)
stock.withdraw("orange", 1)
print("Stan po wyjeciu ", stock.products)
stock.available_items()
print("available items: ", stock.available_items())
Stock.foo('a')
with open('magazyn.csv', 'wt') as data_file:
    stock.save(data_file)
with open('magazyn.csv', 'rt') as data_file:
    stock2 = Stock.load(data_file)
print(stock2.available_items())
print(stock.to_json())
stock_json = stock.to_json()
stock2 = Stock.from_json(stock_json)
print(stock2.available_items() == stock.available_items())
with open('stock.json', 'wt') as stock_json:
    stock.to_json_file(stock_json)
with open('stock.json', 'rt') as stock_json:
    stock4 = Stock.from_json_file(stock_json)
print(stock4.products)

