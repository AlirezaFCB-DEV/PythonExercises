class car:
    def __init__(self, name: str, model: str, year: int, color: str):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def run(self, speed: int) -> str:
        print(f"This Car Can Driving With {speed}KM/H")


BugattiChiron = car("Bugatti", "Chiron", 2028, "WhiteBlue")
print(BugattiChiron)
BugattiChiron.run(450)
