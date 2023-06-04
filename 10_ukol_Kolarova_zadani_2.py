import pandas

vykazy = pandas.read_csv('vykazy.csv')
print(vykazy)

print("\nPočet vykázaných hodin za jednotlivé projekty:")
average = vykazy.groupby('project')['hours'].sum()
print(average)