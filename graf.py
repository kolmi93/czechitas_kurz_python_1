import pandas
import matplotlib.pyplot as plt

url = "https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/vizualizace/ucet.csv"
ucet = pandas.read_csv(url, names=['datum', 'pohyb'], index_col='datum')
print(ucet)

ucet.plot()
plt.show()