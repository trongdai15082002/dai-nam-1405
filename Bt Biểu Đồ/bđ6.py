import matplotlib.pyplot as plt
import numpy as np
plt.subplot(2,1,1)
plt.plot([1,2,3,4],[1,4,9,16],'go')
plt.title('1st subplot')

plt.subplot(2,1,2)
plt.plot(x,y, 'r^')
plt.title('2nd subplot')

plt.suptitle("My sub-plot")
plt.show()