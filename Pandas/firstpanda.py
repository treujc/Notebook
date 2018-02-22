import numpy as np # Numpy is generally used for making fancier lists called arrays and series.
import pandas as pd # Pandas is super important, it's the foundation data analysis library we're using.
import matplotlib.pyplot as plt # Matplotlib is the python plotting library and folks generally import it as "plt"
import seaborn as sns  # Seaborn is a wrapper for Matplotlib and makes some things easier, generally imported as "sns"

database = 'wildlife.csv' # Dataset location

#df = pd.read_csv(database, low_memory=False) # Read in a CSV file and store the contents in a dataframe (df)
#print(df.shape)
# Head() the dataframe
#print(df.head(n=10)) #print(df[:10])
# Accessing the features (column names)
#print(df.columns)
# Accessing the index (row names)
#print(df.index)
#Describe the Dataset
#print(df.describe())

# Re-reading the data file to clean up NULL values that make ugly graphs
df = pd.read_csv(database,
                 low_memory=False,             ### Prevents low_memory warning
                 na_values=['UNKNOWN', 'UNK'], ### Adds UNKNOWN and UNK to list of NULLs
                 na_filter=True,               ### Detect NA/NaN as actual NULL values
                 skip_blank_lines=True)        ### Skip boring blank lines

#Tells you column information about the dataset.
#df.info()

# These are the columns we're going to take from the original dataframe
subset_list = ["INCIDENT_DATE",
               "OPERATOR",
               "STATE",
               "AIRPORT",
               "PHASE_OF_FLT",
               "SPECIES"]

# We're saving them into a new dataframe
df = pd.DataFrame(data=df, columns=subset_list)

#Drop NaN rows.
df = df.dropna()

# ...and resetting the index
df = df.reset_index(drop=True)

df["OPERATOR"].value_counts().head(10)
# Get the numnber of occurances of each operator
operator_counts = df.OPERATOR.value_counts()
# Split and Save the Operator names in a variable
operators = operator_counts.index
# Split and Save the counts in another variable
counts = operator_counts.get_values()

#GroupBy example.
groupby_obj = df.groupby('STATE')
#print(groupby_obj.count())

# Create and Set the color palette
paired_palette = sns.color_palette("colorblind")
sns.set_palette(paired_palette, 10)

# Rotate the x-labels
plt.xticks(rotation=45)

# Add the x-axis title
plt.xlabel("x-axis Title: Airline operators", fontsize=20)

# Add the y-axis title
plt.ylabel("y-axis Title: Number of birdstrikes", fontsize=20)

# Add the plot title
plt.title("Main title: Birdstrikes per Airline Operator", fontsize=20)

# Create the plot
#barplot = sns.barplot(x=operators[:10], y=counts[:10])
barplot = sns.barplot(x=operators, y=counts)
#Display the plot.
plt.show()


#print(barplot)
#print(df.shape)
#print(df.info())
#print(df.head())
#print(df.describe())
