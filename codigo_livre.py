class Phone:
    name = "Nokia1220"
    typePhone = "Nokia"
    color = "Blue"
    battery = "Infinite"
    has_cam = False

    def do_call(self):
        print("Calling .....")

    def play_game(self):
        print("Playing Snake game")

    def music(self):
        print("Playing music")


class Car:
    def __init__(self, make, model, year, mileage=0):

        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self._fuel_level = 65.8

    @property
    def fuel_level(self):
        return self._fuel_level

    def drive(self, distance):
        if distance < 0:
            raise ValueError("Distancia não pode ser negativa")

        fuel_need = distance * 0.1

        if fuel_need > self._fuel_level:
            raise ValueError("Combustivel insuficiente para o trajeto")

        self.mileage += distance
        self._fuel_level -= fuel_need

    def refuel(self, amout):
        if amout < 0:
            raise ValueError("A quantidade nao pode ser negativa né, te liga !")

        new_fuel_level = self._fuel_level + amout
        if new_fuel_level > self._fuel_level:
            raise ValueError("Voce excedeu a capacidade do tanque !!")

    def __str__(self):
        return f"{self.year} {self.make} {self.mileage}"


carro = Car("Fusca", "Volksvagem", 1981, mileage=23)

print(carro)

celular = Phone()

celular.play_game()
