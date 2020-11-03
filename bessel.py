import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt 


x = np.linspace(0, 20, 1000)

for i in range(0,5):
	J=jv(i, x)
	plt.plot(x, J, label= r'$J_' + str(i) + '(x)$')


plt.legend()
plt.title('BESSEL FUNCTION', fontweight = 'bold')
plt.xlabel('x', fontweight='bold')
plt.ylabel('$J_v(x)$', fontweight = 'bold')
plt.grid()
plt.show()