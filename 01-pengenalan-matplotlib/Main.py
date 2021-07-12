import numpy as np
import matplotlib.pyplot as plt

# data

x = np.linspace(1,20,10)

# ada 2 cara pendekatan dalam visualisasi data 

# 1 pendekatan oo style







# 2 pendekatan plot style

print(x)

plt.plot(x,x, label = 'linear')
plt.plot(x , x**2, label = 'quadrat')
plt.plot(x, x**3, label = 'tripel')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('data perpangkatan')
plt.legend()
plt.show()
