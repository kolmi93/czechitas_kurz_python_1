import pandas
import pytemperature
temperatures = pandas.read_csv('temperature.csv')
print(temperatures)

print("\nPřidání nového sloupce 'Celsia'.")
temperatures["AvgTemperatureCelsia"] = pytemperature.f2c(temperatures["AvgTemperature"])
print(temperatures)

print("\nDotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.")
thirty = temperatures[temperatures["AvgTemperatureCelsia"] > 30]
print(thirty)

print("\nDotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).")
europe_15 = temperatures[(temperatures["AvgTemperatureCelsia"] > 15) & (temperatures["Region"] == 'Europe')]
print(europe_15)

print("\nDotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?")
between = temperatures[(temperatures["AvgTemperatureCelsia"] > 30)  | (temperatures["AvgTemperatureCelsia"] < -10)]
print(between)