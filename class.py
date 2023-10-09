class Student():
    def __init__(self, name, Class, game, movie):
        self.name = name
        self.Class = Class
        self.game = game
        self.movie = movie

    def play_game(self):
        return self.game

    def best_movie(self):
        return self.movie
    
    def __str__(self):
        return f"{self.name} is a student {self.movie} is intresting. I love playing {self.game}"
    
Kameshire = Student("KCoder", "Jss3", "CODM", "Naruto Shippumen VI")
Awesome = Student("Asome", "Basic 5", "GTA V", "Justice League")
Great = Student("Greatee", "Jss3", "Blox Fruit", "One Piece")
print(Kameshire)
print(Awesome)
print(Great)

