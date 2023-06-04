import pandas

praha = pandas.read_csv('zam_praha.csv')
praha["město"] = "Praha"

plzen = pandas.read_csv('zam_plzen.csv')
plzen["město"] = "Plzeň"

liberec = pandas.read_csv('zam_liberec.csv')
liberec["město"] = "Liberec"

cz = pandas.concat([praha, plzen, liberec])

platy = pandas.read_csv('platy_2021_02.csv')

february = pandas.merge(cz, platy, on="cislo_zamestnance")
print(february)

print("\ncz = 56, platy = 43 -> 13 zaměstnanců v únoru pro podnik už nepracovalo")
print(len(cz)-len(february))

print("\nPrůměrný plat zaměstnanců:")
average = february.groupby('město')['plat'].mean()
print(average)