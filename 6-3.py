class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"

    def show_attributes(self):
        print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

n1 = Nigiri()
n1.show_attributes()

class Maguro(Nigiri):
    pass

m1 = Maguro()
m1.show_attributes()

class Maguro(Nigiri):
    top = "まぐろ"
m3 = Maguro()
m3.show_attributes()

class Maguro(Nigiri):
    top = "まぐろ"
    price = 100

    def show_attributes(self):
        super().show_attributes()

    def show_one_dish_price(self, num_nigiri=2):
        result = self.price * num_nigiri
        print("一皿({}かん)の値段: {}円".format(num_nigiri, result))

m5 = Maguro()
m5.show_attributes()
m5.show_one_dish_price()

class NigiriNew(Nigiri):

    def __init__(self, wasabi="わさび抜き"):
        self.wasabi = wasabi

    def show_attributes(self):
        super().show_attributes()
        print("wasabi: {}".format(self.wasabi))

class Maguro(NigiriNew):
    top = "まぐろ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print("price: {}円".format(self.price))

m6 = Maguro("わさび入り")
m6.show_attributes()
