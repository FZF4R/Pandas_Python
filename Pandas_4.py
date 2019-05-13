import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

P = pd.read_csv('./fer2013.csv')
Imge = P['pixels'].tail(7).values

for i in range(7):
    img = np.array(list(map(float, Imge[i].split())))
    img = img.reshape([48,48])
    plt.imshow(img)
    plt.show()
    
