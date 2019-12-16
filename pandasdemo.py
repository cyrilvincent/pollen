import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

with sqlite3.connect("house/house.db3") as conn :
    #house_data = pd.read_csv('house/house.csv')
    house_data = pd.read_sql('select * from house', conn)
    house_data = house_data[house_data.surface < 250]
    print(house_data)
    plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)
    plt.show()
