import pandas

praha = pandas.read_csv('zam_praha.csv')
praha["město"] = "Praha"

plzen = pandas.read_csv('zam_plzen.csv')
plzen["město"] = "Plzeň"

liberec = pandas.read_csv('zam_liberec.csv')
liberec["město"] = "Liberec"

cz = pandas.concat([praha, plzen, liberec], ignore_index=True)
platy = pandas.read_csv('platy_2021_02.csv')

#vypíše i ty zaměsnance, co nemají plat
february = pandas.merge(cz, platy, on="cislo_zamestnance", how="outer")
print(february)

print("\nPočet zaměstnanců, kteří v naší firmě již nepracují:")
out_no = len(february[february["plat"].isnull()])
print(out_no)

print("\nZaměstnanci, kteří v naší firmě již nepracují (celý seznam):")
out_name = (february[february["plat"].isnull()])
print("\nZaměstnanci, kteří v naší firmě již nepracují (jména):")
print(out_name.groupby("jmeno")["prijimeni"].sum())

out_name.to_csv('propusteni_zam.csv')