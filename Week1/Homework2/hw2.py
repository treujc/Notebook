import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.covariance import EllipticEnvelope


traindf = pd.read_csv("aps_failure_training_set.csv",na_values=['na'])#usecols=[0,1,2,4,5])
traindf = traindf.dropna() #drop all rows with Nan in a value spot to cleanse data. Imputation might be a better choice. Must run model and see.
#print(traindf.head(n=5))
#print(traindf.describe())
#print(traindf.shape)
print(traindf.mean(axis=0).shape, traindf.mean(axis=0).mean())
traindf = np.vstack([traindf,traindf.mean(axis=0)*1.5])
#traindf = np.vstack([traindf,traindf.mean(axis=0)*1.6])
print(traindf.shape)
