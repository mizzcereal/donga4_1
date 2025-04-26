# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 21:46:04 2025

@author: Admin
"""

import pandas as pd

favorite = pd.Series(['winter', 'summer', 'spring', 'summer', 'summer', 'fall', 'fall', 'summer'])

favorite

#%%
print(favorite.value_counts())

print(favorite.value_counts()/favorite.size)

#%%
import matplotlib.pyplot as plt

fd = favorite.value_counts()

fd.plot.barh(rot = 0)

#%%
import numpy as np

mpg = pd.read_excel(r"C:\Users\Admin\Desktop\donga\donga4_1\bigdata\dfdata\mpg.xlsx")

mv = mpg['category'].value_counts().head()


mv.plot.pie(ylabel= "", autopct = "%1.0f%%")

plt.show()



