import pandas
import matplotlib.pyplot as plt

platy = pandas.read_csv('platy_2021_02.csv')
y=platy['plat']
plt.ylim(0, 14)
plt.hist(y, bins=5, color='#BD425E')
plt.title("Platy zaměstnanců v měsíci únoru r. 2021")
plt.xlabel("\nVýše platu\n")
plt.ylabel("\nČetnnost výskytu\n")
plt.show()