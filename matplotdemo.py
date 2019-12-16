import matplotlib.pyplot as plt
import scipy.stats as stats
import csv
import numpy as np

with open("house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = np.array([float(row["loyer"]) for row in reader])
    surfaces = np.array([float(row["surface"]) for row in reader])
    loyersm2 = loyers / surfaces

    print(f"Mean: {np.mean(loyersm2)}")
    print(f"Std: {np.std(loyersm2)}")
    print(f"Median: {np.median(loyersm2)}")

plt.scatter(surfaces, loyers)



slope, intercept, r_value, p_value, std_err = stats.linregress(surfaces, loyers)
print(r_value, p_value, std_err)
f = lambda x : slope * x + intercept
plt.scatter(surfaces, [f(x) for x in surfaces])

plt.show()