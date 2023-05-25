import pandas
import pytemperature

temperatures = pandas.read_csv('temperature.csv')
temperatures["AvgTemperatureCelsia"] = pytemperature.f2c(temperatures["AvgTemperature"])
print(temperatures)

print("Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).")
november_13 = temperatures[temperatures["Day"] == 13]
print(november_13)

print("Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.")
us_13 = temperatures[temperatures["Day"] == 13 & (temperatures["Country"] == 'US')]
print(us_13)
us_13.to_csv("us_13.csv")

print("Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.")
city = us_13[us_13["City"] == 'Washington']
city_2 = us_13[us_13["City"] == 'Philadelphia']
print(city)
print(city_2)

city_3 = (us_13[us_13["City"].isin(["Washington", "Philadelphia"])])
print(city_3)