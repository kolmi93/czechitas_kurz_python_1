import pandas
import matplotlib.pyplot as plt

platy = pandas.read_csv('platy_2021_02.csv')

# definování X a Y
x=platy['cislo_zamestnance']
y=platy['plat']
fig, ax = plt.subplots()

# popis grafu - vpravo nahoře
bar_label='zaměstnanci'
bar_colors='tab:orange'

ax.bar(x, y, label=bar_label, color=bar_colors)

# popisy grafu - hlavní + x,y
ax.set_ylabel('\nVýše platu\n', size=12)
ax.set_xlabel('\nČíslo zaměstnance\n',size=12)
ax.set_title('Platy zaměstnanců v měsíci únoru r. 2021\n', size=20, fontweight='bold')

#obsah grafu + popisky
bar_container = ax.bar(x, y, color='orange')
ax.bar_label(bar_container, rotation='vertical')
ax.legend(title='GRAF', loc='upper right')
plt.show()