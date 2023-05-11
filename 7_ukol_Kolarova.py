class Car():
    def __init__(self, registration_plate, car_type, km):
        self.registration_plate = registration_plate
        self.car_type = car_type
        self.km = km
        self.avability = True
    
    def __str__(self):
        if self.avability:
            return f"Potvrzuji zapůjčení vozidla."
        return f"Vozidlo není k dispozici."

    def get_info(self):
        print(f"{self.car_type}, SPZ: {self.registration_plate}, najeto {self.km} km.")

    def get_car(self):
        self.avability = False

peugeot_403_cabrio = Car("4A2 3020","Peugeot 403 Cabrio", 47534)
skoda_octavia = Car("1P3 4747","Škoda Octavia", 41253)

wish = input("Jakou značku auta si přejete půjčit? Peugeot či Škoda?\n")

if wish == "Peugeot":
    peugeot_403_cabrio.get_info()
    print(peugeot_403_cabrio)
    peugeot_403_cabrio.get_car()
    print(peugeot_403_cabrio)
elif wish == "Škoda":
    skoda_octavia.get_info()
    print(skoda_octavia)
    skoda_octavia.get_car()
    print(skoda_octavia)
else:
    print("Vámi požadované vozidlo nemáme.")