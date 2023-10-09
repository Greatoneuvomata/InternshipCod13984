# class Game():
#     def __init__(self, name, looks, fruit):
#         self.name = name
#         self.looks = looks
#         self.fruit = fruit

#     def names(self):
#         return self.name
#     def look(self):
#         return self.looks
    
#     def change_fruit(self, new_fruit):
#         self.fruit = new_fruit
        
#     def change_name(self, new_name):
#         self.name = new_name
#     def __str__(self):
#         return f"His name is {self.name} He Looks {self.looks} His best fruit is {self.fruit}"

# blox = Game("Kaido", "Somehow", "Dragon")
# blox.change_fruit("Dough")
# blox.change_name("Katakuri")
# print(blox)


class Food():
    def __init__(self, name, smell, sweet):
        self.name = name
        self.smell = smell
        self.sweet = sweet

    def names(self):
        return self.name
    def look(self):
        return self.sweet
    
    def change_food(self, new_food):
        self.name = new_food
        
    def change_smell(self, new_smell):
        self.smell = new_smell
    def __str__(self):
        return f"The name of the food is {self.name} it smells very {self.smell} it is very {self.sweet}"

end = Food("Rice", "Nice", "Delicious")
end.change_food("Beans")
end.change_smell("Bad")
print(end)