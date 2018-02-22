import numpy as np # Numpy is generally used for making fancier lists called arrays and series.
import pandas as pd # Pandas is super important, it's the foundation data analysis library we're using.
import matplotlib.pyplot as plt # Matplotlib is the python plotting library and folks generally import it as "plt"
import matplotlib
matplotlib.style.use('ggplot')
#import seaborn as sns  # Seaborn is a wrapper for Matplotlib and makes some things easier, generally imported as "sns"

database = 'incomedata.csv' # Dataset location

df = pd.read_csv(database,
                 low_memory=False,             ### Prevents low_memory warning
                 na_values=['UNKNOWN', 'UNK'], ### Adds UNKNOWN and UNK to list of NULLs
                 na_filter=True,               ### Detect NA/NaN as actual NULL values
                 skip_blank_lines=True)        ### Skip boring blank lines

#print(df.head(n=10))
print(df.info())
#print(df.shape) #32561 rows, 15 columns

#boxplot = df['income'].plot(kind='box') #significant outliers above 400k.
#histplot = df['income'].plot(kind='hist')
#group_gender = df.groupby('gender')
#group_gender.mean()['income'].plot(kind='bar') #data suggests descrepancy between male and female average income is negligible.
#group_age = df.groupby('age')
#group_age.mean()['income'].plot(kind='bar') #data suggests decrease in average income by age.
#histplot = df['age'].plot(kind='hist') #much fewer samples for ages > 50.
group_country = df.groupby('nativecountry')
#group_country.mean()['income'].plot(kind='bar')
group_country.count()['income'].plot(kind='bar')
plt.show()


#group_quality = df.groupby('quality')
#group_quality.mean()['chlorides'].plot(kind='bar')
##group_pH = df.groupby('pH')
#group_pH.mean()['alcohol'].plot(kind='line')
#df.plot(kind = 'scatter',x='pH',y='alcohol')
#df.plot(kind = 'scatter',x='pH',y='total_acidity')
#df['quality'].plot(kind='hist')
#df['citric acid'].plot(kind='box')
