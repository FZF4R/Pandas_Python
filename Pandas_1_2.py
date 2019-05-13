import pandas
import matplotlib.pyplot as plt
#from PIL import import Image

#__1
P = pandas.read_csv('./fer2013.csv')
print("Số dòng:",len(P))

#__2
P['emotion'].value_counts().plot(kind='bar')
plt.show()

