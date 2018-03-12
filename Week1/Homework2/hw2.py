import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.covariance import EllipticEnvelope

mat = np.loadtxt("aps_failure_description.txt")
covs = pd.read_csv("aps_failure_training_set.csv")#usecols=[0,1,2,4,5])
print(covs)
print(mat.shape)
#print(mat.mean(axis=0).shape, mat.mean(axis=0).mean())
#mat = np.vstack([mat,mat.mean(axis=0)*1.5])
#mat = np.vstack([mat,mat.mean(axis=0)*1.6])
# print(mat.shape)
