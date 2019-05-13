import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

P = pd.read_csv('./fer2013.csv')
Imge = P[P['emotion']==1]['pixels'].values

for i in range(7):
    x=random.randrange(len(Imge))
    img = np.array(list(map(float, Imge[x].split())))
    img = img.reshape([48,48])
    plt.imshow(img)
    plt.show()
#C:\Users\National Brother\AppData\Local\Programs\Python\Python37\lib\site-packages\matplotlib\image.py