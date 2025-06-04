# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 13:16:35 2025

@author: user
"""

import seaborn as sns
import pandas as pd
from scipy import stats

titanic = sns.load_dataset('titanic')

live = pd.crosstab(titanic['pclass'], titanic['alive'])
print(live)

stats.chi2_contingency(live)



