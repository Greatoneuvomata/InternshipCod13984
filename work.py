class Game():
    def __init__(self, name, looks, fruit):
        self.name = name
        self.looks = looks
        self.fruit = fruit

    def names(self):
        return self.name

    def change_fruit(self, new_fruit):
        self.fruit = new_fruit

    def  __str__(self):
        return f"His name is {self.name} He looks {self.looks}, His best fruit is {self.fruit}"

luffy = Game("Luffy", "Cool", "Dragon")
luffy.change_fruit("Ice")
print(luffy)