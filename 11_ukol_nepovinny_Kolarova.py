import pandas
import matplotlib.pyplot as plt
temperatures = pandas.read_csv('temperature.csv')

helsinki = temperatures[(temperatures['City'] == 'Helsinki')]
miami_beach = temperatures[(temperatures['City'] == 'Miami Beach')]
tokyo = temperatures[(temperatures['City'] == 'Tokyo')]

data_1=(helsinki['AvgTemperature'])
data_2=(miami_beach['AvgTemperature'])
data_3=(tokyo['AvgTemperature'])
data=[data_1,data_2,data_3]

plt.title("Teploty ve světových městech\n", size=20, fontweight='bold')
plt.xlabel("\nSvětová města\n",size=14)
plt.ylabel("\nStupně Fahnheita\n",size=14)

box_plot_data=[data_1,data_2,data_3]
box = plt.boxplot(box_plot_data, patch_artist = True)

# nastavení různých barev boxů
colors = ['#BD425E','#CA8368','#CA68AF']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# pojmenování jednotlivých DataFramů
plt.xticks([1, 2, 3], ['Helsinki', 'Miami Beach', 'Tokyo'])
plt.show()