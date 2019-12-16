# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On charge le dataset
dataframe = pd.read_csv('mesures/mesures.csv')

print(dataframe)

plt.subplot(211)
plt.plot(dataframe['VM'], 'ro', markersize=1)
errorsdf = np.abs(dataframe['VM'] - dataframe['VT'])
plt.subplot(212)
plt.plot(errorsdf, 'ro', markersize=1)
plt.show()
errors = dataframe[np.abs(dataframe['VM'] - dataframe.VT) > 1]
print(errors)

