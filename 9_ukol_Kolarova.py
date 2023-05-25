import pandas
temperatures = pandas.read_csv('temperature.csv')
print(temperatures)

print("\n1. Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního?")
prague = temperatures[temperatures["City"] == 'Prague']
print(prague)

print("\n2. Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.")
eighty = temperatures[temperatures["AvgTemperature"] > 80]
print(eighty)

print("\nDotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).")
europe_60 = temperatures[(temperatures["AvgTemperature"] > 60) & (temperatures["Region"] == 'Europe')]
print(europe_60)

print("\nDotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než -20 stupňů.")
between = temperatures[(temperatures["AvgTemperature"] > 80)  | (temperatures["AvgTemperature"] < -20)]
print(between)