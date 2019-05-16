import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

people_df = pd.read_csv('./fer2013.csv')
arr_np = people_df['pixels']
