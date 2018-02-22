import pandas as pd
import numpy as np

df1 = pd.read_csv('winequality-red.csv', delimiter=';')
df2 = pd.read_csv('winequality-white.csv', delimiter=';')

#print(df.info())
#print(df.describe())
#print(df.shape)

red_alc = df1['alcohol'].mean()
white_alc = df2['alcohol'].mean()

df1['high_alc'] = (df1['alcohol'] > red_alc)
df2['high_alc'] = (df2['alcohol'] > white_alc)

#df1.query('high_alc == False')
df1[df1.high_alc == False]
df2[df2.high_alc == False]

#df1['acidity_bin'] = pd.qcut(df1['fixed acidity'], 5, labels=False) ##qcut uses equal sized bins.
#df2['acidity_bin'] = pd.qcut(df2['fixed acidity'], 5, labels=False)
df1['acidity_bin'] = pd.cut(df1['fixed acidity'], 5, labels=False)
df2['acidity_bin'] = pd.cut(df2['fixed acidity'], 5, labels=False)
#df1.query('acidity_bin < 4')
#df2.query('acidity_bin < 4')

#pd.pivot_table(df1, values = 'alcohol', index = 'quality', columns = 'high_alc')
#pd.pivot_table(df2, values = 'alcohol', index = 'quality', columns = 'high_alc')

#pd.pivot_table(df1, values = 'alcohol', index = 'quality', columns = 'acidity_bin')
print(pd.pivot_table(df2, values = 'alcohol', index = 'quality', columns = 'acidity_bin'))
