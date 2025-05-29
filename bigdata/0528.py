import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\ind_ttest.csv")

group_1 = df.loc[df.group =='A','height']
group_2 = df.loc[df.group =='B', 'height']

stats.shapiro(group_1)  
stats.shapiro(group_2) 

stats.levene(group_1, group_2)

result = stats.ttest_ind(group_1, group_2, equal_var= True) 

#%%
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\user\Desktop\donga\donga4_1\bigdata\dfdata\prestige.csv")

bc = df.loc[df.type =='bc','income']
wc = df.loc[df.type =='wc','income']

print("bc정규성 검정 : ", stats.shapiro(bc))
print("wc정규성 검정 : ", stats.shapiro(wc))

print("등분산성 검정 : ", stats.levene(bc,wc))

result = stats.ttest_ind(bc, wc, equal_var=True)

print(result)