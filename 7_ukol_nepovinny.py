class Car():
    def __init__(self, registration_plate, car_type, km):
        self.registration_plate = registration_plate
        self.car_type = car_type
        self.km = km
        self.avability = True
    
    def __str__(self):
        if self.avability:
            return f"Potvrzuji zapůjčení vozidla."
        return f"Vozidlo není k dispozici"

    def get_info(self):
        print(f"{self.car_type}, SPZ: {self.registration_plate}, najeto {self.km} km.")

    def get_car(self):
        self.avability = False

    def return_car(self,return_km, days):
        self.avability = True
        self.km = return_km
        if days < 7:
            price=days*400
            print(f"Za půjčení auta zaplatíte {price},- Kč.")
        else:
            price=days*300
            print(f"Za půjčení auta zaplatíte {price},- Kč.")

peugeot_403_cabrio = Car("4A2 3020","Peugeot 403 Cabrio", 47534)
skoda_octavia = Car("1P3 4747","Škoda Octavia", 41253)

wish = input("Jakou značku auta si přejete půjčit? Peugeot či Škoda?\n")

if wish == "Peugeot":
    peugeot_403_cabrio.get_info()
    print(peugeot_403_cabrio)
    peugeot_403_cabrio.get_car()
    print(peugeot_403_cabrio)
    q_return_km = int(input("Uveďte stav tachometru při vrácení?\n"))
    q_days = int(input("Kolik dnů jste měl/a vozidlo půjčeno?\n"))
    peugeot_403_cabrio.return_car(q_return_km, q_days)
    peugeot_403_cabrio.get_info()
    print(peugeot_403_cabrio.avability)
elif wish == "Škoda":
    skoda_octavia.get_info()
    print(skoda_octavia)
    skoda_octavia.get_car()
    print(skoda_octavia)
    q2_return_km = input("Uveďte stav tachometru při vrácení?\n")
    q2_days = input("Kolik dnů jste měl/a vozidlo půjčeno?\n")
    skoda_octavia.return_car(q2_return_km, q2_days)
    skoda_octavia.get_info()
    print(skoda_octavia.avability)
else:
    print("Vámi požadované vozidlo nemáme.")