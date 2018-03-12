## Outlier Detection Assignment

### Introduction

We will be doing outlier detection on parts failure data.

https://www.kaggle.com/uciml/aps-failure-at-scania-trucks-data-set

You are welcome to look at example analyses of these data to help
understand better how to structure the analysis, but the goal here is
to apply the outlier detection algorithm techniques that we have learned.

If you want to account for missing values here is a good tutorial resource.

https://www.kaggle.com/dansbecker/handling-missing-values

The above resource mentioned the concept of a train/test split.  This
concept is very important and will become second nature to you.  If
you would like to get move ahead then read the following before
beginning the assignment.

https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6

If you are not yet comfortable with missing values then you may drop those observations and/or columns.

### The data

The dataset consists of data collected from heavy Scania trucks in everyday usage. The system in focus is the Air Pressure system (APS) which generates pressurized air that is utilized in various functions in a truck, such as braking and gear changes. The datasets' positive class consists of component failures for a specific component of the APS system. The negative class consists of trucks with failures for components not related to the APS. The data consists of a subset of all available data, selected by experts.
Content

The training set contains 60000 examples in total in which 59000 belong to the negative class and 1000 positive class. The test set contains 16000 examples. There are 171 attributes per record.

The attribute names of the data have been anonymized for proprietary reasons. It consists of both single numerical counters and histograms consisting of bins with different conditions. Typically the histograms have open-ended conditions at each end. For example, if we measuring the ambient temperature "T" then the histogram could be defined with 4 bins where:

The attributes are as follows: class, then anonymized operational data. The operational data have an identifier and a bin id, like "Identifier_Bin". In total there are 171 attributes, of which 7 are histogram variables. Missing values are denoted by "na".

### The Assignment

Please format your solution as a Jupyter notebook. The analysis you are about to perform is ensure your solution has the following sections.

Section 1: EDA - Summarizing tables and plots
Section 2: Data cleaning - Document what you did to your data and why
Section 3: Model - Implement your model AND write up what your model is doing in plain English
Section 4: Results - Provide some text that interprets your results.  Make some conclusions and discuss what you might do next if your had more time.

You have some choices here when it comes to complexity--essentially how far down the rabbit hole do you want to go. Sections 1 and 2 are pretty straightforward. One possibility is to create an $X$ that can be used directly with this example code.

http://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html#sphx-glr-auto-examples-covariance-plot-mahalanobis-distances-py

Another choice is to dig through the gene expression example to implement a PCA into elliptical envelop model.  Finally, you could implement any 1 or more of the following algorithms from Sklearn.

http://scikit-learn.org/stable/modules/outlier_detection.html

The plotting should be copy and paste--the time investment will come
with gathering enough insight into the method that you selected that
you can **explain** it to someone who does not have this domain
knowledge.
