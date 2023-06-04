import pandas

vykazy = pandas.read_csv('vykazy.csv')
vykazy = vykazy.rename(columns={'emloyee_id': 'cislo_zamestnance'})
print(vykazy)

praha = pandas.read_csv('zam_praha.csv')
praha["město"] = "Praha"
plzen = pandas.read_csv('zam_plzen.csv')
plzen["město"] = "Plzeň"
liberec = pandas.read_csv('zam_liberec.csv')
liberec["město"] = "Liberec"

cz = pandas.concat([praha, plzen, liberec])
print(cz)

print("\nPropojení tabulky výlazů s tabulkou se zaměstnanců:")
together = pandas.merge(cz, vykazy, on="cislo_zamestnance")
print(together)

print("\nStatistika vykázaných hodin za jednotlivé kanceláře:")
concrete = together.groupby('město')['hours'].sum()
print(concrete)