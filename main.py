import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(10, std, 1000) for std in range (1, 6)]

plt.violinplot(data)
plt.xlabel('Data')
plt.ylabel('Density')
plt.title('Violin Plot')
plt.show()